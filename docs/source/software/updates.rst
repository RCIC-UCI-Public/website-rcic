.. _software updates:

Updates with OS changes
=======================

This page lists changes that are a result of the :underline:`Operating System
upgrade`.

.. _rocky updates:

:section:`Rocky Linux 8.10 updates`

.. important:: | HPC3 operating system is **Rocky Linux 8.10** (as of December 18, 2024).
               | All installed software is compiled specifically for this OS.

:bluelight:`For user compiled or installed software`
  1. If you compiled any software packages yourself using :tt:`gcc`, :tt:`intel`,
     :tt:`openmpi` modules and your compiled software no longer works as before
     you may have to recompile it anew.
  2. Some commands, include files and libraries are available from system RPMs
     and do not require modules. If you compiled any software using such
     libraries/binaries you may need to recompile anew as some have changed.
  3. If you installed any packages with :tt:`anaconda` or :tt:`miniconda`, you may 
     need to reinstall them. In this case, please try to use the latest version of
     :tt:`anaconda` or :tt:`miniconda` modules that we provide. Please see
     :ref:`install  conda` user guide that explains how to build and use conda environments on HPC3.
  
     :red:`IMPORTANT:` if you are currently using :tt:`miniconda/4.8.5` and :tt:`miniconda3/4.12.0`
     please follow :ref:`update miniconda3`.

:bluelight:`Summary of changes`
  Modules availability on the previous :tt:`Rocky Linux 8.8` and on the current :tt:`Rocky Linux 8.10` operating systems:

  .. table::
     :class: noscroll-table

     +-----------+-----------------+------------------+---------------------------+
     | Total     | Rocky Linux 8.8 | Rocky Linux 8.10 | Comment                   |
     +===========+=================+==================+===========================+
     | Installed | 330             | 330              | active modules            |
     +-----------+-----------------+------------------+---------------------------+

  * A few modules were removed because they cannot be built on a new operating system.
  * Some modules were removed because they were unused. Usually a  newer version is available.
  * ``screen`` command  is not available, use ``tmux``.
  * Operating system provides default compiler :tt:`gcc 8.5.0` and :tt:`openmpi 4.1.1`
    which are available via modules:

    ============== ========================
    Package        Module
    ============== ========================
    gcc 8.5.0      gcc.system
    openmpi 4.1.1  openmpi/4.1.1/gcc.system
    ============== ========================
  * :tt:`foundation/v8` module is available for backwards
    compatibility. It will simply load a few other modules
    to provide an access to the commonly used tools. If you are using
    a specific tool from the current :tt:`foundation/v8` you will be able to switch
    to using the specific module for that tool
    (see output of ``module display foundation/v8`` to list loaded modules).
  * :tt:`sra-tools` prior to v.3 do not handle writing temp files to a
    separate directory and  are removed as they cause issues. Please see
    :ref:`job sra` for explanation how to use this toolkit with currently available version.
  * :tt:`Python 2.7` has reached the end of life and is no longer supported.
    It is installed but the outcome of any program can not be predicted.
    **If you have any python code that is still using python 2 convert your code to
    Python 3**. Test your application with the :tt:`-W` default command-line option
    to see any deprecation warnings and follow online guides (google) for porting
    Python 2 to Python 3.
  * :tt:`singulariy 3.4.1` built containers may fail with an error that looks like:

    .. code-block:: text

       FATAL: container creation failed: mount /proc/

    Please try to use the newer singularity module and add option ``-B`` to your command:

    .. code-block:: console

       [user@login-x:~]$ module load singularity/3.9.4
       [user@login-x:~]$ singularity exec \
                         -B /dfs8/singularity_containers/rcic/bashrc:/etc/bashrc \
                         /dfs3a/singularity_containers/contName.simg binaryName
  * The :tt:`intel` and :tt:`mkl` modules provide access to a number of Intel Math Kernel Libraries
    including LAPACK, ScaLAPACK, BLAS and threading options.

    The MKL libraries can be linked with Intel or GNU compilers. If you are compiling software yourself and are using :tt:`intel` or :tt:`mkl`
    modules please see `Intel MKL Documentation <https://software.intel.com/en-us/mkl/documentation/view-all>`_
    and `Intel MKL Link Advisory <https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html#gs.o9qcu1>`_
    to help you figure out how to use variables set by them.
  
