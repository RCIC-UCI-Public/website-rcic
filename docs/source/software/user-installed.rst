.. _user installed:

User installed software
=======================

Users often ask to add packages to
:tt:`Python` / :tt:`R` / :tt:`Perl` / :tt:`conda` / :tt:`miniconda` base installations.

| These usually need to be installed by users themselves.
| The following guides explain how to install software in user area:

Please note, you don't need to install
:tt:`Python` / :tt:`R` / :tt:`Perl` / :tt:`conda` / :tt:`miniconda`, we
already have multiple versions of each software installed and they all are
accessible via modules.

Simply load Python/R/Perl/conda/miniconda  module  using command ``module avail``
(read :ref:`list modules` for details) to find out
what particular software is already installed), then follow your package
installation instructions.

.. note:: | There are a few important initial installation steps that are unique to the HPC3.
          | They are explained in the guides below.

.. centered:: Software installation guides

===================== =========================== ================
:ref:`install conda`  :ref:`install python`       :ref:`install r`
:ref:`install perl`   :ref:`install singularity`  :ref:`compile`
===================== =========================== ================

.. _install conda:

Install with conda
------------------

When you want to build a specific application using conda
you :red:`do not need to install Miniconda or Anaconda`.
We provide a few basic Minicaonda/Anaconda versions that can be accessed via modules.
To find out what is available:

.. code-block:: console

   [user@login-x:~]$ module avail miniconda
   ----------------- /opt/rcic/Modules/modulefiles/LANGUAGES ----------------------
   miniconda3/4.8.5  miniconda3/4.12.0

   [user@login-x:~]$ module avail anaconda
   ---------------- /opt/rcic/Modules/modulefiles/LANGUAGES -----------------------
   anaconda/2020.07 anaconda/2021.11 anaconda/2022.05

Usually, to install an application one needs to create a local conda environment.
You can choose either Miniconda or Anaconda depending on what is your package
installation instructions require and build your local conda environment.

For additional info on conda-specific commands and builds please see conda documentation
`Bulding Conda local environments <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`_

Steps below explain the basic build specific to the cluster.

To install conda environment in your user area
follow the steps below. The example is given for the
anaconda version 2021.11 for Python 3.9.7. The steps are the
same for other versions of conda (substitute version numbers where needed).
Your output will have your UCINetID where needed in steps below (we use as an
example panteater).

1. **Get an interactive node**

   Always claim an interactive node  because conda builds involve compilation and downloads
   that can use  a lot of  CPU time and memory. If you do this on login node
   you will have problems and your install will likely fail.

   .. code-block:: console

      [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i

2. **Load desired anaconda/miniconda module**

   For building in your user area, first you need to load anaconda module:

   .. code-block:: console

      [user@login-x:~]$ module load anaconda/2021.11

   Check that ``conda`` command is available after module loading, the output of the
   command below should be similar to:

   .. code-block:: console

      [user@login-x:~]$ which conda
      /opt/apps/anaconda/2021.11/bin/conda

   .. attention:: Conda always provides python and a few other applications.
                  For this reason DO NOT load any python modules when working
                  with anaconda/miniconda modules. If you do, your environment
                  will have problems.

3. **Verify conda info**

   To check info about conda, execute command:

   .. code-block:: console

      [user@login-x:~]$ conda info
           active environment : None
             user config file : /data/homezvol0/panteater/.condarc
       populated config files :
                conda version : 4.10.3
          conda-build version : 3.21.5
               python version : 3.9.7.final.0
             virtual packages : __linux=3.10.0=0
                                __glibc=2.17=0
                                __unix=0=0
                                __archspec=1=x86_64
             base environment : /opt/apps/anaconda/2021.11  (read only)
            conda av data dir : /opt/apps/anaconda/2021.11/etc/conda
        conda av metadata url : None
                 channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                                https://repo.anaconda.com/pkgs/main/noarch
                                https://repo.anaconda.com/pkgs/r/linux-64
                                https://repo.anaconda.com/pkgs/r/noarch
                package cache : /opt/apps/anaconda/2021.11/pkgs
                                /data/homezvol0/panteater/.conda/pkgs
             envs directories : /data/homezvol0/panteater/.conda/envs
                                /opt/apps/anaconda/2021.11/envs
                     platform : linux-64
                   user-agent : conda/4.10.3 requests/2.26.0 CPython/3.9.7 Linux/3.10.0-1160.53.1.el7.x86_64 centos/7.9.2009 glibc/2.17
                      UID:GID : 1234567:1234567
                   netrc file : None
                 offline mode : False

   Check **package cache** and **envs directories** entries in the above output.
   There should be 2 lines for each, one referring to the system installed
   location (lines start with */opt/apps*) and another to your user location
   (line starts with */data/homezvol...*).
   If there are missing entries that point to your user area, you will need
   to create a file in your $HOME using your favorite editor.
   The file name is :tt:`.condarc` and the content is (substitute your
   version, home directory and user name):

   .. code-block:: console

      pkgs_dirs:
        - /data/homezvol0/panteater/.conda/pkgs
        - /opt/apps/anaconda/2021.11/pkgs
      envs_dirs:
        - /data/homezvol0/panteater/.conda/envs
        - /opt/apps/anaconda/2021.11/envs

4. **Initialize conda for your shell**

   Run command:

   .. code-block:: console

      [user@login-x:~]$ conda init bash

   This adds a few lines to your :tt:`~/.bashrc` file which may not always be desirable
   for your work with other programs.  Edit the :tt:`~/.bashrc` file and move all the lines
   added by conda into another file, for example to :tt:`~/.mycondainit-2021.11`.
   The lines are at the end of your :tt:`~/.bashrc` file (lines start end end with conda initialize
   and all the lines between them):

   .. code-block:: bash

      # >>> conda initialize >>>
      # !! Contents within this block are managed by 'conda init' !!
          <some lines are cut here>
      unset __conda_setup
      # <<< conda initialize <<<

5. **Create a local environment**

   Now you are ready to :red:`follow the instructions provided by your software package` and
   can create your local conda environment. The name  can be anything
   that makes sense, has to be a single word (no spaces), the exact
   command will be provided in your software instructions and may have
   additional arguments in it. Here, as an example  we create a local
   environment called **Local2**:

   .. code-block:: console

      [user@login-x:~]$ conda create -n Local2

   This will take some time to complete as anaconda is installing a lot
   of packages in your directory :tt:`~/.conda` and depending on what you are
   installing it may take 2 - 4Gb of space.
   You will see a lot of messages and at the end something similar to:

   .. code-block:: bash

      SomePackage-1.2.1    | 28 KB     | ###################### | 100%
      Preparing transaction: done
      Verifying transaction: done
      Executing transaction: done
      #
      # To activate this environment, use:
      # > conda activate Local2
      #
      # To deactivate an active environment, use:
      # > conda deactivate
      #

   The last few lines indicate the commands you will need for activating and
   deactivating your conda environment.

6. **Install your software package**

   Using your newly created environment you can now install desired software
   :red:`per your software instructions`. The instructions vary, here is a handful of
   possible examples:

   .. code-block:: bash

      [user@login-x:~]$ conda install -c https://conda.binstar.org/bokeh ggplot    # Install ggplot
      [user@login-x:~]$ conda install -c https://conda.binstar.org/asmeurer r-nlme # Install r-nlme
      [user@login-x:~]$ conda install xarray                                       # install xarray

7. **Use your conda environment**

   The above installation steps 1-5 need to be done only once for
   specific software install in a specific local conda environment. Now you have your
   local copy of conda where you can install packages/programs you need.

   You can build multiple local environments using the same method.
   Or you can add more packages to the existing environments. The choice
   depends on the software and on its instructions.

   Every time you login and want to use your conda local environment and its packages you will need
   to run the following commands to activate your conda environment:

   .. code-block:: console

      [user@login-x:~]$ module load anaconda/2021.11
      [user@login-x:~]$ . ~/.mycondainit-2011.11
      [user@login-x:~]$ conda activate Local2


   If you submit your computation via slurm script these 3 commands need to be
   present before you execute your software commands.

   Your environment is deactiated automatically when you logout or when your
   Slurm job finishes.
   To deactivate your environment right away you need to do:

   .. code-block:: console

      [user@login-x:~]$ conda deactivate

.. _install python:

Install Python packages
-----------------------

Python has thousands of specific packages and it is not possible for us to maintain
them all. For this reason users can easily add their desired packages
to the base installs using local *user area*.

The local installation of Python packages will go to the :tt:`$HOME/.local`
and is automatically available to the user.

When you want to install a specific Python package
you :red:`do not need to install Python`. We provide a few
Python versions that can be accessed via modules.

To find out what Python is available:

.. code-block:: console

   [user@login-x:~]$ module avail python
   ---------------------- /opt/rcic/Modules/modulefiles/LANGUAGES ---------------------------
   python/2.7.17  python/3.8.0  python/3.10.2


.. important:: While you can still choose python version 2.7.17, it is no longer
               supported and may not work properly under Rocky Linux 8 operating
               system. It is advisable to use Python 3.

For detailed info on installing Python packages please see
`Python packages with pip <https://pip.pypa.io/en/stable/user_guide>`_.

Steps below explain the basic commands specific to the cluster.

1. **Get an interactive node**

   Always claim an interactive node  because python builds involve compilation and downloads
   that can use  a lot of  CPU time and memory. If you do this on login node
   you will have problems and your install will likely fail.

   .. code-block:: console

      [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i

2. **Load desired python module**

   For building in your user area, first you need to load Python module:

   .. code-block:: console

      [user@login-x:~]$ module load python/3.8.0

   Check that ``python`` and ``pip`` commands are available to you, the output of the commands should
   be similar to:

   .. code-block:: console

      [user@login-x:~]$ which python
      /opt/apps/python/3.8.0/bin/python

      [user@login-x:~]$ which pip
      /opt/apps/python/3.8.0/bin/pip


3. **Install your python package**

   Below we provide a common installation example and are using ``pip``
   to install :tt:`pluggy` package:.

   .. code-block:: console

      [user@login-x:~]$ pip install --user pluggy
      Collecting pluggy
        Using cached pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
      Installing collected packages: pluggy
      Successfully installed pluggy-1.0.0

   Verify that :tt:`pluggy` is now available.

   .. code-block:: console

      [user@login-x:~]$ python
      Python 3.8.0 (default, Jun  8 2022, 08:17:26)
      [GCC 8.5.0 20210514 (Red Hat 8.5.0-10)] on linux
      Type "help", "copyright", "credits" or "license" for more information.

      >>> import pluggy
      >>>

4. **Use your installed python package**

   Next time you need to use your installed python package
   simply load the same python module that you used for building the package:

   .. code-block:: console

      [user@login-x:~]$ module load python/3.8.0

   and proceed with the rest of the commands per your software instructions.

.. _install r:

Install R packages
------------------

When you want to install a specific R package you :red:`do not need to install R`.
We provide a few versions of R that can be accessed via modules.  The base
installs already have a lot of added packages. To find out what R is available:

.. code-block:: console

   [user@login-x:~]$ module avail R
   ------------ /opt/rcic/Modules/modulefiles/LANGUAGES -----------------
   R/4.0.2 R/4.0.4 R/4.1.2 R/4.2.2

You can choose either R version, however it is advisable to
use a later release.

For additional info on installing R packages via different methods please see R documentation
`Installing R packages <https://r-coder.com/install-r-packages/>`_.

Steps below explain the basic commands specific to the cluster.

R has thousands of specific packages and it is not possible for us to maintain
them all. For this reason users can easily add their desired packages
to the base installs using local user area. The local installation of R
packages will go to the :tt:`$HOME/R` and is automatically available to the user.

1. **Get an interactive node**

   Always claim an interactive node because R builds involve compilation and downloads
   that can use  a lot of  CPU time and memory. If you do this on login node
   you will have problems and your install will likely fail.

   .. code-block:: console

      [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i

2. **Load desired module**

   For building in your user area, first you need to load R module:

   .. code-block:: console

      [user@login-x:~]$ module load R/4.1.2

   Check that ``R`` command  is available to you, the output of
   the below command should be similar to:

   .. code-block:: console

      [user@login-x:~]$ which R
      /opt/apps/R/4.1.2/bin/R


3. **Start R**

   .. code-block:: console

      [user@login-x:~]$ R

   Check if your package is already installed, for example for :tt:`farver`:

   .. code-block:: console

      > packageVersion('farver')
      [1] ‘2.1.0’

   In case the package is not installed there will be an error:

   .. code-block:: console

      > packageVersion('farverB')
      Error in packageVersion("farverB") : there is no package called ‘farverB’

4. **Install your R package**

   Below we provide an example of installation of :tt:`ggfun` package  from CRAN:
   There are 3 places when you need to type a response.

   .. code-block:: console

      > install.packages("ggfun")
      Warning in install.packages("ggfun") :
        'lib = "/opt/apps/R/4.1.2/lib64/R/library"' is not writable
      Would you like to use a personal library instead? (yes/No/cancel)  # type yes
      Would you like to create a personal library
      ‘~/R/x86_64-pc-linux-gnu-library/4.1’
      to install packages into? (yes/No/cancel)                          # type yes
      --- Please select a CRAN mirror for use in this session ---
      Secure CRAN mirrors
       1: 0-Cloud [https]
       2: Australia (Canberra) [https]
             ... more lines deleted here
      71: USA (IA) [https]
      72: USA (KS) [https]
      73: USA (MI) [https]
      74: USA (OH) [https]
      75: USA (OR) [https]
      76: USA (TN) [https]
      77: USA (TX 1) [https]
      78: Uruguay [https]
      79: (other mirrors)
      Selection: 72                                                      # type number

      trying URL 'https://rweb.crmda.ku.edu/cran/src/contrib/ggfun_0.0.6.tar.gz'
      Content type 'application/x-gzip' length 148598 bytes (145 KB)
      ==================================================
      downloaded 145 KB

      * installing *source* package ‘ggfun’ ...
      ** package ‘ggfun’ successfully unpacked and MD5 sums checked
      ** using staged installation
      ** R
      ** inst
      ** byte-compile and prepare package for lazy loading
      ** help
      ** installing help indices
      ** building package indices
      ** installing vignettes
      ** testing if installed package can be loaded from temporary location
      ** testing if installed package can be loaded from final location
      ** testing if installed package keeps a record of temporary installation path
      * DONE (ggfun)

      The downloaded source packages are in
          ‘/tmp/Rtmpg5SeVX/downloaded_packages’

   Your typed responses:

   * The warning at the beginning of output is normal as users cant write in the system area.
     Type :tt:`yes` to confirms to use a local library in your user area.
   * Type :tt:`yes` to confirms a creation of personal library. This is done once. Future
     installs will use this existing location.
   * There are many CRAN mirrors where R packages are available. Please select the USA mirror
     and type its number.

5. **Use your installed R package**

   Next time you need to use your installed R package
   simply load the same R module that you used for building the package:

   .. code-block:: console

      [user@login-x:~]$ module load R/4.1.2

   and proceed with the rest of the commands per your software instructions.

.. _install perl:

Install Perl modules
--------------------

Perl has thousands of specific packages and it is not possible for us to maintain
them all. For this reason users can easily add their desired packages
to the base installs using local user area. The local installation of Perl
packages will go to the :tt:`$HOME/perl5` and will be automatically available to the user.

When you want to install a specific Perl module
you :red:`do not need to install perl, cpan or cpanm`.
We provide a few Perl versions that can be accessed via modules.
The base installs already have a lot of added packages.

To find out what Perl is available:

.. code-block:: console

   [user@login-x:~]$ module avail perl
   ----------------- /opt/rcic/Modules/modulefiles/LANGUAGES ----------------------
   perl/5.30.0   perl/5.34.1

For a detailed info on installing Perl packages please see
`How to Install Perl CPAN modules <http://www.cpan.org/modules/INSTALL.html>`_

Steps below explain the basic commands specific to the cluster.


1. **Verify local perl directory**

   Make sure that :tt:`$HOME/perl5` exists and if it does not, create it:

   .. code-block:: console

      [user@login-x:~]$ cd $HOME
      [user@login-x:~]$ ls perl5
      ls: cannot access 'perl5': No such file or directory

      [user@login-x:~]$ mkdir $HOME/perl5

   .. note:: Creation of :tt:`$HOME/perl5` needs to be done only once, the name should
             not be changed to another arbitrary name.

2. **Get an interactive node**

   Always claim an interactive node because perl builds involve compilation and downloads
   that can use  a lot of  CPU time and memory. If you do this on login node
   you will have problems and your install will likely fail.

   .. code-block:: console

      [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i

3. **Load desired perl module**

   For building in your user area, first you need to load Perl module, for example:

   .. code-block:: console

      [user@login-x:~]$ module load perl/5.30.0

  Check that ``perl`` and ``cpanm`` are available,
  the output of the commands below will be similar to:

   .. code-block:: console

      [user@login-x:~]$ which perl
      /opt/apps/perl/5.30.0/bin/perl

      [user@login-x:~]$ which cpanm
      /opt/apps/perl/5.30.0/bin/cpanm

4. **Install your software package**

   Below we provide an installation example for package :tt:`X::Tiny` using ``cpanm``:

   .. code-block:: console

      [user@login-x:~]$ cpanm X::Tiny
      --> Working on X::Tiny
      Fetching http://www.cpan.org/authors/id/F/FE/FELIPE/X-Tiny-0.21.tar.gz ... OK
      Configuring X-Tiny-0.21 ... OK
      ==> Found dependencies: Test::FailWarnings
      --> Working on Test::FailWarnings
      Fetching http://www.cpan.org/authors/id/D/DA/D.../Test-FailWarnings-0.008.tar.gz ... OK
      Configuring Test-FailWarnings-0.008 ... OK
      Building and testing Test-FailWarnings-0.008 ... OK
      Successfully installed Test-FailWarnings-0.008
      Building and testing X-Tiny-0.21 ... OK
      Successfully installed X-Tiny-0.21
      2 distributions installed

   Check that the installed module is found and can be loaded by ``perl``:

   .. code-block:: console

      [user@login-x:~]$ perl -e "use X::Tiny"

   The command should produce no errors and no output, this means ``perl`` found
   the installed package.

5. **Using your installed perl package**

   When you need to use your installed packages simply load the same
   perl module that was used for the installation:

   .. code-block:: console

      [user@login-x:~]$ module load perl/5.30.0

   and proceed with using your packages per your software instructions.

.. _install singularity:

Create Singularity Containers
-----------------------------

.. attention:: We do not provide Docker containers on the cluster due to security.

Sometime people need to create containers for running specific versions of
applications or sets of applications.
We provide Singularity containers that can be built and used from Docker recipes.

For in-depth guide please see
`SingularityCE User Guide <https://docs.sylabs.io/guides/3.9/user-guide/introduction.html>`_

When you want to build a Singularity container you :red:`do not need to install Singularity`.
We provide a few versions of Singularity and its prerequisites that can be accessed via modules.

The following steps include what is specific to the cluster and can be used as
a guide to create your own container using Singularity that is already installed.

To find out what Singularity is available:

.. code-block:: console

   [user@login-x:~]$ module avail singularity
   ------------ /opt/rcic/Modules/modulefiles/LANGUAGES -----------------
   singularity/3.4.1  singularity/3.7.2  singularity/3.9.4

If you have never built container before we suggest to use the
latest available singularity version.

1. **Get an interactive node**

   Always claim an interactive node because Singularity builds involve compilation and downloads
   that can use  a lot of  CPU time and memory. If you do this on login node
   you will have problems and your install will likely fail.

   In addition, Singularity container can be large, we recommend to use your
   private  area in :tt:`/pub/ucinetid` or  your group lab
   allocation on another DFS file system for building the images.

   .. code-block:: console

      [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i
      [user@login-x:~]$ cd /pub/ucinetid

2. **Load desired singularity module**

   For building in your user area, first you need to load Singularity module:

   .. code-block:: console

      [user@login-x:~]$ module load singularity/3.9.4

3. **Run a container create command**

   Follow your specific software instructions for your build.
   Singularity  containers can be created in two ways:

   3a. **Create from a download of pre-built images**

       This is done from a known URL (provided by your desired software).
       The following example command is for creating a :tt:`vg` container with specific software from
       an available docker image:

       .. code-block:: console

          [user@login-x:~]$ singularity pull vg.sif docker://quay.io/vgteam/vg:v1.43.0
          INFO:    Converting OCI blobs to SIF format
          INFO:    Starting build...
          Getting image source signatures
          Copying blob 3b65ec22a9e9 done
          Copying blob 9a050ffbf404 done
          Copying blob 0ac4b81e8d78 done
          ... < cut lines> ...
          Copying blob 4643aa901e21 done
          Copying config d5ad26ca01 done
          Writing manifest to image destination
          Storing signatures
          2022/10/14 10:03:57  info unpack layer: sha256:3b65ec22a9e96affe680712973e88355927506aa3f792ff03330f3a3eb601a98
          2022/10/14 10:03:58  info unpack layer: sha256:9a050ffbf4047ecc30a36cccf582a79bc6adc73474ea153d6607285a7d0a0a07
          ... <cut lines > ...
          2022/10/14 10:04:10  info unpack layer: sha256:4643aa901e21e5ccd09d3364191354accb44ade3d443f4b04dd0110d8fe6ffcf
          INFO:    Creating SIF file...


       A successful build will result in creating :tt:`vg.sif` container in the working  directory:

       .. code-block:: console

          [user@login-x:~]$ ls
          vg.sif

   3b. **Build from a recipe**

       This approach involves using a definition file (also called a recipe file)
       for building a container. The definition file can be downloaded (from your
       software provided URL) or can be created (this is more complex, and one
       needs to know the specifics what the container needs).

       .. code-block:: console

          [user@login-x:~]$ singularity build hla.simg hla.recipe

       Here, :tt:`hla.simg` is a desired Singularity container to build in the Singularity
       Image File (SIF) format, and :tt:`hla.recipe` is the container
       definition file download from the software website.

       A successful build will result in creating :tt:`hla.simg` container in the working  directory.

4. **Verify your container**

   To check the software in your new container:

   .. code-block:: console

      [user@login-x:~]$ singularity run vg.sif
      Singularity> vg version

      vg version v1.43.0 "Barisano"
      Compiled with g++ (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 on Linux
      Linked against libstd++ 20210601
      Built by root@buildkitsandbox

      Singularity> exit
      exit

5. **Use your container**

   Now you can use your container either interactively on a command line using an
   interactive node (get a node with srun) or submitting as a batch job to Slurm.

   In either case, load the same singularity module, provide a full path to
   the container image and specify arguments to your desired software command:

   .. code-block:: console

      [user@login-x:~]$ module load singularity/3.9.4
      [user@login-x:~]$ singularity run /pub/anteater/vg.sif arg1 arg2 arg3

   Additional commands to interact with the container are ``shell`` and ``exec``.
   Please see the `SingularityCE User Guide <https://docs.sylabs.io/guides/3.9/user-guide/introduction.html>`_
   for in-depth command reference.

.. _compile:

Compile software
----------------

Sometimes people need to compile specific versions of applications.
This is done according to the specific software instructions
and taking into account cluster existing modules.

In general, for compiling  one needs a compiler, some prerequisite software packages, ``make``,
``cmake`` or a few other build tools. All of these are accessible via modules.

Steps below explain the basic setup specific to the cluster.

1. **Get an interactive node**

   Always claim an interactive node because software builds involve compilation and downloads
   that can use  a lot of  CPU time and memory. If you do this on login node
   you will have problems and your install will likely fail.

   In addition, downloaded sources and temporary compilation files  can be large,
   we recommend to use your private  area in :tt:`/pub/ucinetid` or  your group lab
   allocation on another DFS file system for compiling and installing.

   .. code-block:: console

      [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i
      [user@login-x:~]$ cd /pub/ucinetid

2. **Find and load desired modules**

   Read your software instructions and figure out what modules provide what you will need
   for compilation.

   We have GCC and Intel compilers, a few versions of OpenMPI, make, cmake and
   a handful of other build tools. They are provided via different
   modules. To see what is available:

   .. code-block:: console

      [user@login-x:~]$ module avail gcc
      [user@login-x:~]$ module avail intel
      [user@login-x:~]$ module avail openmpi
      [user@login-x:~]$ module avail cmake
      [user@login-x:~]$ module avail foundation

   Note, **foundation** includes ``cmake`` plus a few other tools. See ``module display foundation/v8``
   output for details.

   Your software may have a prerequisite such as HDF5. We have a few HDF5 versions
   installed.

   For any prerequisites please check already installed modules and load if you find
   that they satisfy your software needs. See :ref:`modules` guide for
   information how to find and use modules.

   For example, if you are compiling software that needs gcc compiler, cmake,
   OpenMPI-aware HDF5 you will need to load the following modules:

   .. code-block:: console

      [user@login-x:~]$ module load cmake/3.22.1
      [user@login-x:~]$ module load hdf5/1.13.1/gcc.11.2.0-openmpi.4.1.2

   Note, that HDF5 module :tt:`hdf5/1.13.1/gcc.11.2.0-openmpi.4.1.2` name
   implies that it is compiled with GCC and OpenMPI  and their versions are listed in
   the module name.

   **If you use intel or mkl modules:**
     Intel and mkl module provide access to a number of Intel Math Kernel Libraries
     including LAPACK, SCALAPACK, BLAS and threading options. The MKL libraries can be linked with Intel
     or GNU compilers. If you are compiling your software and using **intel** or **mkl**
     modules please see external links
     `Intel MKL Documentation <https://software.intel.com/en-us/mkl/documentation/view-all>`_ and
     `Intel MKL Link Advisory <https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html#gs.o9qcu1>`_
     to help you figure out how to use them.

3. **Follow your package instructions**

   After loading the modules you can configure and compile per your package instructions.

   Many packages use ``configure`` or ``cmake`` for configuring
   and for specifying the installation location. We recommend to use your user area
   for the installation location, for example, :tt:`/pub/ucinetid/sw/`.
   The resulting install will create :tt:`bin`, :tt:`lib`, and any
   other subdirectories in :tt:`/pub/ucinetid/sw/`

4. **Create a module for your software**

   This step may be optional and depends on what your software install provides and how your
   software is built.

   For instructions on creating modules for your installed
   software please see :ref:`user installed modules`.
