.. _software updates:

Software and modules updates
============================

This page lists specific software and modules changes that are a result of the Operating System update.

Please see :ref:`modules` to learn how to use software modules, including 
how to to see the most recent software versions and availability. 

.. important:: If you are using any modules only by name without specifying versions
               (for example ``module load X`` stop and start using module name with the version
               as we always recommended: ``module load X/1.2.3``
               Otherwise, you will get unexpected results of not knowing which version
               of the software you are using when a new version is added or an old version is removed.
.. _softwre os:

Operating System
----------------

.. important:: | HPC3 operating system is **Rocky Linux 8** (as of August 30, 2022).
               | All installed software is compiled specifically for this OS.

When the Operating System changes some system installed software gets
deprecated or replaced by other packages.  Please note:

* ``screen`` is deprecated and is replaced with ``tmux``
* ``docker`` is not available per security vulnerability. Use *singularity* instead.
* ``sudo`` and ``su`` are not available to regular users per security vulnerability.
* If you compiled any software packages yourself using :tt:`gcc`, :tt:`intel`,
  :tt:`openmpi` modules you will have to recompile your packages anew. 
  Please see the table below for details about compilers and their modules availability. 
* Some commands, include files and libraries are available from system RPMs
  and do not require modules. If you compiled any software using such
  libraries/binaries you will need to recompile anew as many have changed with the new OS.
* If you installed any packages with :tt:`naconda` or :tt:`miniconda`, it is likely you will
  need to reinstall them. In this case, please try to use the latest version of
  :tt:`anaconda` or :tt:`miniconda` modules that we provide. Please see
  :ref:`install  conda`
  user guide that explains how to build and use conda environments on HPC3.

.. _modules availability:

Availability
------------

All software that we provide via modules is rebuilt for the new Operating System.
Some software is not possible to install as the prerequisites are no longer present.

**Summary of changes** 

The following table summarizes the differences in installation of modules on
the old and new OS:

.. table::
   :class: noscroll-table

   +-----------+----------+---------------+-------------------------------------+
   | Total     | CentOS 7 | Rocky Linux 8 | Comment                             |
   +===========+==========+===============+=====================================+
   | Installed | 295      | 333           | active modules                      |
   +-----------+----------+---------------+-------------------------------------+
   | Removed   |  75      |               | unused                              |
   +-----------+----------+---------------+-------------------------------------+
   | Removed   |  16      |               | no longer available for the new OS  |
   |           |          |               | or superseded by newer versions.    |
   +-----------+----------+---------------+-------------------------------------+
   | New       |          | 129           | Currently latest available version  |
   +-----------+----------+---------------+-------------------------------------+


**Detailed Changes**

Please use the table below to find out current modules, their versions and changes 
in their availability  for :tt:`Rocky Linux 8`. See footnotes after the table
for a few specific cases.

.. csv-table:: 
   :class: noscroll-table
   :file: updates-list.csv
   :widths: 25,10,10,55
   :header-rows: 1


**Notes**

* Operating system provided default compiler :tt:`gcc 4.8.5` and :tt:`openmpi 1.10.7` are replaced with newer versions.

  ============== ==============
  CentOS 7        Rocky Linux 8
  ============== ==============
  gcc.4.8.5      gcc.system
  openmpi.1.10.7 openmpi.4.1.1
  ============== ==============

  New module names are listed in respective comment column of the comparison
  table below. 

* :tt:`R 3.6.2` is not supported. Use newer R versions from series 4.
* :tt:`Python 2.7` has reached the end of life and is no longer supported. 
  It is installed but the outcome of any program can not be predicted.
  **If you have any python code that is still using python 2 convert your code to
  Python 3**. Test your application with the :tt:`-W` default command-line option
  to see any deprecation warnings and follow online guides (google) for porting
  Python 2 to Python 3.
* :tt:`Java 1.7.0` is no longer supported. Use newer versions of java.
* Intel and mkl module provide access to a number of Intel Math Kernel Libraries 
  including LAPACK, SCALAPACK, BLAS and threading options. The MKL libraries can be linked with Intel
  or GNU compilers. If you are compiling your software and using intel or mkl
  modules please see links
  `Intel MKL Documentaion <https://software.intel.com/en-us/mkl/documentation/view-all>`_
  and `Intel MKL Link Advisory <https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html#gs.o9qcu1>`_
  to help you figure out how to use them.
* Access to some application requires a license. Only registered users can
  use such software. Licenses are usually per PI's group and the access must be approved by a PI.
* VASP was compiled using:

  .. table::
     :class: noscroll-table

     +--------------+-------------------------+------------------------+
     | Vasp Version | CentOS 7                | Rocky Linux 8          |
     +==============+=========================+========================+
     | 5.4.4        | openmpi/1.10.7/gcc.4.8.5| openmpi/4.0.3/gcc.6.5.0|
     |              | fftw/3.3.8/gcc.4.8.5    | fftw/3.3.8/gcc.system  | 
     +--------------+-------------------------+------------------------+
     | 6.1.2        | openmpi/4.0.3/gcc.6.5.0 | openmpi/4.0.3/gcc.6.5.0|
     |              | fftw/3.3.8/gcc.4.8.5    | fftw/3.3.8/gcc.system  |
     +--------------+-------------------------+------------------------+
* :tt:`Cufflinks` does not work under Rocky Linux 8. Use a singularity container build with cufflinks compiled for CentOS 7.
  The image /dfs8/singularity-images/cufflinks.simg is build with singularity/3.7.2. 
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
