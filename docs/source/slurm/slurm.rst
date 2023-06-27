.. _slurm manager:

SLURM workload manager
======================

HPC3 is using the `SLURM <http://slurm.schedmd.com/slurm.html>`_
as the workload manager and job scheduler.
Slurm is widely used widely at super computer centers and is actively maintained.

.. _dos and donts:

Dos and Don'ts 
--------------

Cluster is a shared resource.  Please follow the :ref:`conduct rules` that describe 
how to properly use HPC3. These rules apply to using Slurm for running jobs.

Failure to follow conduct rules may adversely impact others working on the cluster. 

.. _slurm partitions:

Partitions Structure
--------------------

Slurm uses the term *partition* to signify a batch queue of resources.
HPC3 has heterogeneous hardware, memory footprints, and nodes with GPUs.

The tables below show available partitions, their memory, runtime
and job preemption configuration, and cost per hour in :ref:`units cost`.

.. table:: **Available CPU partitions**
   :widths: 15 30 20 20 15
   :class: noscroll-table

   +-----------+---------------------------+------------------+-------------+------------+
   | Partition | Default / Max             | Default / Max    | Cost        | Job        |
   |           |                           |                  |             |            |
   | name      | memory per core           | runtime          | (units/hr)  | preemtion  |
   +===========+===========================+==================+=============+============+
   | standard  | 3 GB / 6 GB               | 2 day / 14 day   | 1           | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | free      | 3 GB / 18 GB              | 1 day / 3 day    | None        | Yes        |
   +-----------+---------------------------+------------------+-------------+------------+
   | debug     | 3 GB / 18 GB              | 15 min / 30 min  | 1           | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | highmem   | 6 GB / 10 GB              | 2 day / 14 day   | 1           | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | hugemem   | 18 GB / 18 GB             |  2 day / 14 day  | 1           | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | maxmem    | 1.5 TB/node / 1.5 TB/node |  1 day / 7 day   | 40 / node   | No         |
   +-----------+---------------------------+------------------+-------------+------------+

* You must be added to a specific group to access the :tt:`highmem / hugemem/ maxmem` partitions.
  If you are not a member of these groups then  you will not be able to submit jobs to these
  partitions and ``sinfo`` command  will not show these partitions.

* The :tt:`maxmem` partition is a single 1.5 TB node and that is reserved for those rare applications that
  :underline:`really require that much memory`. You can only be allocated the entire node. No free
  jobs run in this partition.

.. table:: **Available GPU partitions**
   :widths: 15 30 20 20 15
   :class: noscroll-table

   +-----------+---------------------------+------------------+-------------+------------+
   | Partition | Default / Max             | Default / Max    | Cost        | Job        |
   |           |                           |                  |             |            |
   | name      | memory per core           | runtime          | (units/hr)  | preemtion  |
   +===========+===========================+==================+=============+============+
   | gpu       | 3 GB / 9 GB               | 2 day / 14 day   | 33          | No         |
   +-----------+---------------------------+------------------+-------------+------------+
   | free-gpu  | 3 GB / 9 GB               | 1 day / 3 day    | 0           | Yes        |
   +-----------+---------------------------+------------------+-------------+------------+
   | gpu-debug | 3 GB / 9 GB               | 15 min / 30 min  | 33          | No         |
   +-----------+---------------------------+------------------+-------------+------------+

* You must have a *gpu account* and you must specify it in order to submit to
  the *gpu/gpu-debug* partitions. This is because of differential charging.
  GPU accounts are not automatically given to everyone, your faculty adviser
  can request a GPU lab account.

* Anyone can run jobs in *free-gpu* partition without special account.

.. note:: Please do not override the memory defaults unless your particular job really requires it.
   Analysis of more than 3 Million jobs on HPC3 indicated that more than 98% of jobs fit within
   the defaults. With slightly smaller memory footprints, the scheduler has MORE choices as to where to place jobs on the cluster.

.. _slurm accounting:

Slurm Accounting
----------------

Every HPC3 user is granted :underline:`one time 1,000 free CPU hours` as a startup allowance.
This base allocation is there for you to become familiar with HPC3, Slurm scheduler, and accounting.
This personal base account is created automatically when your HPC3 account is created. 

Most jobs ran on HPC3 are charged to a lab account because most HPC3 users are part of at least one research lab.
If a lab account runs out of CPU hours, more CPU hours can be purchased via recharge.

Any UCI Professor can request an HPC3 *Slurm lab account* and add researchers/students to this account. 
The goal is faculty who request an account will be granted no-cost 200,000 CPU hours per fiscal year.
Based upon the number of requests and the number of nodes that have been purchased by RCIC, this number will vary.  

.. _slurm lab account:

Getting Slurm Lab account
^^^^^^^^^^^^^^^^^^^^^^^^^

PI may request a Slurm lab account by sending a request to hpc-support@uci.edu and specifying 
the following information:

* PI name and UCINetID
* Names and UCINetIDs of the researchers, graduate students or other
  collaborators to add to the account. They will be be able to charge CPU hours to the  lab account.
* Optional: names of  *account coordinators*.  Account coordinators are lab members who will able to manage the group
  members jobs, modify their queue priority, update limits for the total CPU hours for individual members, etc.
  Typically, one or two lab members (Postdocs or Project Specialists).

.. _units cost:

Allocation units
^^^^^^^^^^^^^^^^

When a job is allocated resources, the resources include CPUs and memory.
Memory in each partition is allocated per-CPU core.
When you request more cores, your job is allocated more memory and vice versa.

Jobs will charge **core-hours** or **GPU-hours** to the account.
The costs are calculated as follows.

:1 core-hour:
  | :bluelight:`is 1 allocation unit` charged for 
  | 1 CPU used for 1 hour 
  | Each CPU core-hour is charged to the specified account (or your default user account).

:1 GPU-hour:
  | :bluelight:`is 33 allocation units` charged for
  | 1 GPU used for 1 hour as 32 allocation units, plus
  | 1 CPU used for 1 hour (required to run the job) as 1 allocation unit.
  | Each GPU hour is charged to a GPU-enabled account which can only be used on GPU-nodes.

**Example charges**

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

Free Jobs
^^^^^^^^^

Jobs submitted to *free* partitions are free jobs.

The design of HPC3 is that, on average, about 20% of the cluster is available for free jobs.
The *free* partitions are designed to allow the cluster to run at ~100% utilization, and make it possible
for the  allocated jobs to have very quick access to the resources when needed.
This is accomplished by letting allocated jobs to displace (kill) running free jobs.

Free jobs have the following properties:

* **are not charged to any account**.  However, the balance in the account must have enough core hours to cover the job
  request, even though this amount will not be charged.
  This is how Slurm makes an estimate what resources are used and for how long.
* **can be killed at any time to make room for allocated jobs**.
  When the *standard* partition becomes full, jobs in *free* partition are killed in order to
  allow the allocated jobs to run with a priority. In an attempt to get as much *goodput* through the system,
  the most-recently started free jobs will be killed first.

.. _allocated jobs:

Allocated Jobs
^^^^^^^^^^^^^^

Jobs submitted to the *standard* partition are *allocated* jobs.

Standard jobs have the following properties:

* **are charged to a specified account**. Default is a user account.
* **can not be killed** by any other job.
* **can preempt free jobs**
* once start running  will run to completion
* jobs with QOS set to *normal* are charged for the CPU time consumed.
* jobs with QOS set to *high* are charged double the CPU time consumed.
* Jobs with QOS set to *high* are placed at the front of the jobs queue.
  They are meant to be used when a user needs to jump in front of the queue when
  the time from submission to running is of the essence (i.e. grant proposals and paper deadlines).

