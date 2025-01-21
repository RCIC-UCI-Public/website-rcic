.. _job examples:

Job examples
============

.. contents::
   :local:

This section has several examples of submission scripts for the most common applications.
You will have to tailor the :tt:`SBATCH` options for your requirements (i.e., partition,
cores/memory, GPU, etc.).

Information about requesting resources for the jobs such as memory, local
scratch, time, etc are explained in :ref:`request resources`.

.. _using aliases:

Using Aliases
-------------

You can use aliases and environment variables that are defined in your
:tt:`.bashrc` file in your Slurm submit scripts.

A user panteater has in :tt:`.bashrc`:

.. code-block:: bash

   alias pub='cd /pub/panteater'
   export MYPUB=/pub/panteater

The following script can be used to verify that the defined alias :tt:`pub` and
environment variable :tt:`MYPUB` are accessible in Slurm job:

.. centered:: File alias.sub

.. literalinclude:: files/alias.sub
   :language: bash

Note, first line :tt:`#!/bin/bash -l` requests login shell, this is needed to
execute  your :tt:`.bashrc` on the node where the job is run

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
   *free-gpu* partition. To use one of GPU partitions add to your submit script:

   .. code-block:: bash

      #SBATCH -p free-gpu   # specify free-gpu partition

#. GPU number

   .. important:
      | Nearly 100% of applications on the cluster will use only 1 GPU.
      | **GPU number should be set to 1.**
      | **None of Perl, Python, or R-based applications need multi-GPU**.

      | Very few applications can use multiple GPUs in *P2P* (peer-2-peer) mode.
        For example, *Amber*, *VASP* and *NAMD*.
        These applications need to be specially designed and compiled
        with very specific flags and options to be able to use multi-GPU acceleration.

   To use set the GPU number add  to your submit script:

   .. code-block:: bash

      #SBATCH --nodes=1
      #SBATCH --gres=gpu:1    # specify 1 GPU

#. OPTIONAL: GPU type

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


An example of a GPU job submit script:

   .. code-block:: bash

      #SBATCH -J gpuJob                   # job name
      #SBATCH --nodes=1                   # request to run on 1 node
      #SBATCH -p gpu                      # request gpu partition
      #SBATCH --gres=gpu:1                # request 1 gpu
      #SBATCH -t 5-00:00:00               # set time limit 5 days
      #SBATCH --tasks-per-node=1          # request 1 task per node
      #SBATCH --cpus-per-task=1           # request 1 cpu per task
      #SBATCH --mem=16gb                  # request 16Gb of memory
      #SBATCH --account panteater_lab_gpu
      #SBATCH --output slurm-%x.%A.out

      <your job commands>

The above job request translates into the following:

- Job requested: cpu=1, mem=16Gb, node=1, gpu=1. Total billing is 33 = 32(gpu) + 1(cpu)
- Job is allocated: cpu=2, mem=16Gb, node=1, gpu=1. Total billing is 34 = 32(gpu) + 2(cpu).
  The CPU increase is due to the memory request of 16Gb (for gpu partition max memory per cpu is 9Gb).

.. _job jupyter hub:

Jupyterhub Portal
-----------------

Sometimes applications are available via containers on our *Jupyterhub portal*.
This includes many Bioinformatics applications, Rstudio, etc. Below are the
steps to start a container.

1. **Authenticate at Jupyterhub portal**

   Point your browser
   to `https://hpc3.rcic.uci.edu/biojhub4/hub/login <https://hpc3.rcic.uci.edu/biojhub4/hub/login>`_
   You will see the following screen where you will Use your usual login
   credentials (UCInetID and password) to sign in:

   .. figure:: images/jhub-signin.png
      :align: center
      :width: 90%
      :alt: sign in
 
      Sign in

#. **Select your server configuration and login**

   After  a successful authentication you will see a screen with server options as in the figure below:

   .. figure:: images/jhub-login.png
      :align: center
      :width: 90%
      :alt: server options

      Choose Server Options

   **Modify**

   - :guilabel:`Select Partition/Reservation to use` - choose one of partitions or reservations
   - :guilabel:`Select Account to Charge` - choose one of your Slurm accounts
   - :guilabel:`Select a Containerized Notebook image` - select your desired container
     Note, if you used this portal before check carefully the updated list of
     containers. The older containers names are prefixed with *Centos7*,
     new containers with *Rocky8*.
   - change number of CPUs  and amount of memory if needed

   Press :guilabel:`Start`.  You may see a screen that looks similar to:

   .. figure:: images/jhub-spawn.png
      :align: center
      :width: 90%
      :alt: container starting

      Container is starting

#. **Your server environment**

   Once the notebook is done spawning, you will get a Launcher screen with a number GUI apps you can use.
   The first time you start your Lab interface it will look similar to:

   .. figure:: images/jhub-initial-lab.png
      :align: center
      :width: 90%
      :alt: container initial lab

      Container initial lab

   The container is a subset of the full HPC3 software stack. A standard Jupyter Notebook can be started
   from within your lab server. You also have access to a Linux command-line terminal, if you need it.
   You may need to download/upload files, or install a few R or Python
   packages. Please see :ref:`install jupyter` guide.

   .. important:: | **You must have sufficient space in your $HOME in order to run a session**.
      | If your $HOME is full the server will  fail to start with an error similar to the following
      | :red:`Spawn failed: Server at <...> didn't respond in 300 seconds`
      | where :red:`<...>` shows the http address of a compute node where the server was placed to start.

      **You need to bring your $HOME usage under the quota before
      you can start your session**. Please see :ref:`home quotas <home quotas>`.

#. **Your server generated files**

   Your running container generates session files and directories. Usually, these are placed in
   your $HOME. For example, if you login on HPC3 you might see in your $HOME:

   .. code-block:: console

      [user@login-x:~]$ ls
      biojhub4.12098786.err 
      biojhub4.12098786.out 
      biojhub4_dir           

   * :tt:`biojhub4.12098786.err` is a session error file. The number in the
     file name is a Slurm jobID. The file contains 
     info messages about the session plus will have any error messages which are helpful 
     to identify reasons for container failure to start or work.
   * :tt:`biojhub4.12098786.out` is a session output file. It contains 
     mostly environment settings associated with the container.
   * :tt:`biojhub4_dir` - a directory to keep container generated files (temporary, cache, or persistent). 
     This is NOT a place where you work with your data files and programs, this is needed for a container. 

   If you run many sessions without clearing out these files and directories
   you can fill up your $HOME quota and your container will not start a new
   session or will fail to continue the current one. 

   One can set an alternative place for :tt:`biojhub4_dir` in the pub area. 
   You will need to edit your :tt:`~/.bashrc` file and add at the end a line
   using your account in place of UCINetID:

   .. code-block:: console
   
      export biojhub4HOME="/pub/UCInetID/biojhub4_dir"

   Your next invocation of the container will write session files in your
   :tt:`/pub/UCInetID/biojhub4_dir` location. The :tt:`biojhub4.*.err`
   and :tt:`biojhub4.*.err` files are still written in your $HOME and
   need a periodic removal.

#. **Shutdown your server**

   Be sure to stop your Juputerhub server after you are done with your work.
   This releases backend computing resources for other active computational needs.
   Your notebooks and other files should be saved prior to shutting down your lab.
   Jupyter writes a *state* file for your lab, so that when you relaunch, you
   will be back where you were prior to shutting down.

   .. attention:: The shutdown process involves (1) shutting down ALL your notebooks (2) then 
                  shutting down the server. If you simply shutdown the server, the notebooks
                  remain running and consume server resources. 

   **Step 1: Shut down notebooks**

   For each active notebook, from the :guilabel:`File` menu choose :guilabel:`Close and Shutdown Notebook`:

   .. figure:: images/close-notebook-1.png
      :align: center
      :width: 90%
      :alt: close notebook

      Close and Shutdown Notebook

   There will be a pop-up window asking to confirm, click :guilabel:`Ok`

   .. figure:: images/close-notebook-1-confirm.png
      :align: center
      :width: 50%
      :alt: confirm close notebook

      Confirm Closing Notebook

   Alternatively, choose the sessions tab on the left hand panel and click
   :guilabel:`SHUT DOWN` for each session:

   .. figure:: images/close-notebook-2.png
      :align: center
      :width: 90%
      :alt: close notebook method 2

      Alternative notebook closure method

   **Step 2: Shutdown server**

   From the :guilabel:`File` menu choose :guilabel:`Hub Control Panel`:

   .. figure:: images/jhub-logout-1.png
      :align: center
      :width: 90%
      :alt: control panel

      Hub Control panel

   and you will be forwarded to
   a screen where you can press on :guilabel:`Stop My Server` to shut down the server:

   .. figure:: images/jhub-logout-2.png
      :align: center
      :width: 90%
      :alt: server logout

      Server logout

   your window should look similar to the following when the server is stopped:

   .. figure:: images/jhub-logout-3.png
      :align: center
      :width: 90%
      :alt: server logout result

      Server Logout Result

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
   For the :tt:`ip` the following command will automatically fill in the correct
   value, for example:

   .. code-block:: console

      [user@hpc3-14-00:~]$ jupyter notebook --no-browser --ip=$(hostname -s) --port=8989
      [I 18:19:57.912 NotebookApp] JupyterLab extension loaded from /opt/apps/anaconda/2020.07/lib/python3.8/site-packages/jupyterlab
      [I 18:19:57.912 NotebookApp] JupyterLab application directory is /opt/apps/anaconda/2020.07/share/jupyter/lab
      [I 18:19:57.914 NotebookApp] Serving notebooks from local directory: /data/homezvol0/panteater
      [I 18:19:57.914 NotebookApp] The Jupyter Notebook is running at:
      [I 18:19:57.914 NotebookApp] http://hpc3-14-00:8989/?token=ddfb32c5804b57a452e3f66d2d1572e35af845e84b138dc9
      [I 18:19:57.914 NotebookApp]  or http://127.0.0.1:8989/?token=ddfb32c5804b57a452e3f66d2d1572e35af845e84b138dc9
      [I 18:19:57.914 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
      [C 18:19:57.919 NotebookApp]
          To access the notebook, open this file in a browser:
              file:///data/homezvol0/panteater/.local/share/jupyter/runtime/nbserver-4042129-open.html
          Or copy and paste one of these URLs:
              http://hpc3-14-00:8989/?token=ddfb32c5804b57a452e3f66d2d1572e35af845e84b138dc9
           or http://127.0.0.1:8989/?token=ddfb32c5804b57a452e3f66d2d1572e35af845e84b138dc9

   At this point, you don't have a prompt and you cant do anything in
   this window as your Jupyter notebook is running.

   Note the last URL line of the output above, it includes local host, port and a token.
   Take a note of this line and copy it. You will need to use it on your laptop in the browser.
   The URL line to use must start with :tt:`http://127.0.0.1:`.

   Note, your output from ``jupyter notebook`` command  will have a different
   port, host and a token string.

6. On your laptop connect to the cluster in a new terminal window using ssh tunnel and information
   about your Jupyter notebook start. For our example, for the settings
   produced by the above steps (host *hpc3-14-00* and port *8989*) and for using a local laptop
   port 9090 a user will do:

    .. code-block:: console

       ssh -L 9090:hpc3-14-00:8989 ucinetid@hpc3.rcic.uci.edu

   * Use your ucinetid. When asked for a password and DUO authentication, use your
     usual credentials.
   * Note, the first occurrence of port in the ``ssh`` command
     :tt:`9090` is a local port on your laptop, and you can pick any free port on your laptop
     (use your laptop documentation how to find a free port).
   * The second port :tt:`8989` is the remote port on the cluster node that was configured for
     use by Jupyter when you run the ``jupyter`` command.

   If you pick a local port that is already in use the ``ssh`` command will
   fail, simply use another port number above 6000.

7. On your laptop, open your browser and paste into the URL address area the URL string that was produced by
   starting your Jupyter instance (in step 5) and changing port for your
   chosen local port (use a line from your output):

   | :bluelight:`http://127.0.0.1:`:red:`9090`:bluelight:`/?token=ddfb32c5804b57a452e3f66d2d1572e35af845e84b138dc9`

   Your Jupyter Notebook will be running in the browser on your laptop.

.. attention:: | You can simplify and use the same ports on local and remote hosts.
               | In this case for our example:
               | - in step 6, ssh command will have the same number for local and remote ports
               |   ``ssh -L 8989:hpc3-14-00:8989 ucinetid@hpc3.rcic.uci.edu``
               | - in step 7, you simply copy and paste unchanged URL line into your browser:
               |    http://127.0.0.1:8989/?token=ddfb32c5804b57a452e3f66d2d1572e35af845e84b138dc9

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

.. note:: | To start Matlab non-interactively, use the **-batch** option.
          | To start Matlab interactively, use the **-r** option.

1. Interactive job

   Get an interactive node and start Matlab 

   .. code-block:: console

      [user@login-x:~]$ srun -p free --pty /bin/bash -i
      srun: job 2839817 queued and waiting for resources
      srun: job 2839817 has been allocated resources
      [user@hpc3-y-z:~]$ module load MATLAB/R2020a
      [user@hpc3-y-z:~]$ matlab -r

#. Single core/CPU

   .. centered:: File matlab-single-cpu.sub

   .. literalinclude:: files/matlab-single-cpu.sub
      :language: bash

   The above submit script will submit the Matlab code :tt:`mycode.m` with specified requested resources.
   Note, you dont  need to specify :tt:`.m` extension, Matlab automatically appends it.
   Because the default is one CPU per task, :tt:`-n 1` can be thought of as requesting just one CPU.

   The equivalent command-line method (lines are broken for readability):

   .. code-block:: console

      [user@login-x:~]$ module load MATLAB/R2020a
      [user@login-x:~]$ sbatch -p standard -N 1 -n 1 -t 05-00:00:00 \
                        --wrap="matlab -batch -singleCompThread mycode -logfile mycode.out"

#. Multiple core/CPU

   .. centered:: File matlab-multi-cpu.sub

   .. literalinclude:: files/matlab-multi-cpu.sub
      :language: bash

   The above will submit the Matlab code :tt:`mycode.m` with specified requested resources.
   Note, you dont  need to specify :tt:`.m` extension, Matlab automatically appends it.
   Because the default is one CPU per task, :tt:`-n 12` can be thought of as requesting 12 CPUs.

   The equivalent command-line method (lines are broken for readability):

   .. code-block:: console

      [user@login-x:~]$ module load MATLAB/R2020a
      [user@login-x:~]$ sbatch -p standard -N 1 -n 12 -t 02-00:00:00 \
                        --wrap="matlab -batch -singleCompThread mycode -logfile mycode.out"

#. Parallel pool on a single node 

   Matlab jobs can be run on multiple CPUs in a parallel pool. This
   requires use of  :tt:`parpool` and :tt:`parcluster` commands in
   Matlab script to setup the pool. The :tt:`parfor` loop is used to distribute iterations to multiple workers
   where each worker is running on a different CPU.

   .. note:: | Current UCI Matlab license does not include **MATLAB Parallel Server**. 
             | This means  running parallel jobs across multiple nodes is not supported.
             | :red:`Parallel pool jobs can be run only on a single node`.

   .. centered:: File matlab-parallel.sub

   .. literalinclude:: files/matlab-parallel.sub
      :language: bash

   The above submit script will submit the Matlab code :tt:`prime.m` with specified requested resources
   and collect desired output in the output file :tt:`matlab-example.out` (separate from SLURM output file).
   Note that requested number of tasks is used in Matlab script to setup the
   parallel pool size via a SLURM variable :tt:`SLURM_NTASKS`.
   Contents of prime.m:

   .. centered:: File prime.m

   .. literalinclude:: files/prime.m
      :language: matlab

   Changing the Matlab code to :tt:`hello.m` in the submit script  can run "Hello World" example
   that shows another way to use parallel workers.

   .. centered:: File hello.m

   .. literalinclude:: files/hello.m
      :language: matlab

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

1. **Single core/CPU**

   Nearly all R jobs will only use a single core. 

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

2. **Single node Parallelization**

   When working on a single compute node, one can use R *parallel* libraries
   to achieve the *processor level parallelism*.  Your code must use **library("parallel")**
   When you request X CPUs your code will run on a single node (serial job)
   but will be using X requested CPUs in parallel.


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

3. **Multi-Node Parallelization** 

   There are very few jobs that need this. 

   One can use parallelization across multiple compute nodes. 
   To allow for communication between R processes running on different compute
   nodes your job neds to meet the following requirements:

   - the desired R software package must be using MPI, specifically must use
     *library('Rmpi')*. The desired software package and the Rmpi library must be installed by the user. Before
     installing load one of the MPI modules in addition to your R module.
     For example for *R/4.3.3* use *openmpi/4.1.2/gcc.11.2.0*
   - your submit script must load the same R and MPI modules that were used for the library install.
   - your submit script must request a number of nodes and a number of CPUs to use. 
   - your submit script actual execute command must use ``mpirun``

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
      srun: job 1839817 queued and waiting for resources
      srun: job 1839817 has been allocated resources
      [user@lhpc3-y-z:~]$ module load rstudio/1.4.1106
      [user@lhpc3-y-z:~]$ module load R/4.0.2
      [user@hpc3-y-z:~]$ rstudio

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
      srun: job 1839817 queued and waiting for resources
      srun: job 1839817 has been allocated resources
      [user@hpc3-y-z:~]$ module load rstudio/1.4.1106            # load rstudio module
      [user@hpc3-y-z:~]$ module load R/4.0.2                     # load R module
      [user@hpc3-y-z:~]$ QMLSCENE_DEVICE=softwarecontext rstudio # enforce rendering in rstudio

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

| :red:`Stata is a licensed software and is only available to users whose labs paid for the license`. 
| See :ref:`licensed software` for details.

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

| :red:`VASP is a licensed software and is only available to users whose labs paid for the license`. 
| See :ref:`licensed software` for details.

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

.. _namd job:

NAMD
----

1. Single node multi-CPU job using MPI:

   .. literalinclude:: files/namd-mpi-singlenode.sub
      :language: bash

#. Multi node multi-CPU job using MPI:

   .. literalinclude:: files/namd-mpi-multinode.sub
      :language: bash

#. Multi node multi-GPU job using MPI:

   .. literalinclude:: files/namd-gpu-multinode.sub
      :language: bash
