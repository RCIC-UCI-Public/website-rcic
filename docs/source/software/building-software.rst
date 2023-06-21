.. _install sw:

How to Install software
======================

.. _install conda:

Install with conda
------------------

When you need to build a specific application using conda 
you DO NOT have to install Miniconda (mini version of Anaconda) or Anaconda.
We provide a few basic Minicaonda/Anaconda versions that can be accessed via modules.
to find out what is available:

.. code-block:: console

   [user@login-x:~]$ module avail miniconda
   ----------------- /opt/rcic/Modules/modulefiles/LANGUAGES ----------------------
   miniconda3/4.8.5  miniconda3/4.12.0

   [user@login-x:~]$ module avail anaconda
   ---------------- /opt/rcic/Modules/modulefiles/LANGUAGES -----------------------
   anaconda/2020.07 anaconda/2021.11 anaconda/2022.05

You can choose either Miniconda or Anaconda depending on what is your package
installation instructions require and build your local conda environment. 
Steps below explain the basic setup specific to the cluster. 

For additional info on conda-specific commands and builds please see conda documentation
`Bulding Conda local environments <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html>`_

Usually, to install an application one needs to create a local conda environment.
To install conda environment in your user area 
follow the steps below. The example is given for the 
anaconda version 2021.11 for Python 3.9.7. The steps are the
same for other versions of conda (substitute version numbers where needed).
Your output will have your UCINetID where needed in steps below (we use as an
example panteater).

1. **Get an interactive node**

   Always claim an interactive node  because conda builds involve compilation and downloads 
   that can use  a lot of  CPU time and memory. IF you do this on login node
   you will have problems and your install will likely fail.

   .. code-block:: console

      [user@login-x:~]$ srun -c 2 -p free --pty /bin/bash -i

2. **Load desired module**

   For building in your user area, first you need to load anaconda module:

   .. code-block:: console

      [user@login-x:~]$ module load anaconda/2021.11

   Check that conda is available after module loading, the output of the
   command below should be similar to:

   .. code-block:: console

      [user@login-x:~]$ which conda
      /opt/apps/anaconda/2021.11/bin/conda


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
   The file name is :tt:`.condarc` and the text format is: 
         
   .. code-block::text

      pkgs_dirs:
        - /data/homezvol0/panteater/.conda/pkgs
        - /opt/apps/anaconda/2021.11/pkgs
      envs_dirs:
        - /data/homezvol0/panteater/.conda/envs
        - /opt/apps/anaconda/2021.11/envs

4. **Initialize conda for your shell**

   Run command:

   .. code-block:: console

      [user@login-x:~]$ conda init bash*

   This adds a few lines to your :tt:`~/.bashrc` file which may not always be desirable
   for your work with other programs.  Edit the :tt:`~/.bashrc` file and move all the lines
   added by conda into another file, for example to :tt:`*~/.mycondainit-2021.11`.
   The lines are at the end of your :tt:`~/.bashrc` file (lines start end end with conda initialize
   and all the lines between them):

   .. code-block:: bash

      # >>> conda initialize >>>
      # !! Contents within this block are managed by 'conda init' !!
      --- A FEW MORE LINES HERE WERE CUT ---
      unset __conda_setup
      # <<< conda initialize <<<

5. **Create a local environment**

   Now you are ready to :red:`follow the instructions provided by your software package` and
   can create your local conda environment. The name  can be anything
   that makes sense, has to be a single word (no spaces), the exact
   command will be provided in your software instructions and may have
   additional arguments in it. Here, as an example  we create a simple
   **Local2** environment:

   .. code-block:: console

      [user@login-x:~]$ conda create -n Local2

   This will take some time to complete, as anaconda is creating a lot
   of packages in your directory :tt:`~/.conda`  and depending on what you are 
   installing it may take 2-4Gb of space.
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
   specific software install. Now you have your
   local copy of conda where you can install packages/programs you need.

   You can build multiple local environments using the same method.

   Every time you login and want to use your conda environment and its packages you will need 
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

.. _install r:

Install R packages
------------------

.. _install perl:

Install Perl modules
--------------------

.. _install singularity:

Create Singularity Containers
-----------------------------

.. _compile:

Compiling software
------------------

**If you use intel or mkl moduls**
  Intel and mkl module provide access to a number of Intel Math Kernel Libraries
  including LAPACK, SCALAPACK, BLAS and threading options. The MKL libraries can be linked with Intel
  or GNU compilers. If you are compiling your software and using **intel** or **mkl**
  modules please see external links 
  `Intel MKL Documentation <https://software.intel.com/en-us/mkl/documentation/view-all>_` and
  `Intel MKL Link Advisory <https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-link-line-advisor.html#gs.o9qcu1>`_
  to help you figure out how to use them.
