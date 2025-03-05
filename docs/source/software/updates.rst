.. _software updates:

Software and modules updates
============================

This page lists specific software and modules changes that are a result of the Operating System update.

Please see :ref:`modules` to learn how to use software modules, including
how to to see the most recent software versions and availability.

General Info
------------

.. important:: | HPC3 operating system is **Rocky Linux 8.8** (as of July 25, 2023).
               | All installed software is compiled specifically for this OS.

* ``docker`` is not available per security vulnerability. Use *singularity* instead.
* ``sudo`` and ``su`` are not available to regular users per security vulnerability.
* ``screen`` command  is not available, use ``tmux``.
* Operating system provides default compiler :tt:`gcc 8.5.0` and :tt:`openmpi 4.1.1`
  which are available via modules:

  ============== ========================
  Package        Module
  ============== ========================
  gcc 8.5.0      gcc.system
  openmpi 4.1.1  openmpi/4.1.1/gcc.system
  ============== ========================
* The :tt:`intel` and :tt:`mkl` modules provide access to a number of Intel Math Kernel Libraries
  including LAPACK, ScaLAPACK, BLAS and threading options. The MKL libraries can be linked with Intel
  or GNU compilers. If you are compiling software yourself and are using :tt:`intel` or :tt:`mkl`
  modules please see `Intel MKL Documentation <https://software.intel.com/en-us/mkl/documentation/view-all>`_
  and `Intel MKL Link Advisory <https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html#gs.o9qcu1>`_
  to help you figure out how to use variables set by them.

.. _rocky8.8 updates:

Rocky Linux 8.8 updates
-----------------------

Operating System:
  | HPC3 operating system is **Rocky Linux 8.8** (as of July 25, 2023).
  | All installed software is compiled specifically for this OS.

**For user compiled or installed software**:

1. If you compiled any software packages yourself using :tt:`gcc`, :tt:`intel`,
   :tt:`openmpi` modules you may  have to recompile your packages anew if your
   software no longer works as before.
2. Some commands, include files and libraries are available from system RPMs
   and do not require modules. If you compiled any software using such
   libraries/binaries you may need to recompile anew as some have changed with the new OS.
3. If you installed any packages with :tt:`anaconda` or :tt:`miniconda`, it is possible you will
   need to reinstall them. In this case, please try to use the latest version of
   :tt:`anaconda` or :tt:`miniconda` modules that we provide. Please see
   :ref:`install  conda` user guide that explains how to build and use conda environments on HPC3.

**Summary of changes**

The following table summarizes the modules availability on
the previous :tt:`Rocky Linux 8.6` and on the current :tt:`Rocky Linux 8.8` operating systems:

.. table::
   :class: noscroll-table

   +-----------+-----------------+-----------------+---------------------------+
   | Total     | Rocky Linux 8.6 | Rocky Linux 8.8 | Comment                   |
   +===========+=================+=================+===========================+
   | Installed | 333             | 330             | active modules            |
   +-----------+-----------------+-----------------+---------------------------+
   | Removed   |                 | 24              | unused                    |
   +-----------+-----------------+-----------------+---------------------------+
   | New       |                 | 21              | latest available version  |
   +-----------+-----------------+-----------------+---------------------------+


**Detailed Changes**

Please use the table below to find out changes
in modules availability for :tt:`Rocky Linux 8.8`.
See notes after the table for a few specific cases.

.. table::
   :class: noscroll-table sortable

   +-------------------------------------------------------------------+-------------------------------------+
   | Removed modules                                                   | Added modules                       |
   +===================================================================+=====================================+
   | bamtools/2.5.1                                                    | awscli/2.11.21                      |
   +-------------------------------------------------------------------+-------------------------------------+
   | bracken/2.6.0                                                     | bowtie2/2.5.1                       |
   +-------------------------------------------------------------------+-------------------------------------+
   | gromacs/2020.4/gcc.8.4.0-cuda.10.1.243.openmpi.4.0.3              | cellranger-arc/2.0.2                |
   +-------------------------------------------------------------------+-------------------------------------+
   | gromacs/2020.4/gcc.8.4.0-cuda.10.1.243.openmpi.4.0.3.plumed.2.6.1 | charm/6.10.1/gcc.8.4.0-openmpi.4.0.3|
   +-------------------------------------------------------------------+-------------------------------------+
   | gromacs/2020.4/gcc.8.4.0-openmpi.4.0.3                            | cudasdk/22.9                        |
   +-------------------------------------------------------------------+-------------------------------------+
   | icu/65.1                                                          | gdal/3.6.2                          |
   +-------------------------------------------------------------------+-------------------------------------+
   | igv/2.8.9                                                         | geos/3.11.1                         |
   +-------------------------------------------------------------------+-------------------------------------+
   | jsoncpp/1.9.4                                                     | go/1.20.4                           |
   +-------------------------------------------------------------------+-------------------------------------+
   | julia/1.5.1                                                       | hdf5/1.13.1/cudasdk.22.9            |
   +-------------------------------------------------------------------+-------------------------------------+
   | kraken2/2.1.1                                                     | hdf5/1.14.1/gcc.11.2.0              |
   +-------------------------------------------------------------------+-------------------------------------+
   | mdtraj/1.9.3                                                      | hdf5/1.14.1/gcc.11.2.0-openmpi.4.1.2|
   +-------------------------------------------------------------------+-------------------------------------+
   | mdtraj/1.9.7                                                      | OpenBLAS/0.3.21                     |
   +-------------------------------------------------------------------+-------------------------------------+
   | meme/5.2.0                                                        | proj/9.1.1                          |
   +-------------------------------------------------------------------+-------------------------------------+
   | midas/1.3.2                                                       | qe/7.1/gcc.11.2.0-openmpi.4.1.2     |
   +-------------------------------------------------------------------+-------------------------------------+
   | minimap2/2.17                                                     | R/4.2.2                             |
   +-------------------------------------------------------------------+-------------------------------------+
   | mummer/4.0.0                                                      | rstudio/2022.12.0.353               |
   +-------------------------------------------------------------------+-------------------------------------+
   | pilon/1.23                                                        | singularity/3.11.3                  |
   +-------------------------------------------------------------------+-------------------------------------+
   | plumed/2.6.1/gcc.8.4.0-openmpi.4.0.3                              | sqlite3/3.41.0                      |
   +-------------------------------------------------------------------+-------------------------------------+
   | racon/1.4.13                                                      | sra-tools/3.0.0                     |
   +-------------------------------------------------------------------+-------------------------------------+
   | rMATS/4.1.0                                                       | vasp/6.3.2/cudasdk.22.9             |
   +-------------------------------------------------------------------+-------------------------------------+
   | sas/94M7                                                          | vasp/6.3.2/gcc.11.2.0               |
   +-------------------------------------------------------------------+-------------------------------------+
   | sra-tools/2.10.9                                                  |                                     |
   +-------------------------------------------------------------------+-------------------------------------+
   | sra-tools/2.11.3                                                  |                                     |
   +-------------------------------------------------------------------+-------------------------------------+
   | unicycler/0.4.8                                                   |                                     |
   +-------------------------------------------------------------------+-------------------------------------+

**Notes**

* :tt:`sra-tools` tools prior to v.3 do not handle writing temp files to a
  separate directory and  are removed as they cause issues. Please see
  :ref:`job sra` for explanation how to use this toolkit with currently available version.
* :tt:`Python 2.7` has reached the end of life and is no longer supported.
  It is installed but the outcome of any program can not be predicted.
  **If you have any python code that is still using python 2 convert your code to
  Python 3**. Test your application with the :tt:`-W` default command-line option
  to see any deprecation warnings and follow online guides (google) for porting
  Python 2 to Python 3.
* :tt:`Cufflinks` does not work under Rocky Linux 8. Use a singularity container build with Cufflinks compiled for CentOS 7.
  The image **/dfs8/singularity-images/cufflinks.simg** is build with **singularity/3.7.2**.
  Example of usage:

  .. code-block:: console

     [user@login-x:~]$ module load singularity/3.7.2
     [user@login-x:~]$ singularity exec \
                          /dfs8/singularity-images/cufflinks.simg cuffdiff arg1 ... argN

* If you are using an older container built with **singulariy 3.4.1**,
  and it fails with an error that looks like

  .. code-block:: text

     FATAL: container creation failed: mount /proc/

  Please try adding option ``-B`` to your singularity command and use the latest singularity module:

  .. code-block:: console

     [user@login-x:~]$ module load singularity/3.9.4
     [user@login-x:~]$ singularity exec \
                          -B /dfs8/singularity_containers/rcic/bashrc:/etc/bashrc \
                          /dfs3a/singularity_containers/contName.simg binaryName
