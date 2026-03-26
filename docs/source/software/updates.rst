.. _software updates:

Updates with OS changes
=======================

This page lists changes that are a result of the :underline:`Operating System
upgrade`.

.. _rocky 9.7 updates:

:section:`Rocky Linux 9.7 updates`

.. important:: | HPC3 operating system is **Rocky Linux 9.7** (as of March 24, 2026).
               | All installed software is compiled specifically for this OS.

The operating system update involves many changes across the software stack.
While we try to build all the previous software versions for the new OS, some builds are
impossible. As a result: 

:bluelight:`For user compiled or installed software`
  1. If you compiled any software packages yourself using :tt:`gcc`, :tt:`intel`,
     :tt:`openmpi` modules and your compiled software no longer works as before
     you will have to recompile it anew.
  2. Some commands, include files and libraries are available from system RPMs
     and do not require modules. If you compiled any software using such
     libraries/binaries you may need to recompile anew as many have changed.
  3. User installed anaconda/miniconda/mamba environments will VERY LIKELY need to be reinstalled.
     In this case, please try to use the latest version of :tt:`anaconda` or :tt:`miniconda` modules that we provide. Please see
     :ref:`install  conda` user guide that explains how to build and use conda environments on HPC3.
  4. If you previously used a module that has been removed, you will need to use a newer version of it where available.

:bluelight:`Summary of changes`
  Modules availability on the previous :tt:`Rocky Linux 9.6` and on the current :tt:`Rocky Linux 9.7` operating systems:

  .. table::
     :class: noscroll-table

     +-----------+------------------+------------------+---------------------------+
     | Total     | Rocky Linux 9.6  | Rocky Linux 9.7  | Comment                   |
     +===========+==================+==================+===========================+
     | Installed | 310              | 360              | active modules            |
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
  
       +--------------------------------------------------------+----------+
       | Module name                                            | Comments |
       +========================================================+==========+
       | anaconda/2025.12                                       | Added    |
       +--------------------------------------------------------+----------+
       | boost/1.90.0/gcc.15.2.0                                | Added    |
       +--------------------------------------------------------+----------+
       | clang/20.1.8                                           | Added    |
       +--------------------------------------------------------+----------+
       | cmake/4.2.3                                            | Added    |
       +--------------------------------------------------------+----------+
       | cuda/13.0.1                                            | Added    |
       +--------------------------------------------------------+----------+
       | eigen/5.0.1                                            | Added    |
       +--------------------------------------------------------+----------+
       | ffmpeg/8.0.1                                           | Added    |
       +--------------------------------------------------------+----------+
       | ffnvcodec/13.0.19.0                                    | Added    |
       +--------------------------------------------------------+----------+
       | fftw/3.3.10/gcc.15.2.0                                 | Added    |
       +--------------------------------------------------------+----------+
       | fftw/3.3.10/gcc.15.2.0-openmpi.5.0.9                   | Added    |
       +--------------------------------------------------------+----------+
       | gcc/15.2.0                                             | Added    |
       +--------------------------------------------------------+----------+
       | gdal/3.12.1/gcc.15.2.0                                 | Added    |
       +--------------------------------------------------------+----------+
       | gdrcopy/2.5.1                                          | Added    |
       +--------------------------------------------------------+----------+
       | geos/3.14.1/gcc.15.2.0                                 | Added    |
       +--------------------------------------------------------+----------+
       | glpk/5.0/gcc.15.2.0                                    | Added    |
       +--------------------------------------------------------+----------+
       | gsl/2.8/gcc.15.2.0                                     | Added    |
       +--------------------------------------------------------+----------+
       | julia/1.12.4                                           | Added    |
       +--------------------------------------------------------+----------+
       | libgit2/1.8.5                                          | Added    |
       +--------------------------------------------------------+----------+
       | llvm/20.1.8                                            | Added    |
       +--------------------------------------------------------+----------+
       | mamba/26.1.0                                           | Added    |
       +--------------------------------------------------------+----------+
       | miniconda3/25.11.1                                     | Added    |
       +--------------------------------------------------------+----------+
       | mkl/2025.1.0                                           | Added    |
       +--------------------------------------------------------+----------+
       | OpenBLAS/0.3.31                                        | Added    |
       +--------------------------------------------------------+----------+
       | openmpi/5.0.9/gcc.15.2.0                               | Added    |
       +--------------------------------------------------------+----------+
       | openmpi/5.0.9/gcc.15.2.0-cuda.13.0.1                   | Added    |
       +--------------------------------------------------------+----------+
       | proj/9.7.1/gcc.15.2.0                                  | Added    |
       +--------------------------------------------------------+----------+
       | python/3.14.3                                          | Added    |
       +--------------------------------------------------------+----------+
       | qiime2/2025.10                                         | Added    |
       +--------------------------------------------------------+----------+
       | R/4.5.2                                                | Added    |
       +--------------------------------------------------------+----------+
       | sqlite3/3.51.0/gcc.15.2.0                              | Added    |
       +--------------------------------------------------------+----------+
       | ucx/1.20.0                                             | Added    |
       +--------------------------------------------------------+----------+
       | ucx/1.20.0-cuda.13.0.1                                 | Added    |
       +--------------------------------------------------------+----------+

.. See previous updates details on system and user install software

    * :ref:`Rocky 9.6 updates <rocky 9.6 updates>`

