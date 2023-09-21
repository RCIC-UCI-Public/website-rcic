.. _jobs:

Jobs
=====

Charging jobs to an account is new for the UCI community. Like any policy, it can be two-edged. 

* A large fraction of users should be able to run :ref:`allocated jobs` and never see the limits of their accounts.
* Users who are running a very large number of :ref:`free jobs` are likely to have some of
  their free jobs preempted (killed).

In this section, we provide information about how to submit your jobs to Slurm, how
to monitor them and how to request various resources.

Additional specific :ref:`job examples` show in depth how to run array jobs, request GPUs,
CPUs, and memory for a variety of different job types and common applications.

.. contents::
   :local:

.. _recommendation:

General Recommendations
-----------------------

**Get the most from your allocation:**

  * Look at your past jobs and see how many CPU and memory resource were used. Don't request more than needed.
  * Prioritize your own work. Test and low-priority jobs can be free jobs.  Others should be allocated.
  * Understand that free *comes with no guarantees*.  Your free job can be killed at anytime.

**Quota Enforcement**

  When users exceed their disk space or CPUs quota allocations the following will happen:

  * users will not be able to submit new jobs
  * running jobs will fail

  .. important:: Please check the available disk space and CPU hours in your Slurm account regularly.
     Delete or archive data as needed.

**Inherited environment**

  Any method of the job submission to SLURM (batch, immediate, interactive) will inherit all environment
  variables that were set in your login shell (on the login node where you are executing job submission). 

  * Make sure that there are no environment variables in
    the login shell that can cause problems in the batch script or in ``srun`` command.

    By default there are none, unless one changes the environment via
    setting environment variables either on command line or in :tt:`$HOMEbashrc` file
    or is using conda.

    This is why one needs to load modules either in the SLURM submit script
    or on an interactive node once you execute the `srun` command and not in the
    login shell before the job submission.

  * If you are using conda please review :ref:`install conda` 
    guide that explains how to cleanly separate conda-set environment from your
    login environment.

Details of jobs subscriptions, requesting resources, etc are descbided in
detail in the sections below.


.. _batch job:

Batch Job
---------

``sbatch submit-script.sub``

A batch job is run at sometime in the future by the scheduler.
Submitting batch jobs to Slurm is done with the ``sbatch`` command
and the job description is provided by the submit script.
An example job submit script:

.. centered:: File simple.sub

.. literalinclude:: files/simple.sub
   :language: bash

To submit a job on HPC3, login and using your favorite editor create
:tt:`simple.sub` file with the contents shown above.

Edit the Slurm account to charge for the job to either your personal account or lab account.
Your personal account is the same as your UCINetID.

To submit the job:
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

The command ``srun`` is used to run an interactive job immediately and uses your console
for for standard input/output/error instead of redirecting them to files.

.. important:: | ``srun`` submits jobs for execution but it does not bypass scheduler priority.
               | If your job cannot run immediately, you will wait until Slurm can schedule your request.

The main difference between ``srun`` and ``sbatch``:

.. table::
   :class: noscroll-table

   +--------------------------------------------------+-----------------------------------------+
   | Srun                                             | Sbatch                                  |
   +==================================================+=========================================+
   | Interactive and blocking                         | Batch processing and non-blocking       |
   +--------------------------------------------------+-----------------------------------------+
   | Can be used to create job steps in submit scripts| Can do everything ``srun`` can and more.|
   +--------------------------------------------------+-----------------------------------------+

Examples of interactive jobs:
  .. code-block:: console

     [user@login-x:~]$ srun -A PI_LAB --pty /bin/bash -i                     # 1
     [user@login-x:~]$ srun -p free --pty /bin/bash -i                       # 2
     [user@login-x:~]$ srun --mem=8G -p free --pty /bin/bash -i              # 3
     [user@login-x:~]$ srun -c 4 --time=10:00:00 -N 1 --pty /bin/bash -i     # 4
     [user@login-x:~]$ srun -p free-gpu --gres=gpu:V100:1 --pty /bin/bash -i # 5
     [user@login-x:~]$ srun -p free --x11  --pty /bin/bash -i*               # 6

  1. use *standard* partition and charge to the *PI_LAB* account
  2. use *free* partition (where it may be killed at any time)
  3. use *free* partition and ask for 8Gb of memory per job (ONLY when you truly need it)
  4. use *standard* partition and ask for 4 CPUs for 10 hrs
  5. use *free-gpu* partition and ask for one GPU. :red:`DO NOT ask for more than 1 GPU!`
  6. start an interactive session for GUI jobs. 

     First, a user must login with ssh Xforwarding enabled see :ref:`ssh xforward` guide
     and then use the :tt:`--x11` in ``srun`` command to enable Xforwarding.

Note, these options :tt:`--pty /bin/bash -i` must be the last on a command line
and should not be separated by other options.

Once the ``srun`` command is executed, the scheduler allocates
available resource and starts an interactive shell on the available node.
Your shell prompt will indicate a new *hostname*.

Once done with your work simply type at the prompt:

.. code-block:: console

   [user@hpc3-x-y:~]$ exit

.. _attach to job:

Attach to a job
---------------

``srun --pty --jobid``

.. attention:: The ssh access to compute nodes is turned off

Users will need to use Slurm commands to find a job ID and to attach to
*running jobs* if they want to run simple jobs verification commands on the node where their job is running.

Once attached o a job, the user will be put on the node where the job is
running (first listed if running on multi-node) and will 
**run inside the cgroup (CPU, RAM etc.) of the running job**. This means the user:

  * will be able to execute simple commands such as :tt:`ls, top, ps`, etc.
  * :red:`will not be able to start new processes` that use resources outside of what is specified in
    *jobid*. Any command will use computing resources, and will add to the usage of the job.
  * needs to type ``exit`` after executing desired verification commands in order to
    stop attachment from the job.  The original job will be still running.

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

     [user@hpc3-14-02:~]$ ls /tmp/panteater/
     [user@hpc3-14-02:~]$ exit
     [user@login-x:~]$


Attach to a specific node using :tt:`-w` switch (for multi-node jobs):
  .. code-block:: console

     [user@login-x:~]$ srun --pty --jobid 3559124 --overlap -w hpc3-15-08 /bin/bash
     [user@hpc3-15-08:~]$ 

Most often users just need to see the processes of the job, etc. Such commands
can be run directly.  

Run ``top`` command while attaching to the running job: 
  .. code-block:: console

     [user@login-x:~]$ srun --pty --overlap --jobid $JOBID top

.. _request resources:

Requesting Resources
--------------------

.. _request constrains:

Features/Constraints
^^^^^^^^^^^^^^^^^^^^

HPC3 has a heterogeneous hardware with several different CPU types.
You can request that a job only runs on nodes with certain *features*.

The *features* can be requested via a use of constraints.
To request a feature/constraint, you must add to your submit script:

.. code-block:: bash

   #SBATCH --constraint=<feature_name>

where :tt:`<feature_name>` is one of the defined features (or one of the standard features described 
in the `Slurm sbatch <https://slurm.schedmd.com/sbatch.html>`_ guide).

We defined the following features for node selection:

.. _defined constrains:

.. table:: HPC3 Defined Features
   :widths: 20 45 20 15
   :class: noscroll-table

   +---------------------+---------------------------------------+---------------+--------------+
   | Feature             | Node Description                      | Node          | Cores        |
   |                     |                                       |               |              |
   | name                | (processor/storage)                   | count         | min/mod/max  |
   +=====================+=======================================+===============+==============+
   | intel               | any Intel node including HPC legacy   | compute: 171  | 24 / 40 / 48 |
   |                     |                                       |               |              |
   |                     |                                       | GPU: 32       | 32 / 40 / 40 |
   +---------------------+---------------------------------------+---------------+--------------+
   | avx512              | Intel AVX512                          | compute: 166  | 28 / 40 / 48 |
   |                     |                                       |               |              |
   |                     |                                       | GPU: 32       | 32 / 40 / 40 |
   +---------------------+---------------------------------------+---------------+--------------+
   | epyc or amd         | any AMD EPYC                          | 19            | 40 / 64 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | epyc7551            | AMD EPYC 7551                         | 3             | 40 / 64 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | epyc7601            | AMD EPYC 7601                         | 16            | 64 / 64 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | nvme or fastscratch | Intel AVX512 with /tmp on NVMe disk   | 66            | 32 / 48 / 48 |
   +---------------------+---------------------------------------+---------------+--------------+
   | mlx5_ib             | Updated Infiniband firmware           | 131           | 36 / 40 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+
   | mlx4_ib             | Older Infiniband firmware             | 6             | 24 / 40 / 64 |
   +---------------------+---------------------------------------+---------------+--------------+

To request nodes with updated Infiniband firmware for your MPI-based jobs:

  .. code-block:: bash

    #SBATCH --constraint=mlx5_ib

To request nodes with a large local scratch storage:

  .. code-block:: bash

    #SBATCH --constraint=nvme
    or
    #SBATCH --constraint=fastscratch

  See :ref:`scratch storage` for details.

To request nodes with CPUS capable of AVX512 instructions:

  .. code-block:: bash

    #SBATCH --constraint=avx512

.. _scratch storage:

Scratch storage
^^^^^^^^^^^^^^^

Scratch storage is local to each compute node and is the fastest disk access
for reading and writing the input/output job files.

Scratch storage is created for each job automatically as :tt:`/tmp/ucinetid/jobid/`
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

  will have the following directories created by Slurm for the job on :tt:`hpc3-15-08`

  .. code-block:: console

     /tmp/panteater/20960254
     /tmp/panteater/20889321

  .. note:: While the directory is created automatically, it is A USER RESPONSIBILITY to
            copy files to this location and copy the final results back before the job ends. 

Slurm doesn't have any default amount of scratch space defined per job and that may be fine for most, but not all.
The problem of having enough local scratch arises when nodes are shared by multiple jobs and users.
:red:`One job can cause the other jobs running on the same node to fail`, so please be considerate of your
colleagues by doing the following.

1. **Your job creates just under a few Gb of temporary data directly in $TMPDIR**
   and handles the automatic creation and deletion of these temp files.
   Many Python, Perl, R, Java programs and 3rd party commercial software will
   write to :tt:`$TMPDIR` which is the default for many applications.

   You don't need to do anything special. Do not reset :tt:`$TMPDIR`.

2. **Your job creates just under a few Gb of output in the directory where you
   run the job and does many frequent small file reads and writes** (a few Kb every few minutes).  

   You will need to use a scratch storage where you bring your job data, write temp files 
   and then copy the final output files back when the job is done.

   The reason is :red:`parallel filesystem (CRSP or DFS) is not suitable for small
   writes and reads` and such operations need to be off-loaded to the local
   scratch area on the node where the job is executed. 
   Otherwise you create an I/O problem not just for yourself but for many others 
   who use the same filesystem.

   The following partial submit script shows how to use :tt:`$TMPDIR` for such jobs:

   .. code-block:: bash

      <the rest of submit script is ommitted>

      #SBATCH --tmp=20G                 # requesting 20 GB (1 GB = 1,024 MB) local scratch

      # explicitly copy input files from DFS/CRSP to $TMPDIR
      # note, $TMPDIR already exists for your job
      cd $TMPDIR
      cp /pub/myacount/path/to/my/jobs/data/*dbfiles  $TMPDIR

      # create a directory for the application output
      mkdir -p $TMPDIR/output

      # your job commands are here
      # output from application goes to $TMPDIR/output/
      mapp -tf 45 -o $TMPDIR/output     # program output directory is specified via -o flag 
      mapp2  > $TMPDIR/output/mapp.out  # program output in a specific file

      # explicitly copy output files from $TMPDIR to DFS/CRSP
      mv $TMPDIR/output/* /pub/myaccount/myrun134/

   In this scenario, Slurm job is run in :tt:`$TMPDIR` which is much faster
   for the disk I/O, then the program output is copied back as a big write 
   which is much more efficient compare to many small writes.

3. **Your job creates many Gbs of temporary data (order of ~100Gb)**

   You will need to submit your job to a node with a lot of local scratch storage
   where you bring your job data, write temp files,
   and then copy the final output files back when the job is done.

   In your submit script define how much scratch space your job needs
   (you may need to figure it out by trial test  run)
   and request the nodes that have fast local scratch area via the following SLURM directives:

   .. code-block:: bash


      #SBATCH --tmp=180G                 # requesting 180 GB (1 GB = 1,024 MB) local scratch
      #SBATCH --constraint=fastscratch   # requesting nodes with a lot of space in /tmp

   Folow the above (job type 2 above) submit script example to:

   | - at job start explicitly copy input files from DFS/CRSP to :tt:`$TMPDIR`
   | - at job end explicitly copy output files from :tt:`$TMPDIR` to DFS/CRSP

.. _request memory:

Memory
^^^^^^

There are nodes with different memory footprints. Slurm uses Linux
`cgroups <https://man7.org/linux/man-pages/man7/cgroups.7.html>`_ 
to enforce that applications do not use more memory/cores than they have been allocated.

Slurm has :tt:`default` and :tt:`*max` settings for a memory allocation per core
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
   the defaults. With slightly smaller memory footprints, the scheduler has MORE choices as to 
   where to place jobs on the cluster.

.. note:: For information how to get an  access to higher memory partitions please see :ref:`memory partitions`

When a job requires more memory:
  the memory needs to be specified 
  using one of the two mutually exclusive directives (one or another but not both):

  |   :tt:`--mem-per-cpu=X<specification>` - memory per core 
  |   :tt:`--mem=X<specification>` total memory  per job

  where :tt:`X` is an integer and :tt:`<specification>` of an optional size
  specification (M - megabytes, G - gigabytes, T - terabytes). A default is in megabytes. 

  The same directives formats are used in slurm submit scripts and in ``srun`` command
  for jobs in any partition.


If you want more memory for the job you should:
  | Scenario 1:
  |   - ask for more total memory
  | Scenario 2: 
  |   - ask for max memory per core and if this is not enough
  |   - request more cores. 

  You will be charged more for
  more cores, but you use a larger fraction of the node.

**Examples of memory requests**:

  1. Ask for the total job memory in submit script

       .. code-block:: bash

          #SBATCH --mem=500           # requesting 500MB memory for the job
          #SBATCH --mem=4G            # requesting 4GB (1GB = 1,024MB) for the job

  2. Ask for the memory per CPU in submit script

       .. code-block:: bash
     
          #SBATCH --mem-per-cpu=5000  # requesting 5000MB memory per CPU
          #SBATCH --mem-per-cpu=2G    # requesting 2GB memory per CPU

  3.Ask for 180 Gb for job in standard partition:

       .. code-block:: bash
     
          #SBATCH --partition=standard 
          #SBATCH --mem-per-cpu=6G    # requesting max memory per CPU
          #SBATCH --ntasks=30         # requesting 30 CPUS

     Ask for max memory per CPU and a number of CPUS to make up needed 
     total memory for job as *30 x 6Gb = 180Gb*

  4. Use ``srun`` and request 2 CPUs with a default or max memory

     .. code-block:: console
     
        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=2 --pty /bin/bash -i
        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=2 --mem-per-cpu=18G --pty /bin/bash -i
        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=2 --mem=36G --pty /bin/bash -i
     
     | The first job will have a total memory *2 x 3Gb = 6Gb* 
     | The second and third job each will have a total memory *2 x 18Gb = 36Gb*
     
  5. Use ``srun`` and request 4 CPUs and 10Gb memory per CPU,
  
     .. code-block:: console
     
        [user@login-x:~]$ srun -p free --nodes=1 --ntasks=4 --mem-per-cpu=10G --pty /bin/bash -i
     
     total memory for job is *4 x 10Gb = 40Gb*

.. note:: All above examples are asking for 1 node. This is important to let SLURM
   know that all your processes should be on a single node and not spread over
   multiple nodes. Very few applications that are compiled and run with OpenMPI or
   MPICH can use multiple nodes, the rest of applications  including interactive
   sessions should use a single node.

.. _request time:

Request Time
^^^^^^^^^^^^

Similar to memory limits, Slurm has *default* and *max* settings for a runtime
for each partition.  Please see all partitions settings in :ref:`available partitions`.

:default settings:
  are used when a job submission script does not specify
  different runtime, and for most jobs this is sufficient.

:max settings:
  specify the longest time a job can run in a given partition.
  Job time specifications can not exceed the partition's max setting.
  When a job requires longer runtime than a default it needs to be specified in the Slurm
  script using :tt:`#SBATCH --time=` (or  short notation :tt:`#SBATCH -t`) directive.

Acceptable time formats are 

  * minutes 
  * minutes:seconds
  * hours:minutes:seconds
  * days-hours
  * days-hours:minutes
  * days-hours:minutes:seconds

For example:

.. code-block:: bash

   #SBATCH --time=5        # 5 minutes
   #SBATCH -t 36:30:00     # 36 hrs and 30 min
   #SBATCH -t 7-00:00:00   # 7 days

.. _mail notification:

Mail notification
^^^^^^^^^^^^^^^^^

To receive email notification on the status of jobs, include the following lines in your
submit scripts and make the appropriate modifications to the second line:

.. code-block:: console

   #SBATCH --mail-type=fail,end
   #SBATCH --mail-user=user@domain.com

The first line specifies the event type for which a user requests an email (here failure/end events), the
second specifies a valid email address. We suggest to use a very few event
types especially if you submit hundreds of jobs. For more info, see output of ``man sbatch`` command.

Make sure to use your actual UCI-issued email address. While Slurm sends emails to any email address,
we prefer you use your UCInetID@uci.edu email address. System administrators will use UCInetID@uci.edu
if they need to contact you about a job.

.. attention:: | DO NOT use mail event type ALL, BEGIN.
               | DO NOT enable email notification if you submit hundreds of jobs.
               | Sending an email for each job overloads Postfix server.

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

  .. attention:: :red:`AVOID using command` ``watch`` :red:`to query the Slurm queue in a continuous loop 
                 as in this command:`  ``watch -d squeue <...some arguments...>``

  This frequent querying of Slurm queue  creates an unnecessary overhead
  and affects many users. 

  Instead, check your job output and use :ref:`mail notification` for the job end.

To get detailed info about the job:
  .. code-block:: console

     [user@login-x:~]$ scontrol show job 22877983

  The output will contain a list of *key=value* pairs that provide job information.

.. _job accounting:

Account balance
^^^^^^^^^^^^^^^

| ``sbank``
| ``/pub/hpc3/zotledger``

In order to run jobs on HPC3, a user must have available CPU hours.

1. The `sbank <https://jcftang.github.io/slurm-bank>`_  is short for *Slurm Bank*.
   It is used to display the balance of used and available hours to the user for a given account
   (defaults to the current user).

   Display the account balance for specific account:
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



2. We have a cluster-specific tool to print a ledger of jobs based on specified arguments.

   Default is to print jobs of the current user for the last 30 days:
     .. code-block:: console

        [user@login-x:~]$ /pub/hpc3/zotledger -u panteater
              DATE       USER   ACCOUNT PARTITION   JOBID JOBNAME ARRAYLEN CPUS WALLHOURS  SUs
        2021-07-21  panteater panteater  standard 1740043    srun        -    1      0.00 0.00
        2021-07-21  panteater panteater  standard 1740054    bash        -    1      0.00 0.00
        2021-08-03  panteater    lab021  standard 1406123    srun        -    1      0.05 0.05
        2021-08-03  panteater    lab021  standard 1406130    srun        -    4      0.01 0.02
        2021-08-03  panteater    lab021  standard 1406131    srun        -    4      0.01 0.02
            TOTALS          -         -         -       -       -        -    -      0.07 0.09

   To find all available arguments for this command use:
     .. code-block:: console

        [user@login-x:~]$ /pub/hpc3/zotledger -h

.. _job efficiency:

Efficiency
^^^^^^^^^^

There are a few commands that provide info about resources consumed by the job.

:This command is used for running jobs:
  ``sstat``

:These two commands can be used after the job completes:
  | ``sacct``
  | ``seff``

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
   data for all jobs and job steps.

   Find accounting info about a specific job:
     .. code-block:: console

        [user@login-x:~]$ sacct -j 43223
               JobID  JobName  Partition      Account  AllocCPUS      State ExitCode
        ------------ -------- ---------- ------------ ---------- ---------- --------
           36811_374    array   standard panteater_l+          1  COMPLETED      0:0

   The command uses a default output format. A more useful example will set
   a specific format that provides extra information.

   Find detailed accounting info a job using specific format:
     .. code-block:: console
   
        [user@login-x:~]$ export SACCT_FORMAT="JobID,JobName,Partition,Elapsed,State,MaxRSS,AllocTRES%32"
        [user@login-x:~]$ sacct -j 600
        JobID      JobName  Partition  Elapsed     State  MaxRSS AllocTRES
        ---------- -------  --------  -------- --------- ------- --------------------------------
               600    all1  free-gpu  03:14:42 COMPLETED         billing=2,cpu=2,gres/gpu=1,mem=+
         600.batch   batch            03:14:42 COMPLETED 553856K           cpu=2,mem=6000M,node=1
        600.extern  extern            03:14:42 COMPLETED       0 billing=2,cpu=2,gres/gpu=1,mem=+
   

     :MaxRSS:
       shows your job memory usage.

     :AllocTRES:
       is trackable resources, these are the resources allocated to the job
       after the job started running. The :tt:`%32` is simply a format specification to
       reserve 32 characters for this option in the output. Format specification can
       be used for any option.
    
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
     at 0.011% the job used only a fraction of requested 24Gb of memory
    
   The user should fix the job submit script and ask for less memory per CPU
   and for fewer CPUs.

.. _job pending:

Pending
-------

Jobs submitted to Slurm will start up as soon as the scheduler can find an appropriate resource
depending on the availability of the nodes, job priority and job resources.

Lack of resources or insufficient account balance 
(status reason is *AssocGrpCPUMinutesLimit*) are the most common
reasons that prevent a job from starting.

RCIC does not generally put limits in place unless we see excess,
unreasonable impact to shared resources (often, file systems), or other fairness issues.

When a job is in *PD* (pending) status you need to determine why.

.. important:: The balance in the account must have enough core hours to cover the job request. 

               This applies to ALL partitions, including free. While your job
               will not be charged when submitted to a free partition, there must be a
               sufficient balance for Slurm to begin your job.

.. _pending reasons:

Pending Job Reasons
^^^^^^^^^^^^^^^^^^^

While lack of resources or insufficient account balance are common reasons that prevent a job from starting,
there are other possibilities. 

To see the state reasons of your pending jobs, you can run the ``squeue`` command
with your account name as: 

.. code-block:: console

   [user@login-x:~]$ squeue -t PD -u peat
   JOBID PARTITION NAME USER ACCOUNT ST TIME CPUS NODE NODELIST(REASON)
   92005 standard  watA peat   p_lab PD 0:00    1    1 (ReqNodeNotAvail,Reserved for maintenance)
   92008 standard  watA peat   p_lab PD 0:00    1    1 (ReqNodeNotAvail,Reserved for maintenance)
   92011 standard  watA peat   p_lab PD 0:00    1    1 (ReqNodeNotAvail,Reserved for maintenance)
   95475 free-gpu  7sMD peat   p_lab PD 0:00    2    1 (QOSMaxJobsPerUserLimit)
   95476 free-gpu  7sMD peat   p_lab PD 0:00    2    1 (QOSMaxJobsPerUserLimit)

Reasons that are often seen on HPC3 for job pending state
and their explanation are summarized below.

AssocGrpCPUMinutesLimit:
  Insufficient funds are available to run the job to completion.
  Slurm users MAX time a job might consume which is
  calculated as :tt:`Number of cores x Number of hours`
  requested for the job, and internally marks those hours as unavailable.
Dependency:
  Job has a user-defined dependency on a running job and cannot start until the previous job has completed.
DependencyNeverSatisfied:
  Job has a user-defined dependency that failed. Job will never run and needs to be canceled.
Priority:
  Slurm's scheduler is temporarily holding the job in pending state because other queued jobs have a higher priority.
QOSMaxJobsPerUserLimit:
  The user is already running the maximum number of jobs allowed by the particular partition.
ReqNodeNotAvail, Reserved for maintenance:
  If the job were to run for the requested maximum time, it would run into
  a defined maintenance window. Job will not start until maintenance has been completed.
Resources: 
  The requested resource configuration is not currently available. If a job requests a
  resource combination that physically does not exist, the job will remain in this state forever.

To see all available job pending reasons and their definitions, please see output of
``man squeue`` command in the *JOB REASON CODES* section.
A job may be waiting for more than one reason.

.. _pending in personal account:

Pending job in personal account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Check your jobs status:

   .. code-block:: console

      [user@login-x:~]$ squeue -u panteater
      JOBID   PARTITION  NAME     USER    ACCOUNT ST TIME NODES NODELIST(REASON)
      1666961  standard  tst1 panteater panteater PD 0:00     1 (AssocGrpCPUMinutesLimit)
      1666962  standard  tst2 panteater panteater PD 0:00     1 (AssocGrpCPUMinutesLimit)

   Note, the reason is :tt:`AssocGrpCPUMinutesLimit` which means there is not enough
   balance left in the account. The job was submitted to use a personal account.

2. Check your Slurm account balance

   .. code-block:: console

      [user@login-x:~]$ sbank balance statement -u panteater
      User        Usage |     Account   Usage | Account Limit Available (CPU hrs)
      ---------- ------ + ----------- ------- + ------------- ---------
      panteater*     58 |   PANTEATER      58 |         1,000       942
      panteater*  6,898 |      PI_LAB   6,898 |       100,000    93,102

   The account has :tt:`942`  hours.

3. Check your job requirements

   You can use ``scontrol show job <jobid>`` or a command below

   .. code-block:: console

      [user@login-x:~]$ squeue -o "%i %u %j %C %T %L %R" -p standard -t PD -u panteater
      JOBID        USER NAME CPUS   STATE     TIME_LEFT  NODELIST(REASON)
      1666961 panteater tst1  16  PENDING    3-00:00:00 (AssocGrpCPUMinutesLimit)
      1666962 panteater tst2  16  PENDING    3-00:00:00 (AssocGrpCPUMinutesLimit)

   Each jobs asks for 16 CPUs to run for 3 days which is

   :math:`16 * 24 * 3 = 1152` core-hours, and it is more than 942 hours in the account balance.

   .. attention:: These jobs will never be scheduled to run and need to be canceled

.. _pending in lab account:

Pending job in LAB account
^^^^^^^^^^^^^^^^^^^^^^^^^^

Often users submit a job to a lab account and it results in PD status due to
:tt:`AssocGrpCPUMinutesLimit` reason. 

.. important::  A lab account has a combined single  balance and thus a single limit 
                for all members of the lab.

                Slurm will not  start a new job if :underline:`max time left of current jobs`
                plus :underline:`max time of queued jobs`
                would cause the account to go negative.

.. note:: A user needs to check if there are any other jobs already running in the specified account
          and compute what is the time already requested and allocated by Slurm to all
          jobs on the LAB account.

1. Check your jobs status

   .. code-block:: console

      [user@login-x:~]$ squeue -u panteater -t PD
      JOBID     PARTITION     NAME      USER ACCOUNT ST  TIME CPUS NODE NODELIST(REASON)
      12341501  standard  myjob_98 panteater  PI_lab PD  0:00    1    1 (AssocMaxJobsLimit)
      12341502  standard  myjob_99 panteater  PI_lab PD  0:00    1    1 (AssocMaxJobsLimit)

2. Check the Slurm lab account balance

   .. code-block:: console

      [user@login-x:~]$ sbank balance statement -a PI_LAB
      User         Usage |  Account   Usage | Account Limit Available (CPU hrs)
      ---------- ------- + ----------- -----+ ------------- ---------
      panteater1       0 |   PI_LAB  75,800 |       225,000   67,300
      panteater2  50,264 |   PI_LAB  75,800 |       225,000   67,300
      panteater*  25,301 |   PI_LAB  75,800 |       225,000   67,300

3. Check your job requirements

   .. code-block:: console

      [user@login-x:~]$ scontrol show job 12341501
      JobI4=12341501 JobName=myjob_98
         UserId=panteater(1234567) GroupId=panteater(1234567) MCS_label=N/A
         Priority=299 Nice=0 Account=PI_lab QOS=normal
         JobState=PENDING Reason=AssocMaxJobsLimit Dependency=(null)
         Requeue=0 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
         RunTime=00:00:00 TimeLimit=14-00:00:00 TimeMin=N/A
         SubmitTime=2023-01-18T16:36:06 EligibleTime=2023-01-18T16:36:06
         AccrueTime=2023-01-18T16:36:06
         StartTime=Unknown EndTime=Unknown Deadline=N/A
         NumNodes=1 NumCPUs=1 NumTasks=1 CPUs/Task=1 ReqB:S:C:T=0:0:*:*
         TRES=cpu=1,mem=6G,node=1,billing=1
         <output  cut> 

   Similar output is for the second job. Note :tt:`TimeLimit`.
   For each of two pending jobs the resource request is

   :math:`1 CPU * 14 days * 24 hrs = 336 hrs`

4. Check ALL the running jobs for your lab account

   .. code-block:: console

      [user@login-x:~]$ squeue -t R -A PI_lab -o "%.10i %.9P %.8j %.8u %.16a %.2t %.6C %l %L"
         JOBID PARTITION     NAME     USER       ACCOUNT ST   CPUS  TIME_LIMIT TIME_LEFT
      12341046  standard myjob_39  panteater      PI_lab  R      1 14-00:00:00 13-23:00:22
      12341047  standard myjob_40  panteater      PI_lab  R      1 14-00:00:00 13-23:00:22
      12341048  standard myjob_41  panteater      PI_lab  R      1 14-00:00:00 13-23:00:22
      < total 200 lines for 200 jobs >

   Each of 200 running jobs in the account has run for about 1hr out of allocated 14 days.
   Total max time Slurm has allocated for these running jobs is 

   :math:`1 CPU * 200 jobs * 14 days * 24 hrs = 67200 hrs`

   There are about *200 hrs* already used, (each job run ~1 hr),
   so remaining needed balance is :tt:`67100 hrs`. 
   Per step 1 above, your 2 pending jobs require

   :math:`1 CPU * 14 days * 24 hrs * 2 jobs = 672 hrs`.

   Slurm is computing that if all current jobs ran to their MAX times and if the next job
   were to run MAX time your account would end up negative:

   :math:`67300 - 67100 - 672 = -472 hrs`.

   Therefore Slurm puts these new jobs on hold.  
   These 2 jobs will  start running once some of the remaining running jobs completed
   and the account balance is sufficient.

  .. important:: It is important to correctly estimate time needed for the job,
                 and not ask for more resources (time, cpu, memory) than needed.

.. _fix pending job:

Fix your job
^^^^^^^^^^^^

   Similar fixes apply when using ``srun`` for interactive jobs.

   **You will need to cancel existing pending job (it will never run)**:

   .. code-block:: console

      [user@login-x:~]$ scancel <jobid>

   Next, resubmit the job so that the requested execution hours can be covered by your bank account balance.
   Check and update the following in your submit script:

   1. If your job was run from personal account

      | use a different Slurm account (lab) where you have enough balance
      |   :tt:`SBATCH -A` 

   2. Lower requirements of your job so that requested resources will be no more than core hours available in
      your account. This may mean to use:

      | fewer CPUs 
      |   :tt:`SBATCH --ntasks` or :tt:`#SBATCH --cpus-per-task` 

      | fewer CPUs but with increased memory per CPU 
      |   :tt:`SBATCH --ntasks` and :tt:`#SBATCH --mem-per-cpu` 

      | less memory
      |   :tt:`SBATCH --mem` or :tt:`#SBATCH --mem-per-cpu`

      | set a time limit that is shorter than the default runtime
      |   :tt:`SBATCH --time` 
      

   3. If your job is pending  due to `ReqNodeNotAvail, Reserved for
      maintenance` you need to re-submit your job with a shorter time limit
      that will end BEFORE the maintenance begins.

	  To find out the reservation details use:

      .. code-block:: console

         [user@login-x:~]$ scontrol show reservation

      | The first output line will include the maintenance times, for example:
      | :red:`StartTime=2023-07-25T08:00:00 EndTime=2023-07-26T08:00:00 Duration=1-00:00:00`

      Based on the info about the reservation and the current day/time you can
      estimate what time limit :tt:`SBATCH --time` should be specified for your job in order for
      it to finish before the maintenance starts.

      If your job truly needs requested time limit, nothing can be done until the maintenance is over.
      Remove your job from the queue and resubmit after the maintenance.

   See :ref:`available partitions` for partitions default and max settings.

   Please see :ref:`job examples` for more info.

.. _modify job:

Modification
------------

It is possible to make some changes to jobs that are still waiting to run 
by using the `scontrol` command.

If changes need to be made for a running job, it may be better to kill the job
and restart it after making the necessary changes.

Change job time limit:
  The  format set is  minutes,  minutes:seconds,  hours:minutes:seconds,  days-hours,
  days-hours:minutes  or  days-hours:minutes:seconds.  The *2-12:30* means 2days, 12hrs, and 30 min.

  .. code-block:: console

     [user@login-x:~]$ scontrol update jobid=<jobid> timelimit=<new timelimit>

Change QOS:
  By default, jobs are set to run with :.tt:`qos=normal`.
  :underline:`Users rarely need to change QOS`. 

  .. code-block:: console

     [user@login-x:~]$ scontrol update jobid=<jobid> qos=[low|normal|high]

.. _control jobs:

Cancel/Hold/Release
-------------------

The following commands can be used to:

Cancel a specific job:
  .. code-block:: console

     [user@login-x:~]$ scancel <jobid>

To cancel all jobs owned by a user:
  This only applies to jobs that are associated with your accounts

  .. code-block:: console

     [user@login-x:~]$ scancel -u <username>

To prevent a pending job from starting:
  .. code-block:: console

     [user@login-x:~]$ scontrol hold <jobid>

To release held jobs to run:
  .. code-block:: console

     [user@login-x:~]$ scontrol release <jobid>
