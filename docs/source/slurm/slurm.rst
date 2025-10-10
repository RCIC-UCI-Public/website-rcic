.. _slurm manager:

Slurm workload manager
======================

.. contents::
   :local:

HPC3 is using the `SLURM <http://slurm.schedmd.com/slurm.html>`_
as the workload manager and job scheduler.
Slurm is widely used widely at super computer centers and is actively maintained.

.. _dos and donts:

Dos and Don'ts
--------------

Cluster is a shared resource.  Please follow the :ref:`conduct rules` that describe
how to properly use HPC3. These rules apply to using Slurm for running jobs.

Failure to follow conduct rules may adversely impact others working on the cluster.

.. _slurm accounting:

Slurm Accounting
----------------

Each personal and lab account has a balance that is getting used when you run Slurm jobs.

:bluelight:`Slurm Personal account`
  is created automatically when your HPC3 account is created.
  Every user is granted :underline:`one time 1000 free CPU hours` as a startup allowance.
  This base allocation is there for you to become familiar with HPC3, Slurm scheduler, and accounting.

:bluelight:`Slurm Lab accounts`
  Any UCI Professor can request an HPC3 *Slurm Lab account* and add researchers/students to this account.
  The goal is faculty who request an account will be granted no-cost 200,000 CPU hours per fiscal year.
  Based upon the number of requests and the number of nodes that have been purchased by RCIC, this number will vary.

  Most jobs ran on HPC3 are charged to *Slurm Lab accounts* because most HPC3 users are part of at least one research lab.
  If a lab account runs out of CPU hours, more CPU hours can be purchased via recharge.

.. _slurm lab account:

Getting Slurm Lab Account
^^^^^^^^^^^^^^^^^^^^^^^^^

PI may request a *Slurm Lab account* by sending a request to hpc-support@uci.edu and specifying
the following information:

  * PI name and UCInetID
  * Name and UCInetID of the researchers, graduate students or other
    collaborators to add to the account. They will be be able to charge CPU hours to the lab account.

..  * Optional: names of  *account coordinators*.  Account coordinators are lab members who will able to manage the group
  members jobs, modify their queue priority, update limits for the total CPU hours for individual members, etc.
  Typically, one or two lab members (Postdocs or Project Specialists).

.. attention:: | Students and group members who wish to use Slurm Lab account
               | please see :ref:`add lab account`

Accounts balances
^^^^^^^^^^^^^^^^^

Please learn

  * :ref:`How to check <job accounting>` your account balances.
  * What :ref:`Allocations <allocations>` are available.
  * How :ref:`Realloations <reallocation>` are done.

.. _units cost:

:bluelight:`Allocation Units`
  When a job is allocated resources, the resources include CPUs and memory.
  Memory in each partition is allocated per-CPU core.
  When you request more cores, your job is allocated more memory and vice versa.

  Jobs will charge **core-hours** or **GPU-hours** to the account.
  The costs are calculated as follows.

  :1 core-hour:
    | :bluelight:`is 1 allocation unit` charged for
    | 1 CPU used for 1 hour
    | Each CPU core-hour is charged to the specified account. Default is your
      *Slurm Personal account*.

  :1 GPU-hour:
    | :bluelight:`is 33 allocation units` charged for
    | 1 GPU used for 1 hour as 32 allocation units, plus
    | 1 CPU used for 1 hour (required to run the job) as 1 allocation unit.
    | Each GPU hour is charged to a GPU-enabled account which can only be used on GPU-nodes.

  Example charges

    .. table::
       :class: noscroll-table

       +--------------------------+----------------+
       | A job is using           | Units  charged |
       +==========================+================+
       | 1 CPU X 1 hr             | 1              |
       +--------------------------+----------------+
       | 1 CPU X 6 min            | 0.1            |
       +--------------------------+----------------+
       | 10 CPU X 1 hr            | 10             |
       +--------------------------+----------------+
       | (1 GPU + 1 CPU ) X 1 hr  | 33             |
       +--------------------------+----------------+

.. _free jobs:
.. _allocated jobs:

Free and Allocated Jobs
^^^^^^^^^^^^^^^^^^^^^^^

| All computational processes on the cluster must be submitted as Slurm jobs.
| **Charging jobs to an account is new for the UCI community**.
| There are two types of jobs:

  :bluelight:`allocated`
    jobs are charged to an account.  A large fraction of users will run allocated jobs
    and never see the limits of their accounts.
  :bluelight:`free`
    jobs are not charged to an account. Users who are running a very large number of free jobs are likely to have some of
    their jobs preempted (killed).

.. centered:: Slurm jobs properties

.. table::
   :class: noscroll-table
   :widths: 43,57

   +-------------------------------------------------+----------------------------------------------------------------+
   | Free jobs                                       | Allocated jobs                                                 |
   +=================================================+================================================================+
   | Are submitted to *free*, *free-gpu\** partitions| Are Submitted to all other partitions                          |
   +-------------------------------------------------+----------------------------------------------------------------+
   | Are not charged to any account [1]_             | Are charged to a specified account.                            |
   |                                                 |                                                                |
   | Default is a user personal Slurm account        | Default is a user personal Slurm account                       |
   +-------------------------------------------------+----------------------------------------------------------------+
   | Can be killed at any time to make room          | Can not be killed by any other job.                            |
   |                                                 |                                                                |
   | for allocated jobs [2]_                         | Once start, will run to completion                             |
   +-------------------------------------------------+----------------------------------------------------------------+
   |                                                 | Can preempt free jobs                                          |
   +-------------------------------------------------+----------------------------------------------------------------+
   |                                                 | Jobs with QOS *normal* are charged for the CPU time used       |
   |                                                 |                                                                |
   |                                                 | Jobs with QOS *high* are charged double the CPU time           |
   |                                                 |                                                                |
   |                                                 | used and are placed at the front of the jobs queue [3]_        |
   +-------------------------------------------------+----------------------------------------------------------------+
   | Submitted with ``sbatch`` for batch jobs        | Submitted with ``sbatch`` for batch jobs                       |
   |                                                 |                                                                |
   | Submitted with ``srun`` for interactive jobs    | Submitted with ``srun`` for interactive jobs                   |
   +-------------------------------------------------+----------------------------------------------------------------+

.. [1] The account balance must have enough core hours to cover the job
       request, even though this amount will not be charged.
       This is how Slurm makes an estimate what resources are used and for how long.
       when using a personal account, a user is limited to submitting jobs requesting a total of 1000 core hours
       which is the maximum possible personal balance.

.. [2] When a non-free (for example, *standard*) partition becomes full, jobs in *free* partition are killed in order to
       allow the allocated jobs to run with a priority. In an attempt to get as much *goodput* through the system,
       the most-recently started free jobs will be killed first.

.. [3] Jobs with QOS set to *high*  are meant to be used when a user needs to jump in front of the queue when
       the time from submission to running is of the essence (i.e. grant proposals and paper deadlines).

.. _partitions structure:

Partitions Structure
--------------------

Slurm uses the term *partition* to signify a batch queue of resources.
HPC3 has heterogeneous hardware, memory footprints, and nodes with GPUs.

The tables below show available partitions, their memory, runtime
and job preemption configuration, and cost per hour in :ref:`units cost`.

GPUs in the ``gpu`` partition can natively accelerate 64-bit floating point.
GPUs in the ``gpu32`` partition can natively accelerate 32-bit floating point, but *cannot* accelerate 64-bit floating point.


.. _available partitions:

.. table:: **Available CPU partitions**
   :widths: 15 30 20 20 15
   :class: noscroll-table

   +-----------+---------------------------+------------------+-------------+------------+
   | Partition | Default / Max             | Default / Max    | Cost        | Job        |
   |           |                           |                  |             |            |
   | name      | memory per core           | runtime          | (units/hr)  | preemption |
   +===========+===========================+==================+=============+============+
   | free      | 3 GB / 18 GB              | 1 day / 3 day    | None        | Yes        |
   +-----------+---------------------------+------------------+-------------+------------+
   | standard  | 3 GB / 6 GB               | 2 day / 14 day   | 1           | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | highmem   | 6 GB / 10 GB              | 2 day / 14 day   | 1           | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | hugemem   | 18 GB / 18 GB             |  2 day / 14 day  | 1           | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | maxmem    | 1.5 TB/node / 1.5 TB/node |  1 day / 7 day   | 40 / node   | No         |
   +-----------+---------------------------+------------------+-------------+------------+
.. note::
   You *cannot* submit to the ``standard``, ``highmem``, ``hugemem``, or ``maxmem`` partitions with a Slurm account
   that ends with ``gpu`` or ``gpu32``.


.. table:: **Available GPU partitions**
   :widths: 15 30 20 20 15
   :class: noscroll-table

   +------------+---------------------------+------------------+-------------+------------+
   | Partition  | Default / Max             | Default / Max    | Cost        | Job        |
   |            |                           |                  |             |            |
   | name       | memory per core           | runtime          | (units/hr)  | preemption |
   +============+===========================+==================+=============+============+
   | gpu        | 3 GB / 9 GB               | 2 day / 14 day   | 33          | No         |
   +------------+---------------------------+------------------+-------------+------------+
   | free-gpu   | 3 GB / 9 GB               | 1 day / 3 day    | 0           | Yes        |
   +------------+---------------------------+------------------+-------------+------------+
   | gpu32      | 3 GB / 9 GB               | 2 day / 14 day   | 33          | No         |
   +------------+---------------------------+------------------+-------------+------------+
   | free-gpu32 | 3 GB / 9 GB               | 1 day / 3 day    | 0           | Yes        |
   +------------+---------------------------+------------------+-------------+------------+


.. note::
   To submit to the ``gpu`` partition, you must have a Slurm account that ends with ``gpu``.
   To submit to the ``gpu32`` partition, you must have a Slurm account that ends with ``gpu32``.

Note, there is no difference in cost/core-hour for default and max memory per core.

.. _memory partitions:

Higher Memory
^^^^^^^^^^^^^

There are a few applications that need more memory than a node in standard
partition can offer. Users must be added to a specific group to access the
higher memory :tt:`highmem / hugemem / maxmem` partitions.

If you are not a member of these groups then  you will not be able to submit jobs to these
partitions and ``sinfo`` command  will not show these partitions.

User must be either:
  | (a) member of a group that purchased these node types or
  | (b) clearly demonstrate that their applications require more than standard memory.

    .. attention:: To demonstrate your job requires more memory submit a ticket with the
                   following information:

                   * your job ID and error message
                   * what was your submit script
                   * what is the memory (in GB) that your job needs
                   * include the output of ``seff`` and ``sacct`` commands about your job

:bluelight:`highmem / hugemem`
  There is no difference in cost/core-hour on any of the CPU partitions,

:bluelight:`maxmem`
  The partition is a single 1.5 TB node and that is reserved for those rare applications that
  :underline:`really require that much memory`. You can only be allocated the entire node. No free
  jobs run in this partition.


.. _gpu partitions:

GPU-enabled
^^^^^^^^^^^

:bluelight:`gpu and gpu32`
  You must have a *GPU* or *GPU32 Lab account* and you must specify it in order to submit
  jobs to these partitions. This is because of differential charging.
  There are NO personal GPU accounts.

  **GPU accounts are not automatically given to everyone, your faculty adviser
  can request a GPU Lab account**. See how to
  :ref:`request Slurm Lab account <slurm lab account>` and add a note that
  this request is for GPU account.

:bluelight:`free-gpu`
  Anyone can run jobs in this partition without special account.

.. _node info:

Node/partition Information
--------------------------

| ``sinfo``    show information about nodes and partitions
| ``scontrol`` show details of configuration

Use above commands to get information about nodes and partitions.
There are many command line options available, please run ``man sinfo``
and ``man scontrol`` for detailed information about options.

A few useful examples show information for:

Nodes grouped by features:
  .. code-block:: console

     [user@login-x:~]$ sinfo -o "%33N %5c %8m %30f %10G" -e
     NODELIST                          CPUS MEMORY   AVAIL_FEATURES                 GRES
     hpc3-19-13                        36   515000   intel,mlx5_ib                  (null)
     hpc3-15-[20,22-23],hpc3-17-[00-03 40   386000   intel,avx512,mlx5_ib           (null)
     hpc3-19-12                        24   515000   intel,mlx4_ib                  (null)
     hpc3-19-[14-15]                   36   515000   intel,mlx4_ib                  (null)
     hpc3-20-[16-20],hpc3-22-05        48   384000   intel,avx512,mlx5_ib           (null)
     hpc3-20-[21-22]                   48   772000   intel,avx512,mlx5_ib,nvme,fast (null)
     hpc3-20-24                        48   385000   intel,avx512,mlx5_ib           (null)
     hpc3-21-[00-15,18-32],hpc3-22-[00 48   191000   intel,avx512,mlx5_ib,nvme,fast (null)
     ... output cut ...
     hpc3-l18-01                       64   515000   amd,epyc,epyc7601,mlx4_ib      (null)
     hpc3-l18-[04-05]                  28   257000   intel,avx512,mlx4_ib           (null)
     hpc3-gpu-16-[00-07],hpc3-gpu-17-[ 40   192000   intel,avx512,mlx5_ib           gpu:V100:4
     hpc3-gpu-l54-[03-06]              32   256000   intel,avx512,mlx5_ib,nvme,fast gpu:A100:2
     hpc3-gpu-l54-[08-09]              32   257000   intel,avx512,mlx5_ib,nvme,fast gpu:A30:4
     hpc3-gpu-18-00                    40   386000   intel,avx512,mlx5_ib           gpu:V100:4
     hpc3-gpu-18-[03-04],hpc3-gpu-24-[ 32   256000   intel,avx512,mlx5_ib,nvme,fast gpu:A30:4
     hpc3-gpu-k54-00                   64   3095000  intel,avx512,mlx5_ib,nvme,fast gpu:A30:4
     hpc3-22-[15-16]                   64   2063000  intel,avx512,mlx5_ib,nvme,fast (null)
     hpc3-l18-02                       40   1547000  intel,mlx4_ib                  (null)

Each node by features without grouping:
  .. code-block:: console

     [user@login-x:~]$ sinfo -o "%20N %5c %8m %20f %10G" -N
     NODELIST             CPUS  MEMORY   AVAIL_FEATURES       GRES
     hpc3-14-00           40    192000   intel,avx512,mlx5_ib (null)
     hpc3-14-00           40    192000   intel,avx512,mlx5_ib (null)
     hpc3-14-01           40    192000   intel,avx512,mlx5_ib (null)
     hpc3-14-01           40    192000   intel,avx512,mlx5_ib (null)
     hpc3-14-02           40    192000   intel,avx512,mlx5_ib (null)
     hpc3-14-02           40    192000   intel,avx512,mlx5_ib (null)
     ... output cut ...

Specific single node:
  .. code-block:: console

     [user@login-x:~]$ sinfo -o "%20N %5c %8m %20f %10G" -n hpc3-gpu-16-00
     NODELIST             CPUS  MEMORY   AVAIL_FEATURES       GRES
     hpc3-gpu-16-00       40    192000   intel,avx512,mlx5_ib gpu:V100:4

  A more detailed information is obtained with

  .. code-block:: console

     [user@login-x:~]$ scontrol show node hpc3-gpu-16-00
     NodeName=hpc3-gpu-16-00 Arch=x86_64 CoresPerSocket=20
     CPUAlloc=26 CPUEfctv=40 CPUTot=40 CPULoad=6.80
     AvailableFeatures=intel,avx512,mlx5_ib
     ActiveFeatures=intel,avx512,mlx5_ib
     Gres=gpu:V100:4
     NodeAddr=hpc3-gpu-16-00 NodeHostName=hpc3-gpu-16-00 Version=24.05.3
     OS=Linux 4.18.0-477.15.1.el8_8.x86_64 #1 SMP Wed Jun 28 15:04:18 UTC 2023
     RealMemory=192000 AllocMem=150720 FreeMem=39430 Sockets=2 Boards=1
     State=MIXED ThreadsPerCore=1 TmpDisk=228000 Weight=3 Owner=N/A MCS_label=N/A
     Partitions=free-gpu,gpu
     BootTime=2024-09-17T15:48:44 SlurmdStartTime=2024-10-22T16:04:19
     LastBusyTime=2024-10-21T16:19:36 ResumeAfterTime=None
     CfgTRES=cpu=40,mem=187.50G,billing=168,gres/gpu=4
     AllocTRES=cpu=26,mem=150720M,gres/gpu=4
     CurrentWatts=0 AveWatts=0

How many CPU and GPUs are available in GPU partition:
  .. code-block:: console

     [user@login-x:~]$ sinfo -NO "CPUsState:14,Memory:9,AllocMem:10,Gres:14,GresUsed:22,NodeList:20" -p gpu
     CPUS(A/I/O/T) MEMORY  ALLOCMEM GRES        GRES_USED              NODELIST
     40/0/0/40     180000  122880   gpu:V100:4  gpu:V100:4(IDX:0-3)    hpc3-gpu-16-00
     20/20/0/40    180000  174080   gpu:V100:4  gpu:V100:3(IDX:0-1,3)  hpc3-gpu-16-02
     4/36/0/40     180000  22528    gpu:V100:4  gpu:V100:3(IDX:0,2-3)  hpc3-gpu-17-04
     0/40/0/40     372000  0        gpu:V100:4  gpu:V100:0(IDX:N/A)    hpc3-gpu-18-00
     4/36/0/40     180000  32768    gpu:V100:4  gpu:V100:4(IDX:0-3)    hpc3-gpu-18-01
     4/36/0/40     180000  32768    gpu:V100:4  gpu:V100:4(IDX:0-3)    hpc3-gpu-18-02
     4/28/0/32     245000  12288    gpu:A30:4   gpu:A30:2(IDX:0,2)     hpc3-gpu-18-03
     2/30/0/32     245000  6144     gpu:A30:4   gpu:A30:1(IDX:3)       hpc3-gpu-18-04
     0/32/0/32     245000  0        gpu:A30:4   gpu:A30:0(IDX:N/A)     hpc3-gpu-24-05
     4/28/0/32     245000  32768    gpu:A30:4   gpu:A30:1(IDX:0)       hpc3-gpu-24-08
     0/32/0/32     245000  0        gpu:A30:4   gpu:A30:0(IDX:N/A)     hpc3-gpu-k54-01
     15/17/0/32    245000  46080    gpu:A100:2  gpu:A100:2(IDX:0-1)    hpc3-gpu-l54-03
     0/32/0/32     245000  0        gpu:A30:4   gpu:A30:0(IDX:N/A)     hpc3-gpu-l54-07
     ... output cut ...

  The above output shows in the columns:

  | CPUS(A/I/O/T): number of cores by state as "Allocated/Idle/Other/Total"
  | ALLOCMEM: memory already in use
  | GRES: type and number of GPUs
  | GRES_USED: which GPUs are in use, the part after GPU type means:
  |    * 4(IDX:0-3) all four are in use (0,1,2,3)
  |    * 3(IDX:0,2-3) three are in use (0,2,3) and one (1) is free
  |    * 0(IDX:N/A) all are free
  | NODE_LIST: nodes with this configuration

Detailed configuration of a standard queue:
  .. code-block:: console

     [user@login-x:~]$ scontrol show partition standard
     PartitionName=standard
        AllowGroups=ALL AllowAccounts=ALL AllowQos=normal,high
        AllocNodes=ALL Default=YES QoS=normal
        DefaultTime=2-00:00:00 DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
        MaxNodes=159 MaxTime=14-00:00:00 MinNodes=1 LLN=NO MaxCPUsPerNode=64
        Nodes=hpc3-14-[00-31],hpc3-15-[00-19,21,24-31],hpc3-17-[08-11],...
        PriorityJobFactor=100 PriorityTier=100 RootOnly=NO ReqResv=NO OverSubscribe=NO
        OverTimeLimit=0 PreemptMode=OFF
        State=UP TotalCPUs=7136 TotalNodes=159 SelectTypeParameters=CR_CORE_MEMORY
        JobDefaults=(null)
        DefMemPerCPU=3072 MaxMemPerCPU=6144
        TRES=cpu=7136,mem=35665000M,node=159,billing=7136
