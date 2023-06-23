.. _slurm:

SLURM 
=====

Overview
---------

HPC3 will use the `SLURM scheduler <http://slurm.schedmd.com/slurm.html>`_
SLURM is used widely at super computer centers and is actively maintained.

We provide the numerous <<examples.txt#,EXAMPLES>> that show in depth how to run array jobs,
request GPUs, CPUs, and memory for a variety of different job types and common applications.


Dos and Dont's
--------------

Simple code of conduct is required of all users:

- *Do not run SLURM jobs in your $HOME*.
- *Do not run computational jobs on login nodes* this adversely affects
  many users. Login nodes are meant for light editing, short compilation and for submitting jobs.

- *All jobs, batch or interactive must be submitted to the scheduler*

- Any process that runs for more than an hour  or is using significant memory and CPU within an hour
  should be submitted to SLURM either as interactive or batch job. 
- Any compilation that asks for multiple threads while running make (for example
  make -j 8) needs to be done on interactive node.

- *ALL conda local environments and packages installs need to be done on interactive node*
- *Ssh access to the compute nodes is turned off* to prevent users from starting
  jobs bypassing SLURM.  See <<attachtojob, attaching to running job>> below.
- *Make sure you stay within your disk quota*. File system limits are generally the first
  ones that will negatively affect your job. See <</hpc3/hpc3-reference#storage, storage guides>>

- [red]*Long-running jobs will be removed from login nodes*
- [red]*We reserve the right to limit access for the users who abuse the system*


.. _attach to job:

Attach to a job
---------------

This is from reference guide :


== Free and Accounted Jobs [[cost]]
HPC3 dispenses with the idea of "owner" queues. Instead, jobs are classified into two types:

[horizontal]
Accounted:: The [.tt]*core-hours = #cores X wall-time* used by your job is charged to an account. Any job running this way cannot be killed or pre-empted by another job.  When the job completes, the core hours (or GPU hours) are debited from an account.

Free:: Jobs can run without charging an account in the free partition. Free jobs can get killed by another
accounted job (without warning). Maximum run times are more limited for free jobs.
+

//-

. [red]*Every user on HPC3 is given a one-time allotment of 1000 core hours*
* This is the account balance for personal use
* This number is NOT re-filled.
* If you have no other account to charge, you can use this account or the [.tt]*free* queues.

. [red]*Any UCI faculty who request an account will be granted 200,000^1^ no-cost CPU hours*
* These are hours per fiscal year, allocated in increments every 6 months^2^
* Unused hours can not be replenished later.
* Any UCI Professor can request an HPC3 lab account on behalf of their research group and add any number of
researchers/students to this account. They have complete control over who can charge to
their account and can put spending limits on any person.

^1^Based upon the number of requests and the number of nodes purchased by RCIC, this number will vary.

^2^Based on the unused hours the increment amount will vary

Condo owners have their systems _converted_ into core hours.  For example, a 40-core system can deliver
(with no downtime) a maximum of 350K core hours every year.  Each year that a physical condo node is in the cluster,
95% percent of the condo nodes' theoretical maximum is deposited into the owner's account.

.. _scratch storage:

Using scratch storage
---------------------

| Use as scratch storage for batch Jobs that repeatedly access many small files or make frequent small reads/writes:
|   - at job start: user needs to explicitly copy input files from DFS/CRSP to $TMPDIR
|   - at job end: user needs to explicitly copy output files from $TMPDIR to DFS/CRSP

