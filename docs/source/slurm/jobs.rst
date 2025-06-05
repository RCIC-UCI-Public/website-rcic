.. _jobs:

Jobs howto
==========

.. contents::
   :local:

.. _recommendation:

General Recommendations
-----------------------

In this guide, we provide information about how to submit your jobs to Slurm, how
to monitor them and how to request various resources.

In :ref:`job examples` guide  we show  specific in-depth examples how to run array jobs, request GPUs,
CPUs, and memory for a variety of different job types and common applications.

:bluelight:`Get the most from your allocation`
  * Check your past jobs for how many CPU and memory resources were used. Don't request more than needed.
  * Prioritize your own work: testing and low-priority jobs can be free jobs, others should be allocated.
  * Understand that free *comes with no guarantees*: your free job can be killed at anytime.


:bluelight:`Quota Enforcement`
  When users exceed their disk space or CPUs quota allocations the following will happen:

  * users will not be able to submit new jobs
  * running jobs will fail

  .. important:: Please check the available disk space and CPU hours in your Slurm account regularly.
     Delete or archive data as needed.

:bluelight:`Inherited environment`
  All Slurm batch and interactive jobs will inherit *all environment variables* that were
  set in your login shell (on the login node where you are executing job submission).

  By default, there should be none, unless one changes the environment via
  setting environment variables either on command line or in :tt:`$HOME/.bashrc` file
  or is using conda.

  * Check your :tt:`$HOME/.bashrc` and make  sure that there are no environment variables set
    that can cause problems in the ``sbatch`` or ``srun`` commands. Follow
    the :ref:`bash init files` guide.

  * Load modules either in the Slurm submit script
    or on an interactive node after you executed the ``srun`` command and not in the
    login shell before the job submission.

  * If you are using conda please review :ref:`install conda`
    guide that explains how to cleanly separate conda-set environment from your
    login environment.

.. _batch job:

Batch Job
---------

``sbatch``

A batch job is run at some time in the future by the scheduler.
Submitting batch jobs to Slurm is done with the ``sbatch`` command
and the job description is provided by the submit script.

When to use:
  when your job runs for hours or days.

How to submit:
  .. code-block:: console

     [user@login-x:~]$ sbatch your-submit-script.sub

Example job:
  Login on HPC3 and using your favorite editor create
  :tt:`simple.sub` file using the following contents as a template:

  .. literalinclude:: files/simple.sub
     :language: bash

  Edit the Slurm account to charge for the job to either your personal account or lab account.
  Your personal account is the same as your UCInetID.

  Submit the job:

  .. code-block:: console

     [user@login-x:~]$ sbatch simple.sub
     Submitted batch job 21877983

  When the job has been submitted, Slurm returns a job ID (here 21877983)  that will be used to reference the job
  in Slurm user log files and Slurm job reports.
  After the job is finished, there will be 3 files created by the job:

  :slurm-21877983.err:
    Slurm job error log file
  :slurm-21877983.out:
    Slurm job output log file
  :out.txt:
    Output file created by a specific command that was run in the job.

  .. note:: Slurm error and log files are extremely useful especially to track
            progress and issues with the jobs.

.. _interactive job:

Interactive job
---------------

``srun``

The command ``srun`` is used to submit an interactive job which runs in a shell terminal.
The job uses your console for for standard input/output/error.

.. important:: * All interactive jobs are run on a single node, they can not be run on multiple nodes.
               * Interactive jobs are submitted for execution but do not bypass scheduler priority.
                 If your job cannot run immediately, you will wait until Slurm can schedule your request.

When to use:
  when you want to test a short computation, compile
  software, or run an interactive Python or R session.

When NOT to use:
  when your job runs for many hours or days. Use ``sbatch`` instead.

The main difference between ``srun`` and ``sbatch``:

  .. table::
     :class: noscroll-table

     +--------------------------------------------------+-----------------------------------------+
     | Srun                                             | Sbatch                                  |
     +==================================================+=========================================+
     | Interactive and blocking                         | Batch processing and non-blocking       |
     +--------------------------------------------------+-----------------------------------------+
     | You type commands interactively                  | Your commands run unattended            |
     +--------------------------------------------------+-----------------------------------------+
     | Can be used to create job steps in submit scripts| Can do everything ``srun`` can and more.|
     +--------------------------------------------------+-----------------------------------------+

How to submit:
  1. Get an interactive node

     While on a login node, run the ``srun`` command. When it  is executed, the scheduler allocates
     available resource and starts an interactive shell on the available node.
     Your shell prompt will indicate a new *hostname*:

     .. code-block:: console

        [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i
        srun: job 32654143 queued and waiting for resources
        srun: job 32654143 has been allocated resources
        [user@hpc3-y-z:~]$

  #. Execute your interactive commands

     .. code-block:: console

        [user@hpc3-y-z:~]$ module load python/3.10.2
        [user@hpc3-y-z:~]$ myProgRun.py -arg1 someDir/ -d outputDir/ -f file.nii -scale > out

  #. Once done with your work simply type at the prompt:

     .. code-block:: console

        [user@hpc3-y-z:~]$ exit

Example jobs:
  The following is a list of examples of different requests  for interactive jobs.
  The :tt:`--pty /bin/bash -i` options must be the last on a command line
  and should not be separated by other options:

  .. code-block:: console

     [user@login-x:~]$ srun -A PI_LAB --pty /bin/bash -i                     # 1
     [user@login-x:~]$ srun -p free --pty /bin/bash -i                       # 2
     [user@login-x:~]$ srun --mem=8G -p free --pty /bin/bash -i              # 3
     [user@login-x:~]$ srun -c 4 --time=10:00:00 -N 1 --pty /bin/bash -i     # 4
     [user@login-x:~]$ srun -p free-gpu --gres=gpu:V100:1 --pty /bin/bash -i # 5
     [user@login-x:~]$ srun -p free --x11  --pty /bin/bash -i*               # 6

  1. Use *standard* partition and charge to the *PI_LAB* account
  2. Use *free* partition (where it may be killed at any time)
  3. Use *free* partition and ask for 8GB of memory per job (ONLY when you truly need it)
  4. Use *standard* partition and ask for 4 CPUs for 10 hrs
  5. Use *free-gpu* partition and ask for one V100 GPU. :red:`Do not ask for more than 1 GPU!`
     For many jobs the GPU specification can be simply :tt:`--gres=gpu:1` (GPU type makes no difference for the job).
  6. | Start an interactive session with Xforward enabled (option :tt:`--x11`) for GUI jobs.
     | Note, a user  should have logged on HPC3 with ssh Xforward enabled see :ref:`ssh xforward`
       before running this ``srun`` command.

.. _attach to job:

Attach to a job
---------------

``srun --pty --jobid``

.. attention:: The ssh access to compute nodes is turned off

Users will need to use a job ID of a *running job* and to attach to it
if they want to run simple jobs verification commands on the node where their job is running.

Once attached to a job, the user will be put on the node where the job is
running and will **run inside the cgroup (CPU, RAM etc.) of the running job**. This means the user:

  * will be able to execute simple commands such as :tt:`ls, top, ps`.
  * :red:`will not be able to start new processes` that use resources outside of what is specified in
    *jobid*. Any command will use computing resources, and will add to the usage of the job.
  * needs to type ``exit`` after executing desired verification commands in order to
    stop attachment to the job.  The original job will be still running.

Find *jobid* and attach to it:
  .. code-block:: console

     [user@login-x:~]$ squeue -u panteater
       JOBID PARTITION     NAME      USER ST       TIME  NODES NODELIST(REASON)
     3559123      free    Tst41 panteater  R   17:12:33      5 hpc3-14-02
     3559124      free    Tst42 panteater  R   17:13:33      7 hpc3-14-17,hpc3-15-[05-08]

     [user@login-x:~]$ srun --pty --jobid 3559123 --overlap /bin/bash
     [user@hpc3-14-02:~]$


  Execute your commands at the prompt and exit:

  .. code-block:: console

     [user@hpc3-14-02:~]$ top
     [user@hpc3-14-02:~]$ exit
     [user@login-x:~]$

Attach to a specific node using :tt:`-w` switch (for multi-node jobs):
  By default, the user will be put on the first node listed in ``squeue``
  output if running on multi-node.  To attach to a specific node:

  .. code-block:: console

     [user@login-x:~]$ srun --pty --jobid 3559124 --overlap -w hpc3-15-08 /bin/bash
     [user@hpc3-15-08:~]$


Run  command while attaching to the running job:
  Most often users just need to see the processes of the job, etc. Such commands can be run directly.
  For example, to run ``top``:

  .. code-block:: console

     [user@login-x:~]$ srun --pty --overlap --jobid $JOBID top

.. _request resources:

Requesting Resources
--------------------

.. _request nodes:

Nodes
^^^^^

Very few applications that are compiled to run with Open MPI or MPICH need to  use multiple nodes.
Most jobs on HPC3  including all :ref:`interactive jobs <interactive job>` are single node jobs
and must be run on a single node.  If a single node job is submitted to multiple nodes it will either:

  * fail
  * misuse the resources. You will be charged for reserved and unused resources.


How to request a single node:
  :red:`Users should explicitly ask for 1 node`.  This is important to let SLURM know that all your processes
  should be on a single node and not spread over multiple nodes.
  In your submit script use:

  .. code-block:: bash

     #SBATCH --nodes=1                ## (-N) use 1 node

How to request multiple nodes:
  Your submit script need to include desired number of nodes, for example:

  .. code-block:: bash

     #SBATCH --nodes=2                ## (-N) use 2 nodes

.. _request constrains:

Features/Constraints
^^^^^^^^^^^^^^^^^^^^

HPC3 has a heterogeneous hardware with several different CPU types.
You can request that a job only runs on nodes with certain *features*
which is done via a use of constraints.

To request a feature, you must add to your submit script:

  .. code-block:: bash

     #SBATCH --constraint=feature_name

where :tt:`feature_name` is one of the defined features specific to the cluster (or one of the standard features described
in the `Slurm sbatch <https://slurm.schedmd.com/sbatch.html>`_ guide).
Multiple features can be requested and are separated by commas.

We defined the following for node selection:

.. centered:: HPC3-Specific Features

.. table::
   :widths: 20 45 20 15
   :class: noscroll-table

   +---------------------+---------------------------------------+---------------+--------------+
   | Feature             | Node Description                      | Node          | Cores        |
   |                     |                                       |               |              |
   | name                | (processor/storage)                   | count         | min/mod/max  |
   +=====================+=======================================+===============+==============+
   | intel               | any Intel node including HPC legacy   | compute: 215  | 24 / 40 / 80 |
   |                     |                                       |               |              |
   |                     |                                       | GPU: 38       | 32 / 40 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | avx512              | Intel AVX512                          | compute: 191  | 28 / 40 / 48 |
   |                     |                                       |               |              |
   |                     |                                       | GPU: 38       | 32 / 40 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | epyc or amd         | any AMD EPYC                          | 18            | 40 / 64 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | epyc7551            | AMD EPYC 7551                         | 1             | 40 / 64 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | epyc7601            | AMD EPYC 7601                         | 17            | 64 / 64 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | nvme or fastscratch | Intel AVX512 with /tmp on NVMe disk   | 86            | 32 / 48 / 80 |
   +---------------------+---------------------------------------+---------------+--------------+
   | mlx5_ib             | Updated Infiniband firmware           | 243           | 36 / 40 / 80 |
   +---------------------+---------------------------------------+---------------+--------------+
   | mlx4_ib             | Older Infiniband firmware             | 9             | 24 / 40 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+

To request nodes with updated InfiniBand firmware for your MPI-based jobs:

  .. code-block:: bash

     #SBATCH --constraint=mlx5_ib

To request nodes with a large local scratch storage:

  .. code-block:: bash

     #SBATCH --constraint=nvme
     or
     #SBATCH --constraint=fastscratch

  See :ref:`scratch storage` for details.

To request nodes with CPUs capable of AVX512 instructions:

  .. code-block:: bash

     #SBATCH --constraint=avx512

To request Intel nodes with CPUs capable of AVX512 instructions:

  .. code-block:: bash

     #SBATCH --constraint=intel,avx512

.. _scratch storage:

Scratch storage
^^^^^^^^^^^^^^^

Scratch storage is local to each compute node and is the fastest disk access
for reading and writing the input/output job files.

Scratch storage is created for each job automatically as :tt:`/tmp/UCInetID/jobid/`
when the job starts on a compute node. Slurm *knows* this location and
is referring to it  via an environment variable :tt:`$TMPDIR`.
Users don't need to create :tt:`$TMPDIR` but simply need to use it in their
submit scripts.

For example, a user panteater who has 2 running jobs:

  .. code-block:: console

     [user@login-x:~]$ squeue -u panteater
      squeue
     JOBID     PARTITION      NAME      USER  ACCOUNT ST      TIME CPUS NODE NODELIST(REASON)
     20960254   standard  test-001 panteater   PI_lab  R   1:41:12   25    1 hpc3-15-08
     20889321   standard  test-008 panteater   PI_lab  R  17:24:10   20    1 hpc3-15-08

  will have the following directories created by Slurm on :tt:`hpc3-15-08`

  .. code-block:: console

     /tmp/panteater/20960254
     /tmp/panteater/20889321

  .. note:: While the directory is created automatically, it is a :underline:`user responsibility to
            copy`:

            * input files to :tt:`$TMPDIR` before doing computational commands
            * the final results from :tt:`$TMPDIR` to user area before the job ends.

            These copy commands need to be in the Slurm submit script.

Slurm doesn't have any default amount of scratch space defined per job and that may be fine for most, but not all.
The problem of having enough local scratch arises when nodes are shared by multiple jobs and users.
:red:`One job can cause the other jobs running on the same node to fail`, so please be considerate of your
colleagues by requesting storage for your jobs as follows:

:bluelight:`Your job creates a few Gb of temporary data directly in $TMPDIR`
   and handles the automatic creation and deletion of these temp files.
   Many Python, Perl, R, Java programs and 3rd party commercial software will
   write to :tt:`$TMPDIR` which is the default for many applications.

   **Your action**:
     You don't need to do anything special. Do not reset :tt:`$TMPDIR`.

:bluelight:`Your job creates a few Gb of output in the current directory`
   where you run the job and does many frequent small file reads or writes (a few Kb every few minutes).

   **Your action**:
     You will need to use a scratch storage where you bring your job data, write temp files
     and then copy the final output files back when the job is done.

     .. attention::
        In this scenario, Slurm job is run in :tt:`$TMPDIR` which is much faster
        for the disk I/O, then the program output is copied back as a big write
        which is much more efficient compare to many small writes.

        The reason is :red:`parallel filesystem (CRSP or DFS) is not suitable for small
        writes and reads` and such operations need to be off-loaded to the local
        scratch area on the node where the job is executed.
        Otherwise you create an I/O problem not just for yourself but for many others
        who use the same filesystem.

     The following partial submit script shows how to use :tt:`$TMPDIR` for such jobs:

     .. code-block:: bash

        <the rest of submit script is omitted>

        #SBATCH --tmp=20G                 # requesting 20 GB (1 GB = 1,024 MB) local scratch

        # explicitly copy input files from DFS/CRSP to $TMPDIR
        # note, $TMPDIR is already created for your job by SLURM
        cd $TMPDIR
        cp /pub/myacount/path/to/my/jobs/data/*dbfiles  $TMPDIR

        # create a directory for the application output
        mkdir -p $TMPDIR/output

        # your job commands, this is just one possible example
        # output from application goes to $TMPDIR/output/
        mapp -tf 45 -o $TMPDIR/output     # program output directory is specified via -o flag
        mapp2  > $TMPDIR/output/mapp.out  # program output in a specific file

        # explicitly copy output files from $TMPDIR to DFS/CRSP
        cp $TMPDIR/output/* /pub/myaccount/myDesiredDir/

:bluelight:`Your job creates many Gbs of temporary data (order of ~100Gb)`
   **Your action**:
     You will need to submit your job to a node with a lot of local scratch storage
     where you bring your job data, write temp files,
     and then copy the final output files back when the job is done.

     In your submit script define how much scratch space your job needs
     (you may need to figure it out by trial test  run)
     and request the nodes that have fast local scratch area via the following Slurm directives:

     .. code-block:: bash

        #SBATCH --tmp=180G                 # requesting 180 GB (1 GB = 1,024 MB) local scratch
        #SBATCH --constraint=fastscratch   # requesting nodes with a lot of space in /tmp

     Follow the above submit script example to:

       - at job start explicitly copy input files from DFS/CRSP to :tt:`$TMPDIR`
       - at job end explicitly copy output files from :tt:`$TMPDIR` to DFS/CRSP

.. _request memory:

Memory
^^^^^^

There are nodes with different memory footprints. Slurm uses Linux
`cgroups <https://man7.org/linux/man-pages/man7/cgroups.7.html>`_
to enforce that applications do not use more memory/cores than they have been allocated.

Slurm has *default* and *max* settings for a memory allocation per core
for each partition. Please see all partitions settings in :ref:`available partitions`.

:default settings:
  Are used when a job submission script does not specify
  different memory allocation, and for most jobs this is sufficient.

:max settings:
  Are used when a job requires more memory.
  Job memory specifications can not exceed the partition's max setting.
  If a job specifies a memory per CPU limit that exceeds the system limit, the job's count of CPUs
  per task will automatically be increased. This may result in the job failing due to CPU count limits.

.. note:: Please do not override the memory defaults unless your particular job really requires it.
   Analysis of more than 3 Million jobs on HPC3 indicated that more than 98% of jobs fit within
   the defaults.
   With slightly smaller memory footprints, the scheduler has MORE choices as to
   where to place jobs on the cluster, so your job has a better change to start sooner.

How to request more memory:
  You should specify the memory needs via one of the two mutually exclusive directives (one or another but not both):

  | Scenario 1:
  |   :tt:`--mem=X<size>` ask for more total memory for the job
  | Scenario 2:
  |   :tt:`--mem-per-cpu=X<size>` ask for max memory per core and if this is not enough
  |   request more cores.

  where :tt:`X` is an integer and :tt:`<size>` of an optional size
  specification (M - megabytes, G - gigabytes, T - terabytes). A default is in megabytes.

  You will be charged more for more cores, but you use a larger fraction of the node.
  The same directives formats are used in Slurm submit scripts and for
  interactive jobs in any partition.


**Examples of memory requests**:

  1. Ask for the total job memory in submit script

       .. code-block:: bash

          #SBATCH --mem=500           # requesting 500MB memory for the job
          #SBATCH --mem=4G            # requesting 4GB (1GB = 1,024MB) for the job

  #. Ask for the memory per CPU in submit script

       .. code-block:: bash

          #SBATCH --mem-per-cpu=5000  # requesting 5000MB memory per CPU
          #SBATCH --mem-per-cpu=2G    # requesting 2GB memory per CPU

  #. Ask for 180GB for job in standard partition:

       .. code-block:: bash

          #SBATCH --partition=standard
          #SBATCH --mem-per-cpu=6G    # requesting max memory per CPU
          #SBATCH --ntasks=30         # requesting 30 CPUs

     Ask for max memory per CPU and a number of CPUs to make up needed
     total memory for job as *30 x 6Gb = 180Gb*

  #. Use ``srun`` and request 2 CPUs with a default or max memory

     .. code-block:: console

        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=2 --pty /bin/bash -i
        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=2 --mem-per-cpu=18G --pty /bin/bash -i
        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=2 --mem=36G --pty /bin/bash -i

     | The first job will have a total memory *2 x 3Gb = 6Gb*
     | The second and third job each will have a total memory *2 x 18Gb = 36Gb*

  #. Use ``srun`` and request 4 CPUs and 10GB memory per CPU,

     .. code-block:: console
 
        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=4 --mem-per-cpu=10G --pty /bin/bash -i
 
     total memory for job is *4 x 10Gb = 40Gb*

.. note:: For information how to get an  access to higher memory partitions please see :ref:`memory partitions`

.. _request time:

Runtime
^^^^^^^

Slurm has *default* and *max* settings for a runtime
for each partition.  Please see all partitions settings in :ref:`available partitions`.

.. important:: All interactive jobs  submitted with ``srun`` command and
               all batch jobs submitted with ``sbatch`` command
               have time limits whether you explicitly set them or not.

:default settings:
  are used when a job submission script or ``srun`` command do not specify
  runtime, and for most jobs this is sufficient.

:max settings:
  specify the longest time a job can run in a given partition.
  Job time specifications can not exceed the partition's max setting.

When a job requires longer run time than a default it needs to be specified
using time directive :tt:`--time=format` (or the equivalent short notation
:tt:`-t format`.

**Acceptable time formats**:
  ========================= ===============================
   minutes                  days-hours
   minutes:seconds          days-hours:minutes
   hours:minutes:seconds    days-hours:minutes:seconds
  ========================= ===============================

For example, for Slurm script:

.. code-block:: bash

   #SBATCH --time=5        # 5 minutes
   #SBATCH -t 36:30:00     # 36 hrs and 30 min
   #SBATCH -t 7-00:00:00   # 7 days

Similarly,  for ``srun`` command:

.. code-block:: bash

   srun --time=10 <other arguments>      # 10 minutes
   srun -t 15:00:00  <other arguments>   # 15 hours
   srun -t 5-00:00:00 <other arguments>  # 5 days


**Runtime extension**
  If your job and was submitted for the max default time
  and you realize it will not finish by the specified runtime limit
  you can ask for a runtime extension.
  Please see :ref:`change job time limit <modify job>`.

  Note, there is no runtime extension for free jobs.

.. _mail notification:

Mail notification
^^^^^^^^^^^^^^^^^

To receive email notification on the status of jobs, include the following lines in your
submit scripts and make the appropriate modifications to the second line:

.. code-block:: console

   #SBATCH --mail-type=fail,end
   #SBATCH --mail-user=user@domain.com

The first line specifies the event type for which a user requests an email (here failure and end events), the
second specifies a valid email address. We suggest to use a very few event
types especially if you submit hundreds of jobs. For more info, see output of ``man sbatch`` command.


.. attention:: * Do not use mail event type *ALL,BEGIN*.
               * Do not enable email notification if you submit hundreds of jobs.
                 Sending an email for each job overloads Postfix server.
               * Make sure to use your actual UCI-issued email address. While Slurm sends emails to any email address,
                 system administrators will use UCInetID@uci.edu if they need to contact you about a job.

.. _job monitoring:

Monitoring
----------

.. _job status:

Status
^^^^^^

| ``squeue``
| ``scontrol show job``

To check the status of your job in the queue:
  .. code-block:: console

     [user@login-x:~]$ squeue -u panteater
        JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
     22877983  standard     test panteater R       0:03      1 hpc3-17-11

  .. attention:: | Avoid using command ``watch`` to query the Slurm queue in a continuous loop as in
                 | ``watch -d squeue <...some arguments...>``

  This frequent querying of Slurm queue  creates an unnecessary overhead
  and affects many users.  Instead, check your job output and use :ref:`mail notification` for the job end.

To get detailed info about the job:
  .. code-block:: console

     [user@login-x:~]$ scontrol show job 22877983

  The output will contain a list of *key=value* pairs that provide job information.

.. _job accounting:

Account balance
^^^^^^^^^^^^^^^

| ``sbank``
| ``zotledger``

In order to run jobs on HPC3, a user must have available CPU hours.

1. The ``sbank`` is short for `Slurm bank <https://jcftang.github.io/slurm-bank>`_
   It is used to display the balance of used and available hours to the user for a given account
   (defaults to the current user).

   Display the account balance for specific lab account and get info about next reallocation:
     .. code-block::
	 
        [user@login-x:~]$ sbank balance statement -a peter_lab
        Account             Usage | Account Limit Available (SUs)
        --------------- --------- + ------------- ---------------
        PETER_LAB           3,083 |         3,500             417
        ---------------------------------------------------------
        Next reallocation: 2025-07-17


   Display the account balance for specific user account:
     .. code-block::

        [user@login-x:~]$ sbank balance statement -a panteater
        User         Usage |     Account   Usage | Account Limit Available (CPU hrs)
        ---------- ------- + ----------- ------- + ------------- ---------
        panteater*      58 |   PANTEATER      58 |         1,000       942

   Display the account balances for specific user:
     .. code-block::

        [user@login-x:~]$ sbank balance statement -u panteater
        User        Usage |     Account    Usage | Account Limit Available (CPU hrs)
        ---------- ------ + ----------- -------- + ------------- ---------
        panteater*     58 |   PANTEATER       58 |         1,000       942
        panteater*  6,898 |      PI_LAB    6,898 |       100,000    93,102
        panteater*     84 | PANTEATER_LAB_GPU 84 |        33,000    32,916

   .. note:: An hour of a GPU requires at least 2 CPU cores.
            Hence, the minimum charge for a single GPU is (32 + 2) = 34 SUs/hour.


2. The ``zotledger`` is a cluster-specific tool to print a ledger of jobs based on specified arguments.
   To find all available arguments for this command use ``zotledger -h``.

   Default is to print jobs of the current user for the last 30 days:

     .. code-block:: console

        [user@login-x:~]$ zotledger -u panteater
              DATE       USER   ACCOUNT PARTITION   JOBID JOBNAME ARRAYLEN CPUS WALLHOURS  SUs
        2021-07-21  panteater panteater  standard 1740043    srun        -    1      0.00 0.00
        2021-07-21  panteater panteater  standard 1740054    bash        -    1      0.00 0.00
        2021-08-03  panteater    lab021  standard 1406123    srun        -    1      0.05 0.05
        2021-08-03  panteater    lab021  standard 1406130    srun        -    4      0.01 0.02
        2021-08-03  panteater    lab021  standard 1406131    srun        -    4      0.01 0.02
            TOTALS          -         -         -       -       -        -    -      0.07 0.09


.. _job efficiency:

Efficiency
^^^^^^^^^^

| ``sacct``
| ``seff``
| ``seff-array``
| ``sstat``

These are commands that provide info about resources consumed by the job.

:use for running jobs:
  ``sstat``

:use for completed jobs:
  ``sacct``,  ``seff``, ``seff-array``

All commands need to use a valid *jobid*.

1. The `sstat <https://slurm.schedmd.com/sstat.html>`_
   displays various running job and job steps resource utilization information.

   For example, to print out a job's average CPU time use (avecpu), average number of bytes written by all tasks
   (AveDiskWrite), average number of bytes read by all tasks (AveDiskRead),
   as well as the total number of tasks (ntasks) execute:

   .. code-block:: console

      [user@login-x:~]$ sstat -j 125610 --format=jobid,avecpu,aveDiskWrite,AveDiskRead,ntasks
             JobID     AveCPU AveDiskWrite  AveDiskRead   NTasks
      ------------ ---------- ------------ ------------ --------
      125610.batch 10-18:11:+ 139983973691 153840335902        1


2. The `sacct <https://slurm.schedmd.com/sacct.html>`_ command  can be used to see accounting
   data for all jobs and job steps and other useful info such how long job
   waited in the queue.

   Find accounting info about a specific job:

     .. code-block:: console

        [user@login-x:~]$ sacct -j 43223
               JobID  JobName  Partition      Account  AllocCPUS      State ExitCode
        ------------ -------- ---------- ------------ ---------- ---------- --------
           36811_374    array   standard panteater_l+          1  COMPLETED      0:0

     The command uses a default output format.

   Find detailed accounting info a job using specific format:
     .. code-block:: console

        [user@login-x:~]$ export SACCT_FORMAT="JobID,JobName,Partition,Elapsed,State,MaxRSS,AllocTRES%32"
        [user@login-x:~]$ sacct -j 600
        JobID      JobName  Partition  Elapsed     State  MaxRSS AllocTRES
        ---------- -------  --------  -------- --------- ------- --------------------------------
               600    all1  free-gpu  03:14:42 COMPLETED         billing=2,cpu=2,gres/gpu=1,mem=+
         600.batch   batch            03:14:42 COMPLETED 553856K           cpu=2,mem=6000M,node=1
        600.extern  extern            03:14:42 COMPLETED       0 billing=2,cpu=2,gres/gpu=1,mem=+


     * *MaxRSS*: shows your job memory usage.
     * *AllocTRES*: is trackable resources, these are the resources allocated to the job
       after the job started running. The :tt:`%32` is a format specification to
       reserve 32 characters for this option in the output. Format specification can
       be used for any option.
 
   Find how long your jobs were queued (column *Planned*) before they started running:
     .. code-block:: console

        [user@login-x:~]$ export SACCT_FORMAT='JobID%20,Submit,Start,Elapsed,Planned'
        [user@login-x:~]$ sacct -j 30054126,30072212,30072182 -X
               JobID              Submit               Start    Elapsed    Planned
        ------------ ------------------- ------------------- ---------- ----------
            30054126 2024-07-14T11:17:00 2024-07-14T17:03:08   00:22:09   05:46:08
            30072182 2024-07-14T20:29:30 2024-07-14T20:31:16   00:05:20   00:01:46
            30072212 2024-07-14T20:44:14 2024-07-14T20:44:26   00:05:58   00:00:12

   .. note:: Other useful options in SACCT_FORMAT are *User*, *NodeList*, *ExitCode*.
             To see all available options, run ``man sacct`` command.


3. The ``seff`` Slurm efficiency script is used to find useful information about the job
   including the memory and CPU use and efficiency.  Note, ``seff`` doesn't
   produce accurate results for multi-node jobs. Use this command for single node jobs.

     .. code-block:: console

        [user@login-x:~]$ seff -j 423438
        Job ID: 423438
        Cluster: hpc3
        User/Group: panteater/panteater
        State: COMPLETED (exit code 0)
        Nodes: 1
        Cores per node: 8
        CPU Utilized: 00:37:34
        CPU Efficiency: 12.21% of 05:07:36 core-walltime
        Job Wall-clock time: 00:38:27
        Memory Utilized: 2.90 MB
        Memory Efficiency: 0.01% of 24.00 GB

   Important info is on *CPU* and *Memory* lines.

   :CPU efficiency:
     at 12.21%  the job used only a small portion of requested 8 CPUs

   :Memory efficiency:
     at 0.011% the job used only a fraction of requested 24GB of memory
 
   The user should fix the job submit script and ask for less memory per CPU
   and for fewer CPUs.

4. The ``seff-array`` command is an extension of ``seff`` to use for array jobs.
   It provides CPU and memory efficiency and wall-clock time for the array
   tasks and calculates their *Min, Max, Mean* and *Standard Deviation*.

     .. code-block:: console

        [user@login-x:~]$ seff-array 123456
        Job information:
        -----------------------------
           ID: 123456
           Name: DataUpdater
           Cluster: hpc3
           User/Group: panteater/panteater
           Requested CPUs: 1 cores on 1 node(s)
           Requested Memory: 3G
           Requested Time: 12-00:00:00

        Job tasks status:
        -----------------------------
           CANCELLED by 63168: 1
           COMPLETED: 148

        Finished job tasks stats:
        -----------------------------
           Excluding pending/running/cancelled jobs tasks.
           StDev is calculated as 'population standard deviation'.

           --------------------------------------------------------------------------
           Measure                         Min          Max         Mean        StDev
           --------------------------------------------------------------------------
           CPU efficiency    (%)          0.67        24.20         1.18         1.91
           Memory efficiency (%)          0.14         0.64         0.61         0.04
           Wall-clock (d-hh:mm:ss)    00:01:27   2-04:06:32  1-013:12:16     10:06:39
           --------------------------------------------------------------------------


.. _job pending:

Pending
-------

Jobs submitted to Slurm will start up as soon as the scheduler can find an appropriate resource
depending on the availability of the nodes, job priority and job requests.

Lack of resources or insufficient account balance
(status reason is *AssocGrpCPUMinutesLimit* or *AssocGrpBillingMinutes*) are the most common
reasons that prevent a job from starting.

RCIC does not generally put limits in place unless we see excess,
unreasonable impact to shared resources (often, file systems), or other fairness issues.

.. important:: **The balance in the account must have enough core hours to cover the job request**.

               * This applies to all jobs submitted with ``sbatch`` or ``srun``.
               * This applies to all partitions, including free. While your job
                 will not be charged when submitted to a free partition, there must be a
                 sufficient balance for Slurm to begin your job.

When a job is in *PD* (pending) status you need to determine why.

.. _pending reasons:

Pending Job Reasons
^^^^^^^^^^^^^^^^^^^

While lack of resources or insufficient account balance are common reasons that prevent a job from starting,
there are other possibilities.  A job may be waiting for more than one reason.

To see all available job pending reasons and their definitions in the
Slurm `Job Reason Codes <https://slurm.schedmd.com/job_reason_codes.html>`_ guide
or see output of ``man squeue`` command in the *JOB REASON CODES* section.

How to find job pending reason:
  Run the ``squeue`` command (with your login account after :tt:`-u`):

  .. code-block:: console

     [user@login-x:~]$ squeue -t PD -u peat
     JOBID PARTITION NAME USER ACCOUNT ST TIME CPUS NODE NODELIST(REASON)
     92005 standard  watA peat   p_lab PD 0:00    1    1 (ReqNodeNotAvail,Reserved for maintenance)
     92008 standard  watA peat   p_lab PD 0:00    1    1 (ReqNodeNotAvail,Reserved for maintenance)
     92011 standard  watA peat   p_lab PD 0:00    1    1 (ReqNodeNotAvail,Reserved for maintenance)
     95475 free-gpu  7sMD peat   p_lab PD 0:00    2    1 (QOSMaxJobsPerUserLimit)
     95476 free-gpu  7sMD peat   p_lab PD 0:00    2    1 (QOSMaxJobsPerUserLimit)

Most common reasons for job pending state and their explanations:
  ================================================================ =================================================
  :ref:`AssocGrpCPUMinutesLimit <pending AssocGrpCPUMinutesLimit>` :ref:`JobArrayTaskLimit <pending arraytasklimit>`
  :ref:`AssocGrpBillingMinutes <pending AssocGrpBillingMinutes>`   :ref:`MaxGRESPerAccount <pending gres>`
  :ref:`Dependency <pending dependency>`                           :ref:`QOSMaxJobsPerUserLimit <pending qosmax>`
  :ref:`DependencyNeverSatisfied <pending dependency never>`       :ref:`ReqNodeNotAvail, Reserved for maintenance <pending reason maintenance>`
  :ref:`Priority <pending priority>`                               :ref:`Resources <pending reason resources>`
  ================================================================ =================================================

.. _pending AssocGrpCPUMinutesLimit:

:bluelight:`Pending job due to AssocGrpCPUMinutesLimit`
  Same as :ref:`AssocGrpBillingMinutes <pending AssocGrpBillingMinutes>`.

.. _pending AssocGrpBillingMinutes:

:bluelight:`Pending job due to AssocGrpBillingMinutes`
  This means insufficient funds are available to run the job to completion.

  Slurm calculates *MAX Time* a job might consume as Number :subscript:`cores` x Number :subscript:`hours`
  from the cores and hours requested for the job.
  If the calculated value is less than the available account balance it means
  there is not enough balance to run the job.

  Slurm will not  start a new job if left :underline:`MAX Time of current jobs`
  plus :underline:`MAX Time of queued jobs` would cause the account to go negative.

  .. note:: A user needs to check if there are any other jobs already running in the specified account
            and compute what is the time already requested and allocated by Slurm to all
            jobs on this account.

  **Job in personal account**
    Check your jobs status

       .. code-block:: console

          [user@login-x:~]$ squeue -u panteater
          JOBID  PARTITION  NAME     USER    ACCOUNT ST TIME NODES NODELIST(REASON)
           6961   standard  tst1 panteater panteater PD 0:00     1 (AssocGrpBillingMinutes)
           6962   standard  tst2 panteater panteater PD 0:00     1 (AssocGrpBillingMinutes)

       The reason :tt:`AssocGrpBillingMinutes` is given for
       the personal account where the job was submitted.

    Check your Slurm account balance

       .. code-block:: console

          [user@login-x:~]$ sbank balance statement -u panteater
          User        Usage |     Account   Usage | Account Limit Available (CPU hrs)
          ---------- ------ + ----------- ------- + ------------- ---------
          panteater*     58 |   PANTEATER      58 |         1,000       942
          panteater*  6,898 |      PI_LAB   6,898 |       100,000    93,102

       The account has `942`  hours.

    Check your job requirements

       You can use ``scontrol show job <jobid>`` or a command below

       .. code-block:: console

          [user@login-x:~]$ squeue -o "%i %u %j %C %T %L %R" -p standard -t PD -u panteater
          JOBID       USER NAME CPUS   STATE     TIME_LEFT  NODELIST(REASON)
          66961 panteater tst1  16  PENDING    3-00:00:00 (AssocGrpBillingMinutes)
          66962 panteater tst2  16  PENDING    3-00:00:00 (AssocGrpBillingMinutes)

       Each jobs asks for 16 CPUs to run for 3 days which is
       :math:`16 * 24 * 3 = 1152` core-hours, and it is more than `942` hours in the account balance.

    .. attention:: These two jobs will never be scheduled to run and need to be canceled

  **Job in LAB account**
    .. important:: A lab account has a combined single balance limit
                   for all members of the lab.

    Check your jobs status

       .. code-block:: console

          [user@login-x:~]$ squeue -u panteater -t PD
          JOBID     PARTITION     NAME      USER ACCOUNT ST  TIME CPUS NODE NODELIST(REASON)
          12341501  standard  myjob_98 panteater  PI_lab PD  0:00    1    1 (AssocGrpBillingMinutes)
          12341502  standard  myjob_99 panteater  PI_lab PD  0:00    1    1 (AssocGrpBillingMinutes)

    Check your Slurm lab account balance

       .. code-block:: console

          [user@login-x:~]$ sbank balance statement -a PI_LAB
          User         Usage |  Account   Usage | Account Limit Available (CPU hrs)
          ---------- ------- + ----------- -----+ ------------- ---------
          panteater1       0 |   PI_LAB  75,800 |       225,000   67,300
          panteater2  50,264 |   PI_LAB  75,800 |       225,000   67,300
          panteater*  25,301 |   PI_LAB  75,800 |       225,000   67,300

    Check your job requirements

       .. code-block:: console

          [user@login-x:~]$ scontrol show job 12341501
          JobI4=12341501 JobName=myjob_98
             UserId=panteater(1234567) GroupId=panteater(1234567) MCS_label=N/A
             Priority=299 Nice=0 Account=PI_lab QOS=normal
             JobState=PENDING Reason=AssocGrpBillingMinutes Dependency=(null)
             Requeue=0 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
             RunTime=00:00:00 TimeLimit=14-00:00:00 TimeMin=N/A
             SubmitTime=2023-01-18T16:36:06 EligibleTime=2023-01-18T16:36:06
             AccrueTime=2023-01-18T16:36:06
             StartTime=Unknown EndTime=Unknown Deadline=N/A
             NumNodes=1 NumCPUs=1 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
             TRES=cpu=1,mem=6G,node=1,billing=1
             <output  cut>

       There is a similar output is for the second job. Note the :tt:`TimeLimit`
       which is the time run requested for the job.
       For each of two pending jobs the resource request is:
       :math:`1 CPU * 14 days * 24 hrs = 336 hrs`

    Check ALL the running jobs for your lab account

       .. code-block:: console

          [user@login-x:~]$ squeue -t R -A PI_lab -o "%.10i %.9P %.8j %.8u %.16a %.2t %.6C %l %L"
             JOBID PARTITION     NAME     USER       ACCOUNT ST   CPUS  TIME_LIMIT TIME_LEFT
          12341046  standard myjob_39  panteater      PI_lab  R      1 14-00:00:00 13-23:00:22
          12341047  standard myjob_40  panteater      PI_lab  R      1 14-00:00:00 13-23:00:22
          12341048  standard myjob_41  panteater      PI_lab  R      1 14-00:00:00 13-23:00:22
          < total 200 running jobs >

       | Each of 200 running jobs in the account has run for about 1hr out of allocated 14 days.
         Total max time Slurm has allocated for these running jobs is
       | :math:`1 CPU * 200 jobs * 14 days * 24 hrs = 67200 hrs`

       | There are about *200 hrs* already used, (each job already run for ~1 hr), so remaining needed
         balance is :tt:`67100 hrs`.  Your 2 pending jobs require
       | :math:`1 CPU * 14 days * 24 hrs * 2 jobs = 672 hrs`.

       | Slurm is computing that if all current jobs ran to their MAX times and if the next job
         were to run MAX time your account would end up negative:
       | :math:`67300 - 67100 - 672 = -472 hrs`.

       Therefore Slurm puts these new jobs on hold.
       These 2 jobs will  start running once some of the remaining running jobs completed
       and the account balance is sufficient.

      .. important:: It is important to correctly estimate time needed for the job,
                     and not ask for more resources (time, cpu, memory) than needed.

.. _pending dependency:

:bluelight:`Pending job due to Dependency`
  Job has a user-defined dependency on a running job and cannot start until
  this running job has completed.

.. _pending dependency never:

:bluelight:`Pending due to DependencyNeverSatisfied`
  Job has a user-defined dependency that failed. Job will never run and needs to be canceled.

.. _pending arraytasklimit:

:bluelight:`Pending due to JobArrayTaskLimit`
  The user has reached job array's limit on the number of simultaneously running tasks.

.. _pending priority:

:bluelight:`Pending due to Priority`
  Slurm scheduler is temporarily holding the job in pending state because other queued jobs have a higher priority.

.. _pending gres:

:bluelight:`Pending due to MaxGRESPerAccount`
   The job's GRES request exceeds the per-Account limit.
   We have limits how many GPUs can be allocated to a single user.

.. _pending qosmax:

:bluelight:`Pending due to QOSMaxJobsPerUserLimit`
  The user is already running the maximum number of jobs allowed by the particular partition.

.. _pending reason maintenance:

:bluelight:`Pending job due to ReqNodeNotAvail, Reserved for maintenance`
  This means if your job is started now it will not complete by the time the
  scheduled maintenance starts. Slurm is holding your job because no jobs can run during the maintenance period.
  You either have to wait or you need to change your job requirements.
  See :ref:`fix pending jobs <fix pending job>`.
  Job will not start until maintenance has been completed.

.. _pending reason resources:

:bluelight:`Pending job due to Resources`
  This means the requested resource configuration is not currently available. If a job requests a
  resource combination that physically does not exist, the job will remain in this state forever.

.. _fix pending job:

Fix Pending Job
^^^^^^^^^^^^^^^

  Fixes apply for batch jobs submitted with ``sbatch`` or for interactive
  jobs submitted with ``srun``.

  :bluelight:`Cancel the job`
    For many of the job pending reasons the first step is to cancel your job:

    .. code-block:: console

       [user@login-x:~]$ scancel <jobid>

  **Fix pending job due to**

  :bluelight:`AssocGrpBillingMinuteso or AssocGrpCPUMinutesLimit`
    First, cancel existing pending job (it will never run).
    Next, resubmit the job so that the requested execution hours can be covered by your bank account balance.
    Check and update the following in your submit script:

     * If your job was run from personal account

       :tt:`SBATCH -A` - use a different Slurm account (lab) where you have enough balance

     * Lower requirements of your job so that requested resources will be no more than core hours available in
       your account. This may mean to use:

       :tt:`SBATCH --ntasks` or :tt:`#SBATCH --cpus-per-task` - fewer CPUs

       :tt:`SBATCH --ntasks` and :tt:`#SBATCH --mem-per-cpu` - fewer CPUs, increase memory per CPU

       :tt:`SBATCH --mem` or :tt:`#SBATCH --mem-per-cpu` - less memory

       :tt:`SBATCH --time` - set a time limit shorter than the default runtime

  :bluelight:`ReqNodeNotAvail, Reserved for maintenance`
    You need to cancel your job and re-submit it job with a shorter time limit
    that will end BEFORE the maintenance begins.

    If you did not specify time limit, the default time setting is in effect.
    Please see :ref:`available partitions` for partitions default and max settings
    and :ref:`job examples` for additional info.

    To find out the reservation details use:

    .. code-block:: console

       [user@login-x:~]$ scontrol show reservation
        ReservationName=RCIC: HPC3 scheduled maintenance StartTime=2024-03-27T08:00:00 EndTime=2024-03-28T08:00:00 Duration=1-00:00:00
        Nodes=hpc3-14-[00-31],... NodeCnt=228 CoreCnt=9936 Features=(null) PartitionName=(null) Flags=MAINT,IGNORE_JOBS,SPEC_NODES,ALL_NODES
        TRES=cpu=9936
        Users=root,... Groups=(null) Accounts=(null) Licenses=(null) State=INACTIVE BurstBuffer=(null) Watts=n/a
        MaxStartDelay=(null)

    The first output line includes the maintenance start time, end time and duration.

    Based on the info about the reservation time and the current day/time you can
    estimate what time limit :tt:`SBATCH --time` should be specified for your job in order for
    it to finish :red:`before the maintenance starts`.

    If your job truly needs requested time limit, nothing can be done until the maintenance is over.
    Cancel your job and resubmit after the maintenance.

  :bluelight:`Resources`
    Check Slurm estimate for the job start time:

    .. code-block:: console

       [user@login-x:~]$ squeue --start -j 32511
       JOBID PARTITION NAME     USER ST          START_TIME NODES SCHEDNODES NODELIST(REASON)
       32511     free  GEN panteater PD 2024-08-15T13:36:57     1 hpc3-14-00 (Resources)

    | The estimated time start is listed under *START_TIME*.
    | You either have to wait or you need to cancel your job, change its requirements and resubmit.


  :bluelight:`JobArrayTaskLimit`
     You need to wait till some already running tasks complete. Scheduler will
     automatically start the next task.

  :bluelight:`MaxGRESPerAccount`
     You need to wait till some of your already running jobs requesting GPUs complete.
     There is a limit how many GPUs can be used by a single user or a single GPU account.

  :bluelight:`Dependency`
     You need to wait till the job dependency on another already running job is fulfilled.

  :bluelight:`DependencyNeverSatisfied`
     You need to cancel your job because its dependency job was canceled or
     failed. This job will never run and only takes scheduler resources.

  :bluelight:`QOSMaxJobsPerUserLimit`
     You need to wait till some of your already running jobs in this partition complete.

  :bluelight:`Priority`
     The scheduler will automatically start your job when the higher priorities
     jobs are run and the resources become available.

.. _modify job:

Modification
------------

``scontrol``

This command can be used to make some changes to jobs that are still waiting to run.

If changes need to be made for a running job, it may be better to kill the job
and restart it after making the necessary changes.

Change QOS:
  By default, jobs are set to run with :tt:`qos=normal`.
  :underline:`Users rarely need to change QOS`.

  .. code-block:: console

     [user@login-x:~]$ scontrol update jobid=<jobid> qos=[low|normal|high]

Change job time limit:
  Only the Slurm administrator can increase job's time limit.
  If your job is already running and you have established that it will not
  finish by its current time limit you can submit a ticket indicating:

    - your JOBID
    - your desired time extension

  Note, we need to receive your request before your job's current end time
  and your bank account must have sufficient funds to cover the desired time
  extension.

.. _control jobs:

Cancel/Hold/Release
-------------------

| ``scancel``
| ``scontrol``

The following commands can be used to:

Cancel a specific job:
  .. code-block:: console

     [user@login-x:~]$ scancel <jobid>

Cancel all jobs owned by a user:
  This only applies to jobs that are associated with your accounts

  .. code-block:: console

     [user@login-x:~]$ scancel -u <username>

Prevent a pending job from starting:
  .. code-block:: console

     [user@login-x:~]$ scontrol hold <jobid>

Release held jobs to run:
  .. code-block:: console

     [user@login-x:~]$ scontrol release <jobid>
