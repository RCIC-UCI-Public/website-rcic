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
