
.. _news:

News & Events
=============

* General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
* Any additional information is outlined in notification emails to hpc-users@uci.edu
  (all current users) and is described in the details below.
* When the maintenance is completed all users are notified via emails to hpc-users@uci.edu.

| :blogtitle:`HPC3 and CRSP during Winter Administrative Recess`

| :red:`The RCIC staff will be on Winter Administrative Recess December 24, 2024, to January 2, 2025`

**HPC3 and CRSP remain operational during the Winter Break**

However, during this time we will :red:`respond only to critical situations`. Any questions
regarding routine issues and services will be dealt with when we return to work after January 2nd, 2025. 

RCIC staff volunteer their time  during the campus shutdown.

Examples of critical and routine issues are listed below:
  :bluelight:`Critical situations (not a comprehensive list)`:

  - physical damage to the nodes
  - emergency power restoration to the servers
  - security break-in
  - down file servers

  :bluelight:`Routine issues (not a comprehensive list):`

  - HPC3/CRSP account management
  - access to PI's lab resources (Slurm/CRSP)
  - any Slurm job issues such as pending, etc.
  - any over quota questions
  - any software questions or requests

| Please refrain from sending tickets about non-critical issues during the recess.
| We appreciate your cooperation and wish you a Happy Holiday Season!


| :blogtitle:`HPC3 Downtime December 18, 2024`

| :red:`The next outage will be before Christmas break, December 18, 2024, beginning at 8am`

Maintenance Items:
  1. OS revision update from **Rocky 8.8 to Rocky 8.10**.
  #. Full rebuild of all software, see table below for software changes.
  #. Top-to-bottom re-installation of all compute and login nodes.

Impacts:
  This is a full outage

  1. All existing logins will be terminated.
  #. You will NOT have access to HPC3 or CRSP during the planned downtime.
  #. No jobs can run during the maintenance period.
  #. Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on December 18 will be held.
     Please see :ref:`requesting time limits <request time>` on queues.
  #. After the maintenance you may need to reinstall software that you compiled or installed yourself.

Software changes:
  | Some modules will be removed because they cannot be built on a new system or are unused. 
  | Note, the table below will be periodically updated till the maintenance date.

  .. table:: **Software changes**
     :align: center
     :class: noscroll-table

     +--------------------------------------+-----------------------------------+
     | Scheduled to be removed              | Use instead                       |
     +======================================+===================================+
     | afni/20.3.01                         | afni/22.1.09                      |
     +--------------------------------------+-----------------------------------+
     | amber/19.11/gcc.8.4.0                | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | ants/2.2.0                           | ants/2.3.5                        |
     +--------------------------------------+-----------------------------------+
     | aria2/1.36.0                         |                                   |
     +--------------------------------------+-----------------------------------+
     | biom-format/2.1.12                   |                                   |
     +--------------------------------------+-----------------------------------+
     | bionetgen/2.5.1                      |                                   |
     +--------------------------------------+-----------------------------------+
     | bionetgen/2.8.0                      |                                   |
     +--------------------------------------+-----------------------------------+
     | bowtie2/1.2.3                        | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | bowtie2-python2/2.4.1                | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | bowtie2/2.4.4                        | bowtie2/2.5.1                     |
     +--------------------------------------+-----------------------------------+
     | boost/1.50.0/gcc_8.4.0               | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | boost/1.71.0/gcc_8.4.0               | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | cellranger/3.1.0                     | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | charm/6.10.1/gcc.8.4.0-openmpi.4.0.3 | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | cmseq/1.0.4                          |                                   |
     +--------------------------------------+-----------------------------------+
     | dendropy/4.5.2                       |                                   |
     +--------------------------------------+-----------------------------------+
     | fastp/0.20.0                         | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | ffmpeg/0.10.16                       | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | ffmpeg/1.2.12                        | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | fftw/3.3.8/gcc.8.4.0-openmpi.4.0.3   | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | foundation/v7                        | foundaiton/v8 [#]_                |
     +--------------------------------------+-----------------------------------+
     | freesurfer/7.1.1                     | newer version                     |
     +--------------------------------------+-----------------------------------+
     | freesurfer/7.3.2                     | newer version                     |
     +--------------------------------------+-----------------------------------+
     | gromacs/2020.4/gcc.8.4.0             | newer version                     |
     +--------------------------------------+-----------------------------------+
     | hclust2/1.0.0                        |                                   |
     +--------------------------------------+-----------------------------------+
     | hdf5/1.10.5/gcc.system-openmpi.4.1.1 | newer version                     |
     +--------------------------------------+-----------------------------------+
     | hdf5/1.10.5/intel.2020u1-openmpi.4.0.3 | newer version                   |
     +--------------------------------------+-----------------------------------+
     | humann/3.0.1                         |                                   |
     +--------------------------------------+-----------------------------------+
     | icu/70.1                             |                                   |
     +--------------------------------------+-----------------------------------+
     | igv/2.12.3                           |                                   |
     +--------------------------------------+-----------------------------------+
     | jags/4.3.0                           |                                   |
     +--------------------------------------+-----------------------------------+
     | julia/1.7.1                          | newer version                     |
     +--------------------------------------+-----------------------------------+
     | likwid/5.0.1                         |                                   |
     +--------------------------------------+-----------------------------------+
     | likwid/5.2.1                         |                                   |
     +--------------------------------------+-----------------------------------+
     | lz4/1.9.3                            | available without module          |
     +--------------------------------------+-----------------------------------+
     | metaphlan/3.0.14                     |                                   |
     +--------------------------------------+-----------------------------------+
     | miniconda3/4.8.5 [2]_                | miniconda3/23.5.2                 |
     +--------------------------------------+-----------------------------------+
     | miniconda3/4.12.0 [2]_               | miniconda3/23.5.2                 |
     +--------------------------------------+-----------------------------------+
     | mrtrix3/3.0.2                        |                                   |
     +--------------------------------------+-----------------------------------+
     | mrtrix3/3.0.3                        |                                   |
     +--------------------------------------+-----------------------------------+
     | nco/4.9.6/gcc.8.4.0                  | newer version                     |
     +--------------------------------------+-----------------------------------+
     | parallel/20211222                    | available without module          |
     +--------------------------------------+-----------------------------------+
     | phylophlan/3.0.2                     |                                   |
     +--------------------------------------+-----------------------------------+
     | pytorch/1.5.1                        | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | tophat/2.1.1                         |                                   |
     +--------------------------------------+-----------------------------------+
     | qiime2/2020.8                        | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | qiime2/2021.2                        | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | qiime2/2022.2                        | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | roary/3.13.0                         |                                   |
     +--------------------------------------+-----------------------------------+
     | udunits/2.2.26/intel.2020u1          | newer versions                    |
     +--------------------------------------+-----------------------------------+
     | xz/5.2.5                             | available without module          |
     +--------------------------------------+-----------------------------------+

  .. [#] The foundation/v8 module will be provided for backwards
         compatibility. It will simply load a few other modules
         to provide an access to the commonly used tools. If you are using
         a specific tool from the current foundation/v8 you will be able to switch
         to using the specific module for that tool 
         (see output of ``module display foundation/v8``)
         
  .. [#] :red:`IMPORTANT:` If you are currently using miniconda/4.8.5 or miniconda3/4.12.0
         please follow :ref:`update miniconda3`.

