.. _software updates:

Updates with OS changes
=======================

This page lists changes that are a result of the :underline:`Operating System
upgrade`.

.. _rocky 9.6 updates:

:section:`Rocky Linux 9.6 updates`

.. important:: | HPC3 operating system is **Rocky Linux 9.6** (as of July 29, 2025).
               | All installed software is compiled specifically for this OS.

The operating system update involves many changes across the software stack.
While we try to build all the previous software versions for the new OS, some builds are
impossible. As a result: 

  * Some modules were removed because they cannot be built on a new system as
    the underlying requirements are no longer satisfied.
  * Some modules were removed because they were unused. Where possible, a newer version is available.
  
:bluelight:`For user compiled or installed software`
  1. :red:`User compiled and installed software will need to be recompiled and reinstalled`.
     If you compiled any software packages yourself using :tt:`gcc`, :tt:`intel`,
     :tt:`openmpi` modules and your compiled software no longer works as before
     you will have to recompile it anew.
  2. Some commands, include files and libraries are available from system RPMs
     and do not require modules. If you compiled any software using such
     libraries/binaries you may need to recompile anew as many have changed.
  3. User installed anaconda/miniconda/mamaba environments will VERY LIKELY need to be reinstalled.
     In this case, please try to use the latest version of :tt:`anaconda` or :tt:`miniconda` modules that we provide. Please see
     :ref:`install  conda` user guide that explains how to build and use conda environments on HPC3.
  4. If you previously used a module that has been removed, you will need to use a newer version of it where available.

:bluelight:`Summary of changes`
  Modules availability on the previous :tt:`Rocky Linux 8.10` and on the current :tt:`Rocky Linux 9.6` operating systems:

  .. table::
     :class: noscroll-table

     +-----------+------------------+------------------+---------------------------+
     | Total     | Rocky Linux 8.10 | Rocky Linux 9.6  | Comment                   |
     +===========+==================+==================+===========================+
     | Installed | 330              | 310              | active modules            |
     +-----------+------------------+------------------+---------------------------+

  Operating system provides default **gcc** and **openmpi**
  which are available via modules:

  ============== ========================
  Version        Module
  ============== ========================
  gcc 11.5.0     gcc/system
  openmpi 4.1.1  openmpi/4.1.1/gcc.system
  ============== ========================

:bluelight:`Software changes details`
    .. table:: **Software changes**
       :align: center
       :class: noscroll-table
       :widths: 50,50
  
       +--------------------------------------------------------+------------------------------------------------------+
       | Module name                                            | Comments                                             |
       +========================================================+======================================================+
       |                  .. centered:: :blue:`Removed modules`                                                        |
       +--------------------------------------------------------+------------------------------------------------------+
       | bcftools/1.10.2                                        | Cannot build, use newer version                      |
       +--------------------------------------------------------+------------------------------------------------------+
       | bustools/0.40.0                                        | Unused, use newer version                            |
       +--------------------------------------------------------+------------------------------------------------------+
       | canu/2.0                                               | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | charm/6.10.1/gcc.11.2.0                                | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | charm/6.10.1/gcc.11.2.0-openmpi.5.0.1                  | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | charm/7.0.0/gcc.11.2.0                                 | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | cuda/10.1.243                                          | Not supported on Rocky 9, use newer version          |
       +--------------------------------------------------------+------------------------------------------------------+
       | gatk/4.1.9.0                                           | Security vulnerability, use newer version            |
       +--------------------------------------------------------+------------------------------------------------------+
       | gromacs/2021.2/gcc.8.4.0-cuda.10.1.243.openmpi.4.0.3   | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | gromacs/2022.1/gcc.8.4.0-openmpi.4.1.2                 | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | intel/2020u1                                           | This Intel compiler deoends on a shared library      |
       |                                                        | that is unavailable on Rocky 9.                      |
       |                                                        |                                                      |
       |                                                        | The following affected modules are removed:          |
       |                                                        |                                                      |
       |                                                        | * mpich/3.4/intel.2020u1                             |
       |                                                        | * openmpi/4.0.3/intel.2020u1                         |
       |                                                        | * hdf5/1.10.5/intel.2020u1                           |
       |                                                        | * ioapi/3.2/intel.2020u1                             |
       |                                                        | * netcdf-c/4.7.0/intel.2020u1 (including             |
       |                                                        |   dependent netcdf-f version 4.5.2)                  |
       |                                                        |                                                      |
       |                                                        | Use modules with newer intel compier where available |
       +--------------------------------------------------------+------------------------------------------------------+
       | ioapi/3.2/gcc.11.2.0                                   | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | petsc/3.20.1/gcc.11.2.0                                | Unused                                               |
       |                                                        |                                                      |
       | petsc/3.20.1/gcc.11.2.0-cuda.11.7.1                    | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | protobuf/3.11.4                                        | Unused                                               |
       |                                                        |                                                      |
       | protobuf/3.19.4                                        | Unused                                               |
       +--------------------------------------------------------+------------------------------------------------------+
       | salmon/1.2.1                                           | Cannot build, use newer version                      |
       +--------------------------------------------------------+------------------------------------------------------+
       | tensorflow/2.0.0                                       | Cannot build, use newer version                      |
       +--------------------------------------------------------+------------------------------------------------------+
       | tensorRT/6.0.1.5                                       | Cannot build, use newer version                      |
       +--------------------------------------------------------+------------------------------------------------------+
       | tk/8.6.12                                              | Unused. Functionality is provided by tcl/8.6.12      |
       +--------------------------------------------------------+------------------------------------------------------+
       |                  .. centered:: :blue:`Updated modules`                                                        |
       +--------------------------------------------------------+------------------------------------------------------+
       | CUDA 10 compiled modules:                              | Replaced by CUDA 11 compiled modules:                |
       |                                                        |                                                      |
       | * gromacs/2020.4/gcc.8.4.0-cuda.10.1.243               | * gromacs/2020.4/gcc.8.4.0-cuda.11.7.1               |
       | * gromacs/2021.2/gcc.8.4.0-cuda.10.1.243               | * gromacs/2021.2/gcc.8.4.0-cuda.11.7.1               |
       | * gromacs/2021.2/gcc.8.4.0-cuda.10.1.243.openmpi.4.0.3 | * gromacs/2021.2/gcc.8.4.0-cuda.11.7.1.openmpi.4.0.3 |
       | * namd/2.14b2/gcc.8.4.0-cuda.10.1.243                  | * namd/2.14b2/gcc.8.4.0-cuda.11.7.1                  |
       +--------------------------------------------------------+------------------------------------------------------+
       | gcc/<any version>                                      | No longer provides **go**.                           |
       |                                                        | To use **go** please load module go/1.22.3           |
       +--------------------------------------------------------+------------------------------------------------------+
       | gcc/system                                             | System default compiler is updated to version 11.5.0.|
       |                                                        |                                                      |
       |                                                        | Modules compiled with system compiler:               |
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
       | openmpi/4.1.1/gcc.system                               | System default openmpi compiled with gcc 11.5.0      |
       +--------------------------------------------------------+------------------------------------------------------+
       | gdal/3.1.0                                             | Replaced by gdal/3.1.0/gcc.8.4.0                     |
       |                                                        |                                                      |
       | gdal/3.4.1                                             | Replaced by gdal/3.4.1/gcc.11.2.0                    |
       |                                                        |                                                      |
       | gdal/3.6.2                                             | Replaced by gdal/3.6.2/gcc.11.2.0                    |
       +--------------------------------------------------------+------------------------------------------------------+
       | geos/3.8.1                                             | Replaced by geos/3.8.1/gcc.8.4.0                     |
       |                                                        |                                                      |
       | geos/3.10.2                                            | Replaced by geos/3.10.2/gcc.11.2.0                   |
       |                                                        |                                                      |
       | geos/3.11.1                                            | Replaced by geos/3.11.1/gcc.11.2.0                   |
       +--------------------------------------------------------+------------------------------------------------------+
       | intel-tbb/2021.5.0                                     | Replaced by intel-tbb/2021.11                        |
       +--------------------------------------------------------+------------------------------------------------------+
       | mpich/4.0/gcc.11.2.0                                   | Replaced by mpich/4.0/gcc.system                     |
       +--------------------------------------------------------+------------------------------------------------------+
       | proj/6.3.2                                             | Replaced by proj/6.3.2/gcc.8.4.0                     |
       |                                                        |                                                      |
       | proj/9.0.0                                             | Replaced by proj/9.0.0/gcc.11.2.0                    |
       |                                                        |                                                      |
       | proj/9.1.1                                             | Replaced by proj/9.1.1/gcc.11.2.0                    |
       +--------------------------------------------------------+------------------------------------------------------+
       | sqlite3/3.32.3                                         | Replaced by sqlite3/3.32.3/gcc.8.4.0                 |
       |                                                        |                                                      |
       | sqlite3/3.38.2                                         | Replaced by sqlite3/3.38.2/gcc.11.2.0                |
       |                                                        |                                                      |
       | sqlite3/3.41.0                                         | Replaced by sqlite3/3.41.0/gcc.11.2.0                |
       +--------------------------------------------------------+------------------------------------------------------+
       | R/4.1.2                                                | **Seurat** and **leiden** libraries cannot be        |
       |                                                        | built. Use newer R if you need these specific        |
       | R/4.2.2                                                | packages.                                            |
       +--------------------------------------------------------+------------------------------------------------------+
       |                                                        | Updated packages:                                    |
       |                                                        |                                                      |
       | R/4.3.3                                                | * **Seurat** to version 5.3.0                        |
       |                                                        | * **SeuratObject** to version 5.0.2                  |
       | R/4.4.2                                                | * replace **leiden** by **leidenbase**               |
       +--------------------------------------------------------+------------------------------------------------------+
       |                  .. centered:: :blue:`New modules`                                                            |
       +--------------------------------------------------------+------------------------------------------------------+
       | gatk/4.6.2.0                                           | Added                                                |
       +--------------------------------------------------------+------------------------------------------------------+
       | hdf5/1.14.1/gcc.11.2.0-openmpi.5.0.1                   | Added                                                |
       +--------------------------------------------------------+------------------------------------------------------+
       | intel/2025.1.0                                         | Added                                                |
       +--------------------------------------------------------+------------------------------------------------------+
       | intel-tbb/2022.1                                       | Added (subset of Intel 2025 compiler)                |
       +--------------------------------------------------------+------------------------------------------------------+
