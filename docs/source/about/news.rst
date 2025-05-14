
.. _news:

News & Events
=============

* General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
* Any additional information is outlined in notification emails to hpc-users@uci.edu
  (all current users) and is described in the details below.
* When the maintenance is completed all users are notified via emails to hpc-users@uci.edu.

July TBD
--------

| :blogtitle:`HPC3 Downtime July TBD, 2025`
| :blogauthor:`2025-05-13 by Nadya Williams`

| The next outage will be In July (date to be determined), 2025, beginning at 8am.
| The cluster will be unavailable for most of the day.

Maintenance Items:
  1. OS version update from **Rocky 8.10 to Rocky 9**.
  #. Top-to-bottom re-installation of all compute and login nodes.
  #. Full rebuild of all software, see table below for software changes.

Impacts:
  This is a full outage.

  #. All existing logins will be terminated.
  #. You will NOT have access to HPC3 during the planned downtime.
  #. You will have access to CRSP using `Web based File browser` or `CRSP Desktop App`.
  #. No Slurm jobs can run or remain in the queue.
  #. :red:`All jobs remaining in the queue on the maintenance day will be terminated`.
  #. Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on the day of maintenance
     will need to be submitted after the maintenance.
     Please see :ref:`requesting time limits <request time>` on queues.

Software changes:
  The operating system update involves many changes across the software stack.
  While we try to build all the software for the new OS, some builds are
  impossible and some applications may not behave the same even if they are built
  without errors.

  Some modules will be removed because they cannot be built on a new system or because
  the underlying requirements are no longer satisfied.

  *Note, the table below will be periodically updated till the maintenance date*.

  .. table:: **Software changes**
     :align: center
     :class: noscroll-table

     +--------------------------------------+----------------------------------------+
     | Module                               | Comments                               |
     +======================================+========================================+
     | salmon/1.2.1                         | cannot build, removed                  |
     +--------------------------------------+----------------------------------------+
     | bcftools/1.10.2                      | cannot build, use newer version        |
     +--------------------------------------+----------------------------------------+
     | Seurat module in R/4.1.2             | cannot build, use newer R              |
     +--------------------------------------+----------------------------------------+
     | Seurat module in R/4.2.2             | cannot build, use newer R              |
     +--------------------------------------+----------------------------------------+
     | Seurat module in R/4.3.3             | update to version 5.3.0                |
     |                                      |                                        |
     | SeuratObject module in R/4.3.3       | update to version 5.0.2                |
     +--------------------------------------+----------------------------------------+
     | Seurat module in R/4.4.2             | update to version 5.3.0                |
     |                                      |                                        |
     | SeuratObject module in R/4.4.2       | update to version 5.0.2                |
     +--------------------------------------+----------------------------------------+
     | geos/3.8.1                           | replaced by geos/3.8.1/gcc.8.4.0       |
     |                                      |                                        |
     | geos/3.10.2                          | replaced by geos/3.10.2/gcc.11.2.0     |
     |                                      |                                        |
     | geos/3.11.1                          | replaced by geos/3.11.1/gcc.11.2.0     |
     +--------------------------------------+----------------------------------------+
     | sqlite3/3.32.3                       | replaced by sqlite3/3.32.3/gcc.8.4.0   |
     |                                      |                                        |
     | sqlite3/3.38.2                       | replaced by sqlite3/3.38.2/gcc.11.2.0  |
     |                                      |                                        |
     | sqlite3/3.41.0                       | replaced by sqlite3/3.41.0/gcc.11.2.0  |
     +--------------------------------------+----------------------------------------+
     | proj/6.3.2                           | replaced by proj/6.3.2/gcc.8.4.0       |
     |                                      |                                        |
     | proj/9.0.0                           | replaced by proj/9.0.0/gcc.11.2.0      |
     |                                      |                                        |
     | proj/9.1.1/gcc.11.2.0                | replaced by proj/9.1.1/gcc.11.2.0      |
     +--------------------------------------+----------------------------------------+
     | gdal/3.1.0                           | replaced by gdal/3.1.0/gcc.8.4.0       |
     |                                      |                                        |
     | gdal/3.4.1                           | replaced by gdal/3.4.1/gcc.11.2.0      |
     |                                      |                                        |
     | gdal/3.6.2                           | replaced by gdal/3.6.2/gcc.11.2.0      |
     +--------------------------------------+----------------------------------------+
     | gcc/system                           | compiler version is now 11.5.0.        |
     |                                      |                                        |
     |                                      | This affects modules:                  |
     |                                      |                                        |
     |                                      | * openmpi/4.1.1/gcc.system             |
     |                                      | * ucx/1.8.0/gcc.system                 |
     |                                      | * ucx/1.15.0/gcc.system                |
     |                                      | * ucx/1.15.0/gcc.system                |
     |                                      | * fftw/3.3.8/gcc.system                |
     |                                      | * hdf5/1.10.5/gcc.system               |
     |                                      | * hdf5/1.13.1/gcc.system               |
     |                                      | * hdf5/1.13.1/gcc.system-openmpi.4.1.1 |
     +--------------------------------------+----------------------------------------+
     | intel/2020u1                         | removed, does not work.                |
     |                                      |                                        |
     |                                      | Removed affected modules:              |
     |                                      |                                        |
     |                                      | * mpich/3.4/intel.2020u1               |
     |                                      | * openmpi/4.0.3/intel.2020u1           |
     |                                      | * hdf5/1.10.5/intel.2020u1             |
     |                                      | * ioapi/3.2/intel.2020u1               |
     |                                      | * netcdf-c/4.7.0/intel.2020u1          |
     +--------------------------------------+----------------------------------------+
     | **go** is no longer provided by gcc  | load  module  go/1.22.3 if need **go** |
     +--------------------------------------+----------------------------------------+

After the maintenance:
  * :red:`User compiled and installed software will need to be reinstalled`. 
  * User installed conda environments will LIKELY need to be reinstall.

