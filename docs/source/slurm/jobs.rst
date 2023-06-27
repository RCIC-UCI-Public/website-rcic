.. _jobs:

Jobs
=====

Charging jobs to an account is new for the UCI community. Like any policy, it can be two-edged. 

* A large fraction of users should be able to run :ref:`allocated jobs` and never see the limits of their accounts.
* Users who are running a very large number of :ref:`free jobs` are likely to have some of
  their free jobs preempted (killed).

TODO 

We provide the numerous <<examples.txt#,EXAMPLES>> that show in depth how to run array jobs, request GPUs,
CPUs, and memory for a variety of different job types and common applications.

TODO The scripts can be downloaded from link:examples[this directory].

There are a few methods to submit your jobs to Slurm: *batch*, *interactive*, and
*running jobs immediately*.  Please see sections below.

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

.. _batch job:

Batch Job
---------

``sbatch submit-script.sub``

A batch job is run at sometime in the future by the scheduler.
Submitting batch jobs to Slurm is done with the ``sbatch`` command
and the job description is provided by the submit script.
An example job submit script:

.. centered:: File simplejob.sub

.. literalinclude:: files/simplejob.sub
   :language: bash

To submit a job on HPC3, login and using your favorite editor create
:tt:`simplejob.sub` file with the contents shown above.

Edit the Slurm account to charge for the job to either your personal account or lab account.
Your personal account is the same as your UCINetID.

To submit the job:
  .. code-block:: console

     [user@login-x:~]$ sbatch simplejob.sub
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

.. _job status:

Job Status
----------

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


.. _attach to job:

Attach to a job
---------------

``srun --pty --jobid``

.. attention:: The ssh access to compute nodes is turned off

Users will need to use Slurm commands to find a job ID and to attach to
*running jobs* if they want
to run simple jobs verification commands on the node where their job is running.

Find *jobid* and attach to it:
  .. code-block:: console

     [user@login-x:~]$ squeue -u panteater
       JOBID PARTITION     NAME      USER ST       TIME  NODES NODELIST(REASON)
     3559123      free    Tst41 panteater  R   17:12:33      5 hpc3-14-02
     3559124      free    Tst42 panteater  R   17:13:33      7 hpc3-14-17,hpc3-15-[05-08]

     [user@login-x:~]$ srun --pty --jobid 3559123 --overlap /bin/bash

  This  will put a user on the *hpc3-14-02* node where the job is running
  and will **run inside the cgroup (CPU, RAM etc.) of the running job**.

  This means the user will be able to execute simple commands
  such as :tt:`ls, top, ps`, etc., but will not be able to
  start new processes that use resources outside of what is specified in
  *jobid*. Any command will use computing resources, and therefore will add to
  the usage of the job.

  After executing your desired verification commands simply type **exit**.
  The original job will be still running.

Attach to a specific node using :tt:`-w` switch (for multi-node jobs):

  .. code-block:: console

     [user@login-x:~]$ srun --pty --jobid 3559124 --overlap -w hpc3-14-17 /bin/bash

Most often users just need to see the processes of the job, etc. Such commands
can be run directly.  Run ``top`` command while attaching to the running job: 

  .. code-block:: console

     [user@login-x:~]$ srun --pty --overlap --jobid $JOBID top


.. _mail notification:

Mail notification
-----------------

.. _scratch storage:

Using scratch storage
---------------------

| Use as scratch storage for batch Jobs that repeatedly access many small files or make frequent small reads/writes:
|   - at job start: user needs to explicitly copy input files from DFS/CRSP to $TMPDIR
|   - at job end: user needs to explicitly copy output files from $TMPDIR to DFS/CRSP

