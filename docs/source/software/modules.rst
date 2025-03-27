.. _modules:

Environment modules
===================

.. contents::
   :local:

Overview
---------

Some applications that are installed with the system OS must be always accessible by users.
They do not require any special settings and they are available without any modules.

A very large fraction of scientific software applications on HPC3
can be accessed only after loading their associated :term:`Environment Modules`.

**What are Modules?**
  :bluelight:`Language modules`
     or packages are collections of related variables, functions and subroutines that perform a set
     of specific programming tasks. They are files consisting Python/R/Perl code.
     To access a language module (package) or find out what is installed,
     you need to use its language interface.  For example,

     For Python modules (packages) :

       .. code-block:: python

          import numpy as np
          import matplotlib.pyplot as plt

     For R modules (packages) :

       .. code-block:: R

          library(corrr)

     For Perl modules (packages) :

       .. code-block:: perl

          use File::Temp qw(tempfile);

  :bluelight:`Environment modules`
     are simple files or scripts that, when executed, affect your Unix environment variables.
     They activate a specific software (including Python/R/Perl) that a user wants to use
     via :underline:`providing a control which versions
     of software are active and setting environment needed by that software`.

     For the most part, cluster users only need to know or discover the
     already-available software *environment module* and load it prior to using the application.

     Environment modules are very simple to use:

     :loading a module: is used to activate the software. It
               modifies environment variables ``PATH`` for finding applications binaries,
               ``LD_LIBRARY_PATH`` for shared object libraries, sets specific variables if needed, etc.
     :unloading a module: is used to deactivate the software. It
                 reverses the action of loading and resets the environment variables set by loading.

     Modules are accessible via ``module`` command. To find in-depth details about
     using this command  please execute ``module --help`` command.

     Please see sections below to learn how to use environment modules.

.. _list modules:

List modules
------------

``module avail``

**To list all available modules:**

  .. code-block:: console

     [user@login-x:~]$ module avail

  The output will list all installed modules by :ref:`categories <module categories>` .
  We try to broadly classify software into categories by what they do so
  that it is a bit easier to find a module you are interested in.

**To list all modules for specific software**:

  .. code-block:: console

     [user@login-x:~]$ module avail eigen
     -------------------- /opt/rcic/Modules/modulefiles/LIBRARIES --------------------
     eigen/3.3.7  eigen/3.4.0

  The output shows 2 modules for *eigen* software in `LIBRARIES` category.

.. _search modules:

Search modules
--------------

| ``module avail``
| ``module keyword``

You might not know the name of a particular module or versions available.
You can use one of the following commands to find some information.
Note, by default the search of modules is case-sensitive.
To turn on case insensitive mode, add ``-i`` switch to your
``module`` commands.

**Partial name lookup**:
  Case sensitive

  .. code-block:: console

     [user@login-x:~]$ module avail eig
     -------------------- /opt/rcic/Modules/modulefiles/LIBRARIES --------------------
     eigen/3.3.7  eigen/3.4.0

  Case insensitive

  .. code-block:: console

    [user@login-x:~]$ module avail -i BWA
    -------------------- /opt/rcic/Modules/modulefiles/BIOTOOLS ---------------------
    bwa/0.7.8  bwa/0.7.17

**Keyword lookup**
  Find the keyword if it shows up anywhere in the module definition:

  .. code-block:: console

     [user@login-x:~]$ module keyword eigen
     -------------------- /opt/rcic/Modules/modulefiles/LIBRARIES --------------------
           eigen/3.3.7: Category_______ LIBRARIES
           eigen/3.3.7: Name___________ eigen
           eigen/3.3.7: Version________ 3.3.7
           eigen/3.3.7: Description____ Eigen is a C++ template library for linear
           ...
           eigen/3.4.0: Category_______ LIBRARIES
           eigen/3.4.0: Name___________ eigen
           eigen/3.4.0: Version________ 3.4.0
           eigen/3.4.0: Description____ Eigen is a C++ template library for linear
           ...
       scalapack/2.1.0: Category_______ LIBRARIES
       scalapack/2.1.0: Name___________ scalapack
       scalapack/2.1.0: Version________ 2.1.0
       scalapack/2.1.0: Description____ ScaLAPACK 2.1.0 is a library of high-performance
       ...

  The above partial output shows in the 1st column module names
  that contain a keyword, and in the second column shows the text line
  of the module file where a keyword was found.  The keyword :tt:`eigen` is found in 3 different
  modules.

.. _display modules:

Display modules
---------------

| ``modulw whatis``
| ``module display``

**Find information about specified module**
  .. code-block:: console

     [user@login-x:~]$ module whatis hdf5/1.10.5/gcc.8.4.0
     hdf5/1.10.5/gcc.8.4.0: Category------- TOOLS
     hdf5/1.10.5/gcc.8.4.0: Name----------- hdf5
     hdf5/1.10.5/gcc.8.4.0: Version-------- 1.10.5
     hdf5/1.10.5/gcc.8.4.0: Description---- HDF5 is a data model, library and file format
     hdf5/1.10.5/gcc.8.4.0:                 for storing and managing data. It supports an
     hdf5/1.10.5/gcc.8.4.0:                 unlimited variety of datatypes, and is designed
     hdf5/1.10.5/gcc.8.4.0:                 for flexible and efficient I/O and for high
     hdf5/1.10.5/gcc.8.4.0:                 volume and complex data. HDF5 is portable and
     hdf5/1.10.5/gcc.8.4.0:                 is extensible, allowing applications to evolve
     hdf5/1.10.5/gcc.8.4.0:                 in their use of HDF5. The HDF5 Technology suite
     hdf5/1.10.5/gcc.8.4.0:                 includes tools and applications for managing,
     hdf5/1.10.5/gcc.8.4.0:                 manipulating, viewing, and analyzing data in
     hdf5/1.10.5/gcc.8.4.0:                 the HDF format. Environment var:
     hdf5/1.10.5/gcc.8.4.0:                 HDF5_HOME=/opt/apps/hdf5/1.10.5/gcc/8.4.0
     hdf5/1.10.5/gcc.8.4.0: Load modules--- java/1.8.0
     hdf5/1.10.5/gcc.8.4.0:                 gcc/8.4.0
     hdf5/1.10.5/gcc.8.4.0: Prerequisites-- java8-module
     hdf5/1.10.5/gcc.8.4.0:                 gcc_8.4.0-module
     hdf5/1.10.5/gcc.8.4.0:                 rcic-module-support
     hdf5/1.10.5/gcc.8.4.0:                 hdf5_1.10.5_gcc_8.4.0

  The output shows this module

     | :tt:`Category` convenience grouping 
     | :tt:`Name`, :tt:`Version` for the software 
     | :tt:`Description` what this software does
     | :tt:`Load modules` prerequisite modules that will be automatically loaded
     | :tt:`Prerequisites` list of already installed RPM packages this software requires to work

  The prerequisites modules and RPMS are automatically found, user does not
  need to do anything special.

**Find more info about a specific module**
  .. code-block:: console

     [user@login-x:~]$ module display hdf5/1.10.5/gcc.8.4.0
     -------------------------------------------------------------------
     /opt/rcic/Modules/modulefiles/TOOLS/hdf5/1.10.5/gcc.8.4.0:

     module-whatis   {Category_______ TOOLS}
     module-whatis   {Name___________ hdf5}
     module-whatis   {Version________ 1.10.5}
     module-whatis   Description---- HDF5 is a data model, library and file format
     module-whatis                   for storing and managing data. It supports an
     module-whatis                   unlimited variety of datatypes, and is designed
     module-whatis                   for flexible and efficient I/O and for high
     module-whatis                   volume and complex data. HDF5 is portable and
     module-whatis                   is extensible, allowing applications to evolve
     module-whatis                   in their use of HDF5. The HDF5 Technology suite
     module-whatis                   includes tools and applications for managing,
     module-whatis                   manipulating, viewing, and analyzing data in
     module-whatis                   the HDF format. Environment var:
     module-whatis                   HDF5_HOME=/opt/apps/hdf5/1.10.5/gcc/8.4.0
     module-whatis   {Load modules___ java/1.8.0}
     module-whatis   {                gcc/8.4.0}
     module-whatis   {Prerequisites__ rcic-module-support}
     module-whatis   {                hdf5_1.10.5_gcc_8.4.0}
     module-whatis   {                java/1.8.0}
     module-whatis   {                gcc/8.4.0}
     prereq          java/1.8.0
     prereq          gcc/8.4.0
     setenv          hdf5__PREFIX /opt/apps/hdf5/1.10.5/gcc/8.4.0
     setenv          hdf5__CPPFLAGS -I/opt/apps/hdf5/1.10.5/gcc/8.4.0/include
     setenv          hdf5__LDFLAGS {-L/opt/apps/hdf5/1.10.5/gcc/8.4.0/lib -Wl,-rpath,/opt/apps/hdf5/1.10.5/gcc/8.4.0/lib}
     setenv          HDF5_HOME /opt/apps/hdf5/1.10.5/gcc/8.4.0
     prepend-path    PATH /opt/apps/hdf5/1.10.5/gcc/8.4.0/bin
     prepend-path    MANPATH /opt/apps/hdf5/1.10.5/gcc/8.4.0/share/man
     prepend-path    LD_LIBRARY_PATH /opt/apps/hdf5/1.10.5/gcc/8.4.0/lib
     prepend-path    PKG_CONFIG_PATH /opt/apps/hdf5/1.10.5/gcc/8.4.0/lib/pkgconfig
     prepend-path    -d { } CPPFLAGS -I/opt/apps/hdf5/1.10.5/gcc/8.4.0/include
     prepend-path    -d { } LDFLAGS {-L/opt/apps/hdf5/1.10.5/gcc/8.4.0/lib -Wl,-rpath,/opt/apps/hdf5/1.10.5/gcc/8.4.0/lib}

  The ``display`` command gives additional info compare to ``whatis``:

     | first output line shows the full path of the module file
     | :tt:`setenv` lines show the environment variables that will be set
     | :tt:`prepend-path` lines show changes added to the PATH-like variables

.. _load modules:

Load modules 
------------

| ``module load``

**To load a specific module**
  .. code-block:: console

     [user@login-x:~]$ module load hdf5/1.14.1/gcc.11.2.0
     [user@login-x:~]$ module list
     Currently Loaded Modulefiles:
     1) java/17   2) gcc/11.2.0   3) hdf5/1.14.1/gcc.11.2.0

**To get the most out of modules please follow a few simple load rules:**
  1. You need to load  modules

     * in Slurm submit scripts for batch jobs
     * in your interactive shell for interactive jobs

     Modules are automatically unloaded when your batch or interactive job exists.

  #. You can load multiple modules, loading order is not important.
  #. Always load a module using the module name with its version:

     .. table::
        :class: noscroll-table
        :widths: 28 72

        +-------------------------+---------------------------------------------------------------+
        | Command                 | Result                                                        |
        +=========================+===============================================================+
        | ``module load X/1.2.3`` | this ensures you will get the version you need.               |
        +-------------------------+---------------------------------------------------------------+
        | ``module load X``       | :underline:`using without a version is DANGEROUS`. A default  |
        |                         | behavior is loading the latest version currently available.   |
        |                         | This may give unexpected results of using a wrong software    |
        |                         | version when a new version is added or an old one is removed. |
        +-------------------------+---------------------------------------------------------------+
		
  #. :red:`Never load modules in your .bashrc or
     .bash_profile files`.

     If loaded in these files, modules will be present for the duration of the
     shell life and will change the shell environment for all commands which is completely unnecessary
     and in some cases can have an undesried effect. Please see :ref:`shell init files <bash init files>`.

.. _unload modules:

Unload modules 
--------------

| ``module unload``

**To unload previously loaded module**
  .. code-block:: console

     [user@login-x:~]$ module unload hdf5/1.14.1/gcc.11.2.0
     [user@login-x:~]$ module list
     No Modulefiles Currently Loaded.

To get the most out of modules please follow a few simple unload rules. 

#. It is easier to unload all loaded modules via

   .. code-block:: console

      [user@login-x:~]$ module purge

#. You can only unload modules that you explicitly loaded via ``module load`` command:

   .. code-block:: console

      [user@login-x:~]$ module load bwa/0.7.17
      ...  do some work ...
      [user@login-x:~]$ module unload bwa/0.7.17

#. :red:`Never unload modules that were auto-loaded by a module itself`

   Environment modules do their job, but have limitations.
   You can easily render your environment into a completely
   broken mess if you randomly unload modules.

   For example, if you unload one of the prerequisite modules that were
   automatically loaded when you did :tt:`module load PkgName/1.2.3` you won't see any errors or
   complaints until you attempt to run :tt:`PkgName` program. Needed libraries or binaries
   that were provided by unloaded module will not be available.
   :underline:`The solution is to unload only modules that you explicitly loaded`. 

#. If you loaded multiple modules and need to unload them (rare cases),
   **always unload modules in the reverse order of loading**:
   last-loaded should be first unloaded. Not doing
   this can result in an expected or broken environment.

   For example, if you loaded modules as:

   .. code-block:: console

      [user@login-x:~]$ module load bwa/0.7.17
      [user@login-x:~]$ module load proj/9.0.0
      [user@login-x:~]$ module load bracken/2.6.0

   You will need to unload them in reverse:

   .. code-block:: console

      [user@login-x:~]$ module unload bracken/2.6.0
      [user@login-x:~]$ module unload proj/9.0.0
      [user@login-x:~]$ module unload bwa/0.7.17


.. _use modules:

HPC3-specific
-------------

There are a few specifics about how the modules are built that are unique to HPC3:

:bluelight:`Nearly all modules have version numbers`
  Version numbers specify the software version they provide, they are important!
  You will need to use them when loading or unloading modules.

.. _module categories:

:bluelight:`We use a notion of Category to group modules`
  This is only a convenience and simply list modules according to the categories
  in the output of ``module avail``  or ``module display`` commands.
  A partial output example shows AI-LEARNING, BIOTOOLS and CHEMISTRY categories: 

  .. code-block:: console

     [user@login-x:~]$ module avail
     ----------------------------- /opt/rcic/Modules/modulefiles/AI-LEARNING -----------------
     pytorch/1.5.1  pytorch/1.11.0  tensorflow/2.0.0  tensorflow/2.8.0  tensorRT/8.4.2.4  

     ----------------------------- /opt/rcic/Modules/modulefiles/BIOTOOLS --------------------
     bamtools/2.5.2    bowtie2-python2/2.4.1  bwa/0.7.8        edirect/2020     gatk/4.1.9.0   
     bcftools/1.10.2   bowtie2/2.4.1          bwa/0.7.17       edirect/2022     gatk/4.2.6.1  
     bcftools/1.15.1   bowtie2/2.4.4          cutadapt/2.10    fastp/0.20.0     hmmer/3.3     
     ... 
     ----------------------------- /opt/rcic/Modules/modulefiles/CHEMISTRY -------------------
     amber/19.11/gcc.8.4.0   gromacs/2021.2/gcc.8.4.0-cuda.10.1.243  
     amber/21.12/gcc.11.2.0  gromacs/2021.2/gcc.8.4.0-cuda.10.1.243.openmpi.4.0.3 
     ... 

.. _module names:

:bluelight:`We use a module naming schema for module names`
  RCIC-authored modules follow a uniform build, formatting and module naming schema.
  You will notice in the output of ``module avail`` commands that the module
  names have a few formats (all from the naming schema).

  The module naming schema makes it more apparent what version is available and what
  are key differences among different versions of the same application. This also shows the potential
  *combinatorial* number of variants of any software (compiled with different compilers, MPI, CUDA, etc).

  .. We do not build every variant of *compiler x mpi*, we build what is needed.

  .. centered:: Module naming schema

  | *name*
  |   example: :tt:`dot`
  |   for module with only a name without version, *reserved for a few OS-installed modules*.
  | *name/version*
  |   example: :tt:`python/3.8.0`
  |   for a specific version of python.
  | *name/version/compiler.compiler_version*
  |   example: :tt:`boost/1.78.0/gcc.8.4.0`
  |   for a specific version of boost built with a specific compiler.
  | *name/version/compiler.compiler_version-mpi.mpi_version*
  |   example: :tt:`hdf5/1.10.5/intel.2020u1-openmpi.4.0.3`
  |   example: :tt:`hdf5/1.10.5/gcc.8.4.0-openmpi.4.0.3`
  |   for HDF5 version built with Intel and GCC compilers and Open MPI.
  | *name/version/compiler.compiler_version-cuda.cuda_version*
  |   example: :tt:`namd/2.14b2/gcc.8.4.0-cuda.10.1.243`
  |   for a specific NAMD version built with gcc compiler and CUDA.


:bluelight:`Many modules are compiled with GCC compiler`
  For some of them we do not specify compiler in the module name, for others we do. This is dictated by
  the software build specifics. The prerequisite compiler will be automatically
  loaded by the module if needed.

:bluelight:`Automatic prerequisites loading`
  If a module has any prerequisite modules they are automatically added when
  the module is loaded. Users don't need to worry about prerequisites.
:bluelight:`Automatic prerequisites unloading`
  The prerequisite modules are automatically removed when the module is
  unloaded. Our modifications to modules has Smart unloading:  when a prerequisite
  was already loaded, unloading the higher-level module will leave the prerequisite intact.
:bluelight:`Users can add their own modules`
  We provide a convenient and simple way for users :ref:`to add their own modules <user installed modules>`.

:bluelight:`How modules change environment`
  Module change user environment via setting specific environment variables 
  and modifying PATH-like existing variables. 

  Suppose you want access to GCC compiler version 8.4.0.

  Check if any modules are loaded, and what is active gcc version:

    .. code-block:: console

       [user@login-x:~]$ module list
       No Modulefiles Currently Loaded.
       [user@login-x:~]$ gcc --version | grep ^gcc
       gcc (GCC) 8.5.0 20210514 (Red Hat 8.5.0-10)

  Load desired gcc module and verify what is gcc version after loading:

    .. code-block:: console

       [user@login-x:~]$ module load gcc/8.4.0
       [user@login-x:~]$ module list
       Currently Loaded Modulefiles:
         1) gcc/8.4.0
       [user@login-x:~]$ gcc --version | grep ^gcc
       gcc (GCC) 8.4.0

  Unload the module, this restores the environment, active gcc version is reverted to default:

    .. code-block:: console

       [user@login-x:~]$ module unload gcc/8.4.0   # 3
       [user@login-x:~]$ gcc --version | grep ^gcc
       gcc (GCC) 8.5.0 20210514 (Red Hat 8.5.0-10)

.. _moudles for compiling:

Modules for compiling 
---------------------

For user installed software there are often prerequisites that a 
software needs. We provide many modules that can satisfy such requirements.

For each module, we set the variables according to what the
software developers provide, and otherwise we use a common convention.
For example, the software installation directory is often specified by the
variable *NAME_DIR* or *NAME_HOME* where *NAME* is the software name.
There is no exact formula but one can always see what
variables are set by a given module via module display commands.

You need to figure out:

  * what modules to load 
  * what environment variables set by these modules you will to use in your software compilation process. 

**Example: compiling VASP**

Lets say, you are compiling VASP software and it requires OpenBLAS, ScaLAPACK,
FFTW with OpenMPI, HDF5 as prerequisites.  VASP installation guide expects you to set
certain variables in the Makefiles according to where these prerequisites are
installed on a given system.  Your actions will be:

1. Check variables that need setting. A short snippet of VASP makefile shows:

   .. code-block:: makefile
   
      OPENBLAS_ROOT ?=     # need OPENBLAS installation dir
      SCALAPACK_ROOT ?=    # need SCALAPACK installation dir
      FFTW_ROOT  ?=        # need FFTW installation dir
      HDF5_ROOT  ?=        # need HDF5 installation dir

      LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran  # this line uses existing variable
      INCS       += -I$(HDF5_ROOT)/include             # this line uses existing variable
      INCS_FFTLIB = -I./include -I$(FFTW_ROOT)/include # this line uses existing variable

#. Use ``moddule av`` commands to find what modules are available for needed software
   prerequisites then ``module display`` to check what each module provides, for example:

   .. code-block:: console
  
      [user@login-x:~]$ module av scalapack
      ------------ /opt/rcic/Modules/modulefiles/LIBRARIES -------------
      scalapack/2.1.0

      [user@login-x:~]$ module display scalapack/2.1.0
 	 -------------------------------------------------------------------
      /opt/rcic/Modules/modulefiles/LIBRARIES/scalapack/2.1.0:

      module-whatis   {Category_______ LIBRARIES}
      module-whatis   {Name___________ scalapack}
      module-whatis   {Version________ 2.1.0}
      module-whatis   {Description____ ScaLAPACK 2.1.0 is a library of high-performance linear algebra routines}
      module-whatis   {                for parallel distributed memory machines. ScaLAPACK solves dense and}
      module-whatis   {                banded linear systems, least squares problems, eigenvalue problems,}
      module-whatis   {                and singular value problems. See http://www.netlib.org/scalapack/}
      module-whatis   {Prerequisites__ rcic-module-support}
      module-whatis   {                scalapack_2.1.0}
      setenv          SCALAPACK_DIR /opt/apps/scalapack/2.1.0
      prepend-path    LD_LIBRARY_PATH /opt/apps/scalapack/2.1.0/lib

   | Here, `SCALAPACK_DIR` is the location of SCALAPACK installation.
   | Similarly, looking at the rest of the modules one can 
     get information about installation directories, include files, libraries, etc.
     for the remaining prerequisites.

#. Load modules with the desired version, compiler and any other option, for example:

   .. code-block:: console
  
      [user@login-x:~]$ module load scalapack/2.1.0
      [user@login-x:~]$ module load OpenBLAS/0.3.19
      [user@login-x:~]$ module load fftw/3.3.10/gcc.11.2.0-openmpi.4.1.2
      [user@login-x:~]$ module load hdf5/1.13.1/gcc.11.2.0

   Note, when choosing different modules keep compier the same, here :tt:`gcc`
   version :tt:`11.2.0`.

#. Once you find all the needed variables edit the makefile:

   .. code-block:: makefile

      OPENBLAS_ROOT ?= $(OPENBLAS_HOME)    # edited line
      SCALAPACK_ROOT ?= $(SCALAPACK_DIR)   # edited line
      FFTW_ROOT  ?= $(FFTW_DIR)            # edited line
      HDF5_ROOT  ?= $(HDF5_HOME)           # edited line

      LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran   # no change
      INCS       += -I$(HDF5_ROOT)/include              # no change
      INCS_FFTLIB = -I./include -I$(FFTW_ROOT)/include  # no change

   Note, you use a variable  such as :tt:`$(SCALAPACK_DIR)` and not what it 
   resolves to,  which is :tt:`/opt/apps/scalapack/2.1.0`. This makes it
   easier to reuse the makefile if you decide to choose a different version of
   a specific module. We keep the environment variables names the same for
   different  versions of  a given module. 

#. Proceed with your software instructions to run ``make``, ``cmake`` or similar commands
   per your install instructions to compile and install your software.

#. To use your compiled software we recommend to create a module for it,
   please see the next section. Remember, you will need to load the same modules you used
   for compiling  when running your executables. 

.. _user installed modules:

User installed modules
----------------------

You don't need to create a new module if you are installing
packages (a.k.a language modules) for Python/R/Perl, or when adding packages with conda.
Please see the install guides in :ref:`user installed` that explain
how to create conda environments, or to install Python/R/Perl packages.

Users who install additional software can add environment module for it
either for themselves or for their groups.

.. attention:: Software install and module install are two separate
               tasks. The installation location of a module file is
               different from the location where the software is installed.

There are a few basic steps:

1. **Compile and install your desired software**

   Do this in your user or group area :underline:`per your software instructions`.
   Verify that the software is working.

   * if installing for yourself, your user area is in :tt:`/pub/UCInetID`

	 .. important:: | Do not install in :tt:`$HOME`.
                    | Do not install in :tt:`$HOME/modulefiles/`

   * if installing for the group, your group area is in one of DFS
     file systems. Make sure that for group access the directories and files permissions
     are set correctly.

2. **Create an environment module template**

   The environment module file is a text file in a specific format that provides
   information about the software and creates needed environment for using it.


   We suggest to use existing available software module files as a templates.

   Run command ``module display`` for one of the available modules,
   the output shows the full path to the module (output first line).
   Copy this file to your user area, for example:

   .. code-block:: console

      [user@login-x:~]$ module display clang/13.0.0
      ----------------------------------------------------
      /opt/rcic/Modules/modulefiles/COMPILERS/clang/13.0.0:

      module-whatis   {Category_______ COMPILERS}
      module-whatis   {Name___________ clang}
      module-whatis   {Version________ 13.0.0}
      module-whatis   {Description____ Clang version 13.0.0.
          <output truncated>

      [user@login-x:~]$ cp /opt/rcic/Modules/modulefiles/COMPILERS/clang/13.0.0 template

   Alternatively, copy and paste the following code into :tt:`template` file:

   .. literalinclude:: files/modulefile-template
      :language: text

   Modify your :tt:`template` file according to :underline:`your new software` needs.
   In general, you will need to specify:

   * software description, name and version
   * environment variables your software needs, for example :tt:`PATH`, :tt:`LD_LIBRARY_PATH`
   * modules that you used to compile your software (compiler, openmpi, etc.)


3. **Install created template file as a module**.

   Now, you have the edited template, you need to rename it and to install it.

   Please follow the `module names`_ naming schema for the module file name and choose
   where to put it.

   For example, lets assume you are installing software called :tt:`gsutil`
   version :tt:`4.53` (per template example above). Your module name can be
   :tt:`gsutils-4.53`.

   a. :bluelight:`If you are installing the new software module for yourself`

      Use :tt:`$HOME/modulefiles/` directory to store your created module files. It is
      searched by module commands by default.

      .. code-block:: console

         [user@login-x:~]$ mkdir ~/modulefiles
         [user@login-x:~]$ mv template ~/modulefiles/gsutil-4.53

      Verify your installed module file is working.
      If your environment module file is installed correctly (file contents and
      file path) then your new module will show  at the end of the output:

      .. code-block:: console

         [user@login-x:~]$ module avail gsutil
         ------------------- /data/homezvol0/panteater/modulefiles ------------------------
         gsutil-4.53

      .. important::

         If no valid module files are present in :tt:`$HOME/modulefiles/`, the
         module name will NOT be shown when running module commands, or will produce an
         error. Review steps above and correct any errors.

   b. :bluelight:`If you are installing the new software module for the group`

      | Let say
      |  you installed a new gcc software 8.4.1 in :tt:`/dfs3/panteater-lab/project1/sw/`
      |  you  want your created modules files be in a directory :tt:`/dfs3/panteater-lab/modulefiles/`

      You need to enable ``module`` commands to find your created module file.
      This is done via adding pathnames to the :tt:`$HOME/.usermodulepath` file.
      Initially, this text file does not exist, simply create it using your favorite text editor:

      .. code-block:: console

         [user@login-x:~]$ touch ~/.usermodulepath
         [user@login-x:~]$ vim ~/.usermodulepath

      | File format is simple:
      |  you can put multiple paths, type each path on a separate line
      |  comment lines start with a :tt:`#`.

      Here is an example :tt:`~/.usermodulespath` file:

      .. code-block:: bash

         # Put a directory path per line to search for additional modules
         # put actual modules files inside the directories specified by
         # the paths below. the modules will be accessible by panteater-lab users
         /dfs3/panteater-lab/modulefiles
         #
         # the following path is for the future use
         /share/crsp/lab/panteater/share/modulefiles

      After you modify the contents of :tt:`$HOME/.usermodulespath`,
      for the changes to take effect please start a new bash shell:

      .. code-block:: console

         [user@login-x:~]$ . ~/.bashrc

      The next steps will copy your created module template module file
      (done in previous step) into your proposed module location. When done
      this will define a new module :tt:`gcc/8.4.1`:

      .. code-block:: console

         [user@login-x:~]$ mkdir -p /dfs3/panteater-lab/modulefiles/gcc/
         [user@login-x:~]$ cp template /dfs3/panteater-lab/modulefiles/gcc/8.4.1

      .. important:: Other users who want to use your publicly available module file,
                     will need to create :tt:`$HOME/.usermodulespath` file with the same contents as yours.
                     Share copy of this file in group area and let others know how to use it.

      If your installed module file is correct you can run module commands
      to display and load your module as shown below:

      .. code-block:: console

         [user@login-x:~]$ module list
         No Modulefiles Currently Loaded.

         [user@login-x:~]$ module avail
         ------------------------ /opt/rcic/Modules/modulefiles/TOOLS -------------------
         fftw/3.3.8                             netcdf-c/4.7.0/intel.2020u1
             <output truncated>
         ------------------------ /dfs3/panteater-lab/modulefiles -----------------------
         gcc/8.4.1

         [user@login-x:~]$ module avail
         [user@login-x:~]$ module load gcc/8.4.1
         [user@login-x:~]$ module list
         Currently Loaded Modulefiles:
           1) gcc/8.4.1

