
.. _news:

News & Events
=============

* General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
* Any additional information is outlined in notification emails to hpc-users@uci.edu
  (all current users) and is described in the details below.
* When the maintenance is completed all users are notified via emails to hpc-users@uci.edu.

July, 2025
-------------

| :blogtitle:`HPC3 Downtime July XX, 2025`
| :blogauthor:`2025-05-13 by Nadya Williams`

| The next outage will be July (date to be determined), 2025, beginning at 8am.
| The cluster will be unavailable for most of the day.

Maintenance Items:
  1. OS version update from **Rocky 8.10 to Rocky 9**.
  #. Top-to-bottom re-installation of all compute and login nodes.
  #. Full rebuild of all applications software, see table below for software changes.
  #. Full rebuild of Slurm software.

Impacts:
  This is a full outage.

  #. All existing logins will be terminated.
  #. You will NOT have access to HPC3 during the planned downtime.
  #. You will have access to CRSP using `Web based File browser` or `CRSP Desktop App`.
  #. No Slurm jobs can run or can be pending in the queue.
  #. :red:`All jobs remaining in the queue on the maintenance day will be terminated`.
  #. Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on the day of maintenance
     will need to be resubmitted after the maintenance.
     Please see :ref:`requesting time limits <request time>` on queues.

Software changes:
  The operating system update involves many changes across the software stack.
  While we try to build all the previous software versions for the new OS, some builds are
  impossible. As a result, some modules will be removed because they cannot be built on a new system or because
  the underlying requirements are no longer satisfied.

  *Note, the table below will be periodically updated till the maintenance date*.

  .. table:: **Software changes**
     :align: center
     :class: noscroll-table
     :widths: 50,50

     +--------------------------------------------------------+------------------------------------------------------+
     | Module                                                 | Comments                                             |
     +========================================================+======================================================+
     | salmon/1.2.1                                           | Cannot build, removed                                |
     +--------------------------------------------------------+------------------------------------------------------+
     | bcftools/1.10.2                                        | Cannot build, use newer version                      |
     +--------------------------------------------------------+------------------------------------------------------+
     | For R/4.1.2                                            | Seurat and leiden packages cannot be                 |
     |                                                        | built. Use newer R if you need these                 |
     |                                                        | packages.                                            |
     +--------------------------------------------------------+------------------------------------------------------+
     | For R/4.2.2                                            | Seurat and leiden packages cannot be                 |
     |                                                        | built. Use newer R if you need these                 |
     |                                                        | packages.                                            |
     +--------------------------------------------------------+------------------------------------------------------+
     |                                                        | Update packages:                                     |
     |                                                        |                                                      |
     | For R/4.3.3                                            | * Seurat to version 5.3.0                            |
     |                                                        | * SeuratObject to version 5.0.2                      |
     |                                                        | * replace leiden by leidenbase                       |
     +--------------------------------------------------------+------------------------------------------------------+
     |                                                        | Update packages:                                     |
     |                                                        |                                                      |
     | For R/4.4.2                                            | * Seurat to version 5.3.0                            |
     |                                                        | * SeuratObject to version 5.0.2                      |
     |                                                        | * replace leiden by leidenbase                       |
     +--------------------------------------------------------+------------------------------------------------------+
     | geos/3.8.1                                             | Replaced by geos/3.8.1/gcc.8.4.0                     |
     |                                                        |                                                      |
     | geos/3.10.2                                            | Replaced by geos/3.10.2/gcc.11.2.0                   |
     |                                                        |                                                      |
     | geos/3.11.1                                            | Replaced by geos/3.11.1/gcc.11.2.0                   |
     +--------------------------------------------------------+------------------------------------------------------+
     | sqlite3/3.32.3                                         | Replaced by sqlite3/3.32.3/gcc.8.4.0                 |
     |                                                        |                                                      |
     | sqlite3/3.38.2                                         | Replaced by sqlite3/3.38.2/gcc.11.2.0                |
     |                                                        |                                                      |
     | sqlite3/3.41.0                                         | Replaced by sqlite3/3.41.0/gcc.11.2.0                |
     +--------------------------------------------------------+------------------------------------------------------+
     | proj/6.3.2                                             | Replaced by proj/6.3.2/gcc.8.4.0                     |
     |                                                        |                                                      |
     | proj/9.0.0                                             | Replaced by proj/9.0.0/gcc.11.2.0                    |
     |                                                        |                                                      |
     | proj/9.1.1/gcc.11.2.0                                  | Replaced by proj/9.1.1/gcc.11.2.0                    |
     +--------------------------------------------------------+------------------------------------------------------+
     | gdal/3.1.0                                             | Replaced by gdal/3.1.0/gcc.8.4.0                     |
     |                                                        |                                                      |
     | gdal/3.4.1                                             | Replaced by gdal/3.4.1/gcc.11.2.0                    |
     |                                                        |                                                      |
     | gdal/3.6.2                                             | Replaced by gdal/3.6.2/gcc.11.2.0                    |
     +--------------------------------------------------------+------------------------------------------------------+
     | **go** is no longer provided by gcc                    | Load  module  go/1.22.3 if need **go**               |
     +--------------------------------------------------------+------------------------------------------------------+
     | gcc/system                                             | System compiler is updated to version 11.5.0.        |
     |                                                        |                                                      |
     |                                                        | Modules compiled with sysem compiler:                |
     |                                                        |                                                      |
     |                                                        | * openmpi/4.1.1/gcc.system                           |
     |                                                        | * ucx/1.8.0/gcc.system                               |
     |                                                        | * ucx/1.12.0/gcc.system                              |
     |                                                        | * ucx/1.15.0/gcc.system                              |
     |                                                        | * fftw/3.3.8/gcc.system                              |
     |                                                        | * hdf5/1.10.5/gcc.system                             |
     |                                                        | * hdf5/1.13.1/gcc.system                             |
     |                                                        | * hdf5/1.13.1/gcc.system-openmpi.4.1.1               |
     +--------------------------------------------------------+------------------------------------------------------+
     | intel/2020u1                                           | Does not work, removed.                              |
     |                                                        |                                                      |
     |                                                        | Removed affected modules:                            |
     |                                                        |                                                      |
     |                                                        | * mpich/3.4/intel.2020u1                             |
     |                                                        | * openmpi/4.0.3/intel.2020u1                         |
     |                                                        | * hdf5/1.10.5/intel.2020u1                           |
     |                                                        | * ioapi/3.2/intel.2020u1                             |
     |                                                        | * netcdf-c/4.7.0/intel.2020u1 (including             |
     |                                                        |   dependent netcdf-f version 4.5.2)                  |
     +--------------------------------------------------------+------------------------------------------------------+
     | intel-tbb/2021.5.0                                     | Replaced by  intel-tbb/2021.11                       |
     +--------------------------------------------------------+------------------------------------------------------+
     | intel-tbb/2022.1                                       | Added                                                |
     +--------------------------------------------------------+------------------------------------------------------+
     | intel/2025.1.0                                         | Added                                                |
     +--------------------------------------------------------+------------------------------------------------------+
     | cuda/10.1.243                                          | Not supported, removed.                              |
     +--------------------------------------------------------+------------------------------------------------------+
     | Modules compiled with CUDA 10:                         | Replaced by modules compiled with CUDA 11:           |
     |                                                        |                                                      |
     | * gromacs/2020.4/gcc.8.4.0-cuda.10.1.243               | * gromacs/2020.4/gcc.8.4.0-cuda.11.7.1               |  
     | * gromacs/2021.2/gcc.8.4.0-cuda.10.1.243               | * gromacs/2021.2/gcc.8.4.0-cuda.11.7.1               |  
     | * gromacs/2021.2/gcc.8.4.0-cuda.10.1.243.openmpi.4.0.3 | * gromacs/2021.2/gcc.8.4.0-cuda.11.7.1.openmpi.4.0.3 |
     | * namd/2.14b2/gcc.8.4.0-cuda.10.1.243                  | * namd/2.14b2/gcc.8.4.0-cuda.11.7.1                  |
     +--------------------------------------------------------+------------------------------------------------------+
     | tensorflow/2.0.0                                       | Not supported, removed.                              |
     +--------------------------------------------------------+------------------------------------------------------+
     | tensorRT/6.0.1.5                                       | Not supported, removed.                              |
     +--------------------------------------------------------+------------------------------------------------------+
     | hdf5/1.14.1/gcc.11.2.0-openmpi.5.0.1                   | Added                                                |
     +--------------------------------------------------------+------------------------------------------------------+
     | mpich/4.0/gcc.11.2.0                                   | Replaced by mpich/4.0/gcc.system                     |
     +--------------------------------------------------------+------------------------------------------------------+

After the maintenance:
  * :red:`User compiled and installed software will need to be reinstalled`. 
  * User installed conda environments will VERY LIKELY need to be reinstalled.
  * If you previously used a module that has been removed, try to use a newer version of it where available.

