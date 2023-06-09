.. _job examples:

Job example scripts
===================

This section has several examples of submission scripts for the most common applications.
You will have to tailor the :tt:`SBATCH` options for your requirements (i.e., partition,
cores/memory, GPU, etc.).

Information about requesting resources for the jobs such as memory, local
scratch, time, etc are explained in :ref:`request resources`.

.. _job array:

Array
-----

Job arrays provide a way to submit a large number of similar jobs at once.
All jobs must have the same initial options (e.g. memory needs, time limit, etc.),
but usually have different input parameters.

Using a job array instead of a large number of separate serial jobs is advantageous
since the scheduler does not have to analyze job requirements for each task in the array
separately, so it will run these jobs more efficiently.

It is also much easier for the user to create 1 submit script instead of multiple
submit scripts.

Job arrays are only supported for batch jobs.
The array index values are specified using the :tt:`--array` or :tt:`-a` option
of the ``sbatch`` command or in the submit script. The array index can be
specified in a few ways:

.. code-block:: bash

   #SBATCH --array=0-200             # index values from 0 to 200 inclusive
   #SBATCH --array=1,3,5,7,9         # index values 1,3,5,7,9
   #SBATCH --array=0-20:2            # step size 2, index values 0,2,4,...,20
   #SBATCH --array=1-1000%10         # index values from 1 to 1000, run 10 tasks simultaneously

.. note:: You should not use a job array to submit tasks with very short run times,
          e.g. much less than an hour. Tasks with run times of only a few minutes
          should be grouped into longer jobs using GLOST, GNU Parallel,
          or a shell loop inside of a job (see the :ref:`array short tasks`).

Please see in-depth `Slurm Array Jobs <https://slurm.schedmd.com/job_array.html>`_
documentation.

.. _array env:

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

Job arrays will have additional environment variable set as follows:

:SLURM_ARRAY_JOB_ID:
  the submitted batch job job ID, or the first job ID of the array
:SLURM_ARRAY_TASK_ID:
  the job array index value, each task has a different one
:SLURM_ARRAY_TASK_COUNT:
  the number of tasks in the job array
:SLURM_ARRAY_TASK_MAX:
  the highest job array index value
:SLURM_ARRAY_TASK_MIN:
  the lowest job array index value

For example, the following very simple test script is for an array job with 4
tasks. It does nothing computational but shows what variables are
available for the job:

.. centered:: File array-vars.sub

.. literalinclude:: files/array-vars.sub
   :language: bash

We can submit this file as a job and check the result of the submission, for
example:

.. code-block:: console

   [user@login-x:~]$ sbatch array-vars.sub
   Submitted batch job 22413720
   [user@login-x:~]$ squeue -u panteater
   JOBID       PARTITION    NAME     USER    ACCOUNT ST  TIME CPUS NODE NODELIST(REASON)
   22413720_1  free       mytest panteater panteater  R  0:01    1    1 hpc3-l18-05
   22413720_2  free       mytest panteater panteater  R  0:01    1    1 hpc3-l18-05
   22413720_3  free       mytest panteater panteater  R  0:01    1    1 hpc3-l18-04
   22413720_4  free       mytest panteater panteater  R  0:01    1    1 hpc3-l18-04

Note, each array task will have a different JOBID and
will produce 2 output files, one for Slurm stderr and one for Slurm stdout.
The file names are per specification in the submit script.
The :tt:`mytest.*.err` files should be empty, and the :tt:`mytest.*.out` files will have
the output from the tasks.

.. attention:: | If you only use :tt:`%A` in the logs file name specification,
               | all array tasks will write to a single file.
               | **The performance of the job run will be drastically reduced**.
               | Make sure to use both :tt:`%A` and :tt:`%a` as was shown in the submit script.

.. _array indexing:

Array indexing
^^^^^^^^^^^^^^

**Simple case**

The following example shows how to use environment variables in the array job.
This job will be scheduled as 100 independent tasks.  Each task has a time limit
of 1 hour and each task may start at a different time on a scheduled node.

The script references :tt:`$SLURM_ARRAY_TASK_ID` (1) to select an input file
and (2) to set a command line argument for the application.

.. centered:: File array.sub

.. literalinclude:: files/array.sub
   :language: bash

In this example script, for a 100-task job array the input files were
named :tt:`data_file_1.txt` through :tt:`data_file_100.txt`
which allowed the user to use :tt:`$SLURM_ARRAY_TASK_ID` to specify the file name.

**More complex case**

Often files are not named in that precise manner but can still be referenced
using the task ID.
For example if you have a directory :tt:`inputs/` with 100 files that end in :tt:`.txt`, you can use
the following approach in your submit script to get the name of the file for each task automatically:

.. code-block:: console

   filename=$(ls inputs/*.txt | sed -n ${SLURM_ARRAY_TASK_ID}p)
   MyProg  $filename

Here, in the first line, a command ``ls`` list all the files with needed naming
convention (the list will be 100 names long) and pipes the output into the ``sed``
command which takes a single line from the output and assigns it to the
variable :tt:`filename`. The single line corresponds to the to :tt:`SLURM_ARRAY_TASK_ID`
order in the list of files.

The second line simply executes the needed program with the variable which holds
now a specific file name for this specific array task.

**Multiple input parameters**

Array indexing can be used for multiple input parameters to a program.
Let say a program X requires 3 parameters, a file name and 2 numbers.
A user can create a simple text file that lists all needed parameters
for the desired tasks:

.. code-block:: bash

   /a/path/to/fileM    23 14.5
   /a/other/path/fileZ 12 11.2
   /a/path/to/fileS     1  2.2
   < remaining lines are cut >

Then in the Slurm submit script a user can request 20 array tasks
(same number as the number of parameters lines in the created file)
and provide the needed parameter for each task as:

.. code-block:: bash

   INPUT=/path/to/params.txt
   Args=$(awk "NR==$SLURM_ARRAY_TASK_ID" $INPUT)
   progX $Args

Here, variable :tt:`Args` will hold 3 values that correspond to a line in
:tt:`params.txt` file, the line number is SLURM_ARRAY_TASK_ID.
The last line simply runs the desired  program on 3 parameters for the current array task.

.. _array short tasks:

Running many short tasks
^^^^^^^^^^^^^^^^^^^^^^^^

When each array task is short (seconds or a few minutes), array jobs
become inefficient and overload the scheduler because time spent on managing
tasks will be longer than doing actual work. This is a negative impact not
only on your job but on all other users.

When you have hundreds or thousands of very short tasks, it is better to
combine simple array with a loop that groups multiple tasks for efficiency.

In the following example, we specify 4 array tasks,
then use shell variables and loop to set the number of runs for each array
task to do and the starting and ending number of runs for them.
The submit script will do 4,000 runs of a program
(here substituted by ``echo`` for simplicity) where each run takes just a few seconds to complete.
Instead of running an array job with 4,000 tasks, the script will be much more efficient
to run 4 array tasks where each completes 1,000 runs.

.. centered:: File array-short-tasks.sub

.. literalinclude:: files/array-short-tasks.sub
   :language: bash

.. _job dependent:

Dependent
---------

Job dependencies are typically used to construct pipelines where jobs need to be launched
in sequence upon the successful completion of previously launched jobs.
Dependencies can also be used to chain together long simulations requiring multiple steps.

With Slurm this is done by using the :tt:`--dependency` feature. To familiarize yourself with the dependency feature
take a look at the man page ``man sbatch`` and read dependency section.

Here is an example workflow of commands that shows how to use this feature.

1. Submit a 1st job that has no dependencies and set a variable to hold the job ID

   .. code-block:: console

      [user@login-x:~]$ jobid1=$(sbatch --parsable first_job.sub)

2. Submit a 2nd job with a condition that
   *will launch only after the first one completed successfully*.
   Set a variable to hold this 2nd job ID.

   .. code-block:: console

      [user@login-x:~]$ jobid2=$(sbatch --dependency=afterok:$jobid1 second_job.sub

3. Submit a 3rd job that depends on a successful completion of the second job.

   .. code-block:: console

      [user@login-x:~]$ jobid3=$(sbatch --dependency=afterok:$jobid2 third_job.sub)

4. Submit the last job with a condition that
   *will launch only after the 2nd  and the 3rd jobs are completed successfully*.

   .. code-block:: console

      [user@login-x:~]$ sbatch --dependency=afterok:$jobid2,afterok:$jobid3 last_job.sub

5. Show dependencies in ``squeue`` output:

   .. code-block:: console

      [user@login-x:~]$ squeue -u $USER -o "%.8A %.4C %.10m %.20E"

   .. note:: If a dependency condition is not satisfied, then the dependent job will remain
             in the Slurm queue with status **DependencyNeverSatisfied**.  In this case, you
             need to cancel your jobs manually with the ``scancel`` command
             and check for job errors.

.. _job gpu:

GPU
---

To run a GPU job one needs to request:

1. GPU partition

   To see all available partitions use ``sinfo`` command
   that lists all partitions and nodes managed by Slurm. All users can use
   *free-gpu* and *gpu-debug* partitions. To use one of GPU partitions add to
   your submit script

   .. code-block:: bash

      #SBATCH --partition=free-gpu   # specify free-gpu partition

2. GPU type and number

   Currently, HPC3 has a few GPU types.
   GPU type and number are specified with :tt:`gres` directive, for both
   interactive and batch jobs.

   In your Slurm submit script you will need to add

   .. code-block:: bash

      #SBATCH --nodes=1
      #SBATCH --gres=gpu:V100:1    # specify 1 GPU of type V100

   To find out what Generic RESource (GRES) is available use the following command:

   .. code-block:: console

      [user@login-x:~]$ sinfo -o "%60N %10c %10m  %30f %10G" -e

   .. important:: GPU number should be set to 1.
                  Nearly 100% of applications on the cluster will use only 1 GPU.
                  None of Perl, Python, R-based applications need multi-GPU.
                  Very few applications can use multiple GPUs in *P2P* (peer-2-peer) mode.

                  These applications need to be specially designed and compiled
                  with very specific flags and options to be able to use multi-GPU acceleration.
                  A few examples of applications that can do P2P are *Amber*, *VASP* and *NAMD*.

.. _job jupyter hub:

Jupyterhub Portal
-----------------

Sometimes applications are available via containers on our *Jupyterhub portal*.
This includes many Bioinformatics applications, Rstudio, etc. Below are the
steps to start a container that will provide Rstudio along with a few other
applications.

1. Point your browser
   to `https://hpc3.rcic.uci.edu/biojhub3/hub/login <https://hpc3.rcic.uci.edu/biojhub3/hub/login>`_
   You will see the following screen where you will Use your usual login
   credentials (UCInetID and password) to sign in:

   .. image:: images/jhub-signin.png
      :align: center
      :width: 70%
      :alt: sign in

2. After  a successful authentication you will see a screen with server options as in the figure below:

   .. image:: images/jhub-login.png
      :align: center
      :alt: server login

   **Modify**

   - :guilabel:`Select Partition/Reservation to use` - choose one of partitions or reservations
   - :guilabel:`Select Account to Charge` - choose one of your Slurm accounts
   - change number of CPUs  and amount of memory if needed
   - :guilabel:`Select a Containerized Notebook image` - select your desired container.
     Note, if you used this portal before check carefully the updated list of
     containers. The older containers names are prepended with *Centos7*,
     new containers with *Rocky8*.

   Press :guilabel:`Start`.

   Once the notebook is done spawning, you will get a Launcher screen with a number GUI apps you can use.
   One of those buttons is RStudio.

   **You must have sufficient space in your $HOME in order to run a session**.
   If your $HOME is full the server will  fail to start with an error similar to
   the following :red:`Spawn failed: Server at <...> didn't respond in 300 seconds`
   where :red:`<...>` shows the http address of a compute node where the server was placed to start.

   In this case you need to bring your $HOME usage under the quota. Please see
   :ref:`home quotas <home quotas>`.

3. Be sure to stop your Juputerhub notebook server after you are done with your work.
   From the :guilabel:`File` menu choose :guilabel:`Hub Control Panel` and you will be forwarded to
   a screen where you can press on :guilabel:`Stop My Server` to shut down the server:

   .. image:: images/jhub-logout.png
      :align: center
      :width: 70%
      :alt: server logout


.. _Jupyter notebook:

Jupyter Notebook
----------------

Sometime people create specific conda environments with additional
software and wish to run Jupyter notebooks. As we do not allow computational
jobs on login nodes, here are the steps to run notebooks on interactive nodes.

1. Once you login to HPC3, get an interactive node using ``srun`` command.
   The example below will give 1 CPU and default 3 Gb memory. For most cases this is
   sufficient.

   .. code-block:: console

      [user@login-x:~]$ srun -p free --pty /bin/bash -i

   In some instances, users need to request more memory which is done with
   :tt:`--mem=` or :tt:`--mem-per-cpu` directives (see more info in :ref:`request resources`)
   and specify that *all cores should be on a single node*.
   For example, to get 20 Gb for your Notebook do:

   .. code-block:: console

      [user@login-x:~]$ srun -p free --mem=20G --node=1 --pty /bin/bash -i

   Please note, the above requests are for a free partition, depending on what work you do
   you may need a standard partition.

2. After executing ``srun`` command you will be put on a compute node of the cluster.
   Take a note of the host name, it is usually a part of your shell prompt. If unsure
   simply execute this command to find out:

   .. code-block:: console

      [user@hpc3-14-00:~]$ hostname -s

   In this example the node is *hpc3-14-00*

3. Load your desired anaconda module, for example:

   .. code-block:: console

      [user@hpc3-14-00:~]$ module load anaconda/2020.07


4. Pick a high numbered port (above 6000) and check if it is free:

   .. code-block:: console

      [user@hpc3-14-00:~]$ ss -l -n | grep 8989

   If the port is free there will be no output from the command.
   If there is an output from the command, then the port is in use, pick another
   one and check again until you find a free port

5. Start the notebook with the :tt:`--ip`, :tt:`--port` and :tt:`--no-browser` options.
   For the ip the following command will automatically fill in the correct
   value, for example:

   .. code-block:: console

      [user@hpc3-14-00:~]$ jupyter notebook --no-browser --ip=$(hostname -s) --port=8989

   There will be output from the  notebook command and it will include local host string and a token.
   Take a note of this string and copy it. You will need to use it on your laptop in the browser in the last
   step. This string will look similar to:

   .. code-block:: bash

      http://127.0.0.1:8989/?token=ae4ebf3bwd456780a047254898fabsd8234gefde11bb

6. On your laptop connect to the cluster in a terminal window using ssh tunnel and information
   about your Jupyter notebook start. For our example, for the above steps
   settings (host *hpc3-14-00* and port *8989*) a user will do:

    .. code-block:: console

       ssh -L 9090:hpc3-14-00:8989 ucinetid@hpc3.rcic.uci.edu

   Use your ucinetid. When asked for a password, use your
   usual credentials. Note, the first occurrence of port in the ssh command
   *9090* is port on your laptop, and you can pick any free port on your laptop
   (see your laptop documentation how to do this).
   The second *8989* is the port on the cluster node that is configured for use.

7. On your laptop open your browser and paste the string that was produced by
   starting your Jupyter instance in step 5 above into the browser URL address area:

   | :bluelight:`http://127.0.0.1:8989/?token=ae4ebf3bwd456780a047254898fabsd8234gefde11bb`

   Your Jupyter Notebook will be running in the browser on your laptop.

.. _job large memory:

Large memory
------------

Some jobs may need more memory. For these jobs users will need to

* set memory requirement
* and the number of CPUs to use

.. centered:: File large-memory.sub

.. literalinclude:: files/large-memory.sub
   :language: bash

.. _job matlab:

Matlab
------

1. Single core/CPU:

   .. centered:: File matlab-single-cpu.sub

   .. literalinclude:: files/matlab-single-cpu.sub
      :language: bash

   The above submit script will submit the Matlab code :tt:`mycode.m` with specified requested resources.
   Note: because the default is one CPU per task, :tt:`-n 1` can be thought of as requesting just one CPU.

   The equivalent command-line method:

   .. code-block:: console

      [user@login-x:~]$ module load MATLAB/R2020a*
      [user@login-x:~]$ sbatch -p standard -N 1 -n 1 -t 05-00:00:00 \
                               --wrap="matlab -nodesktop -nosplash -singleCompThread \
                               -r mycode -logfile mycode.out"

2. Multiple core/CPU

   .. centered:: File matlab-multi-cpu.sub

   .. literalinclude:: files/matlab-multi-cpu.sub
      :language: bash

   The above will submit the Matlab code [.tt]*mycode.m* with specified requested resources.
   Note: because the default is one CPU per task, [.tt]*-n 12* can be thought of as requesting 12 CPUs.

   The equivalent command-line method:

   .. code-block:: console

      [user@login-x:~]$ module load MATLAB/R2020a
      [user@login-x:~]$ sbatch -p standard -N 1 -n 12 -t 02-00:00:00 \
                               --wrap="matlab -nodesktop -nosplash -singleCompThread \
                               -r mycode -logfile mycode.out"


.. _job mpi:

MPI
---

MPI jobs use multiple cores across different nodes.
The following submit script will use 80 cores across 2 different nodes.
Each core will be allocated a default 3 GB of RAM, for a total of 240 Gb for
the job.

.. centered:: File mpi.sub

.. literalinclude:: files/mpi.sub
   :language: bash

**Special case openmpi**
  This scenario applies ONLY to applications that are compiled using one of openmpi
  modules (versions 4.0.x and 4.1.x) and have failed with the following error
  when run on multiple nodes:

  :red:`[btl_openib_component.c:3655:handle_wc] Unhandled work completion opcode is 136`

  The openmpi versions in 4.0.x and 4.1.x series use **openib** interface which no
  longer works the same way under a new operating system. The solution is to
  instruct openmpi to use **UCX**. This is done via the following in your submit
  script:

  1. :tt:`#SBATCH --constraint="mlx5_ib"` run on nodes with updated IB firmware
  2. use 3 export commands to set the UCX parameters for openmpi
  3. add :tt:`-mca mpl ucx`  parameters  to your mpirun command

  .. centered:: File mpi-special-case.sub

  .. literalinclude:: files/mpi-special-case.sub
     :language: bash

.. _job hybrid:

MPI/OpenMP hybrid
-----------------

A hybrid job uses multiple processes and multiple threads within a process.
Usually, MPI is used to start the multiple processes, and then each process
uses a multi-threading library to do computations with multiple threads.

Here is an example of 8 MPI processes running on 2 nodes (4 MPI tasks per node)
with 5 OpenMP threads per each process, each OpenMP thread has 1 physical core
and needs 3 GB memory. The job requests a total of 40 cores and 120 GB of RAM

.. centered:: File hybrid.sub

.. literalinclude:: files/hybrid.sub
   :language: bash

.. _job openmp:

OpenMP
------

OpenMP jobs use multiple cores on a single machine. Below is an example of a
submission script that utilizes 6 physical cores to run OpenMP program.
**In a strictly OpenMP job the number of nodes is always 1**.

.. centered:: File openmp.sub

.. literalinclude:: files/openmp.sub
   :language: bash

Note, the value of :tt:`OMP_NUM_THREADS` is defined to be equal to the value of Slurm
variable :tt:`SLURM_CPUS_PER_TASK`. This ensures that any change to a number of requested threads is
automatically passed to OpenMP.

.. _job python:

Python
------

1. Single core/CPU

   .. centered:: File python-single-cpu.sub

   .. literalinclude:: files/python-single-cpu.sub
      :language: bash

   The above will submit the Python 3 code with specified requested resources.

   The equivalent command-line method:

   .. code-block:: console

      [user@login-x:~]$ module load python/3.8.0
      [user@login-x:~]$ sbatch -p standard -N 1 -n 1 -t 2:00:00 --mail-type=end \
                               --mail-user=UCInetID@uci.edu --wrap="python3 myscript.py"

2. Multiple core/CPU

   .. centered:: File python-multi-cpu.sub

   .. literalinclude:: files/python-multi-cpu.sub
      :language: bash

   The above will submit the Python 3 code with specified requested resources.

   The equivalent command-line method:

   .. code-block:: console

      [user@login-x:~]$ module load python/3.8.0
      [user@login-x:~]$ sbatch -p standard -N 1 -n 1 -c 12 -t 5- --wrap="python myscript.py"

.. _job r:

R
--

1. Single core/CPU

   .. centered:: File R-single-cpu.sub

   .. literalinclude:: files/R-single-cpu.sub
      :language: bash

   The above will submit the R code :tt:`mycode.R` with specified requested resources.
   Note: because the default is one CPU per task, :tt:`-n 1` can be thought of as requesting just one CPU.

   The equivalent command-line method:

   .. code-block:: console

      [user@login-x:~]$ module load R/4.1.2
      [user@login-x:~]$ sbatch -p standard -N 1 -n 1 -t 1- \
                               --wrap="R CMD BATCH --no-save mycode.R"

2. Multiple core/CPU

   .. attention:: Nearly all R jobs will only use a single core. Please make sure your job is
                  multi-threaded or is explicitly using R parallel libraries.

   .. centered:: File R-multi-cpu.sub

   .. literalinclude:: files/R-multi-cpu.sub
      :language: bash

   The above will submit the R code :tt:`mycode.R` with specified requested resources.
   Note: because the default is one CPU per task, :tt:`-n 12` can be thought of as requesting 12 CPUs.

   The equivalent command-line method:

   .. code-block::

      [user@login-x:~]$ module load R/3.6.2*
      [user@login-x:~]$ sbatch -p standard -N 1 -n 12 -t 00:20:00 \
                               --wrap="R CMD BATCH --no-save mycode.R"

.. _job rstudio:

Rstudio
-------

There a few ways to run Rstudio.

1. **Windows users**

   This method usually works for users who connect to the cluster using
   `MobaXterm <https://mobaxterm.mobatek.net/>`_.

   Once  logged in, claim an interactive session, load rstudio and R modules
   and start ``rstudio``:

   .. code-block:: console

      [user@login-x:~]$ srun -p free --pty --x11 /bin/bash -i
      [user@login-x:~]$ module load rstudio/1.4.1106
      [user@login-x:~]$ module load R/4.0.2
      [user@login-x:~]$ rstudio

2. **Mac users**

   Your local Mac needs to have ``XQuartz`` installed. This is a standard application
   that provides X Window system for Mac OS. Follow Mac installation guide for
   installing applications if you don't have XQuartz installed.

   Login on the cluster using X forwarding. This means using  :tt:`-X`
   or  :tt:`-X -Y` option in the ssh command. For example:

   .. code-block:: console

      ssh -X panteater@hpc3.rcic.uci.edu

   Once logged in, claim an interactive session, load Rstudio
   and R modules. Enforce software rendering engine in the ``rstudio`` command:

   .. code-block:: console

      [user@login-x:~]$ srun -p free --pty --x11 /bin/bash -i   # claim an interactive session
      [user@login-x:~]$ module load rstudio/1.4.1106            # load rstudio module
      [user@login-x:~]$ module load R/4.0.2                     # load R module
      [user@login-x:~]$ QMLSCENE_DEVICE=softwarecontext rstudio # enforce rendering in rstudio

3. **All users**

   If the above method does not work for you (common for Mac users), the alternative way
   is to use our :ref:`Jupyterhub Portal <job jupyter hub>`
   and a container with Rstudio.

.. _job sas:

SAS
---

.. centered:: File sas.sub

.. literalinclude:: files/sas.sub
   :language: bash

The above will submit your SAS code with specified requested resources.

.. _job sra:

SRA toolkit fasterq-dump
------------------------

.. danger:: Running multi-threaded (read multi-CPU) ``fastq-dump``, ``fasterq-dump``
            or ``parallel-fastq-dump`` command directly in any directory
            on DFS filesystem results in a deadlock and makes a server UNUSABLE
            for ALL users until the server is rebooted.

.. important:: SRA tools prior to v. 3 did not handle writing temp files to a separate
               directory. Do not use SRA tools prior to v.3 for fastq-dump or fasterq-dump commands.

.. important:: It is faster to do a ``prefetch`` followed by ``fasterq-dump`` (or any other dump
               version) compare to letting ``fasterq-dump`` do the download.

               If you already prefetched SRA files and have them stored in some directory
               simply use the correct full path to the SRA files in your ``fasterq-dump`` command.

To avoid issues with the  deadlocking users need to use scratch disk when
running above commands.

Follow this simple recipe that will prefetch needed SRA sequences and convert them to fastq format.
All file writing is done in a scratch local disk and the final files are  moved to a desired directory.

.. centered:: File prefetch-fasterq-dump.sub

.. literalinclude:: files/prefetch-fasterq-dump.sub
   :language: bash

Your commands may have additional arguments, use them as needed. The
important option to avoid deadlocking is ``--temp $TMPDIR`` and do downloads in
**$TMPDIR**.

.. _job stata:

Stata
-----

.. centered:: File stata.sub

.. literalinclude:: files/stata.sub
   :language: bash

The above will submit the Stata job (mycode.do) with specified requested resources.

.. _job tensorflow:

Tensorflow
----------

1. Tensorflow CPU only

   .. centered:: File tensorflow-cpu.sub

   .. literalinclude:: files/tensorflow-cpu.sub
      :language: bash

   The above will submit the Tensorflow 2.0 job with specified requested resources.

   The equivalent command-line method:

   .. code-block:: console

      [user@login-x:~]$ module load tensorflow/2.0
      [user@login-x:~]$ sbatch -p standard -N 1 -n 1 -t 02-00:00:00 --wrap="python mycode.py"


2. Tensorflow with GPU

   .. centered:: File tensorflow-gpu.sub

   .. literalinclude:: files/tensorflow-gpu.sub
      :language: bash

   The above will submit the gpu Tensorflow 2.0 job, note request for gpu
   partition and gres resourcds.

   The equivalent command-line method:

   .. code-block::

      [user@login-x:~]$ module load tensorflow/2.0
      [user@login-x:~]$ sbatch -p gpu -N 1 -n 1 -t 02-00:00:00 \
                               --gres=gpu:V100:1 --wrap="python mycode.py"

.. _job vasp:

VASP
----

VASP is a licensed software and is only available to users whose labs paid
for the license. Users must be in specific groups in order to access this software.

In order to be in a specific vasp group we need a confirmation from your PI who bought the
license and we need to have a record of such license.

1. VASP versions 5.4.4 and 6.1.2

   These two versions run in a similar way, just load the desired VASP module.

   Note, that 3 export statements, :tt:`--constraint`  directive and addition of
   :tt:`-mca pml ucx` to the ``mpirun`` command are required.

   .. centered:: File vasp-5.sub

   .. literalinclude:: files/vasp-5.sub
      :language: bash

2. VASP version 6.3.2 CPU

   The following example shows how to run VASP v 6.3.2 compiled with gcc 11
   The module already has correct settings for UCX variables. Please consult
   VASP documentation on how to use *OMP_NUM_THREADS* for multiple threads

   Note, :tt:`--constraint` directive and addition of :tt:`-mca pml ucx` to
   the ``mpirun`` command are required.  The UCX environment variables are
   already set by this version of VASP  module.

   .. centered:: File vasp-63.sub

   .. literalinclude:: files/vasp-63.sub
      :language: bash

3. VASP version 6.3.2 GPU

   To run VASP on GPU, it is required to run on a single node. It is possible to
   use up to 4 GPUs on a single node. Please consult VASP documentation how to
   use multiple GPUs. The following example uses 1 GPU

   .. centered:: File vasp-63-gpu.sub

   .. literalinclude:: files/vasp-63-gpu.sub
      :language: bash
