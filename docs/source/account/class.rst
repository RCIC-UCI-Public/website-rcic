.. _class account:

Class Accounts
==============

We provide support for some UCI classes that need computational resources. 

:bluelight:`Class Professor`
  **Before the quarter starts** please send email to hpc-support@uci.edu
  with the following info:

    1. Class catalog name (example cs175).
    #. UCInetIDs of the class TAs. Please confirm that you delegate the TAs to
       handle class-related requests.
    #. | *Class roster - a text file with student UCInetIDs one per line*.
       | Please, do not send :tt:`.xls` or :tt:`.csv` files or links to google docs. 
       | For a short roster can copy/paste it into the email.
       | Please indicate who is a graduate level or undergraduate level student. 
    #. What type of computational access you need: CPU, GPU or both. 
    #. What amount of shared data you expect to have publicly available to the students 
       (see :tt:`public/` below). Please note, we do not provide multiple Tbs of class storage. 
    #. Class software requirements if any:

       * In general, we do not install software just for the classes.  A desired
         software may be already available on the cluster.
       * If you expect to work with conda environments, students should follow our guide
         :ref:`installing conda environments <install conda>`.

  **During the quarter** all email requests from TAs must be cc'ed to the class professor.

  **After the quarter ends** please send us a confirmation email that the class has ended and we can
  remove all class associated accounts.

:bluelight:`We will create`
  1. Student class accounts per provided roster.
  #. Slurm class accounts, and deposit a free allocation of hours:

     * *classname_class* for CPU usage, example cs175_class
     * *classname_class_gpu* for GPU usage, example cs175_class_gpu

  #. Class disk storage allocation is :tt:`/data/class/<classname>` directory, example /data/class/cs175.
     A single quota for the class is calculated as

     Quota :subscript:`GB` =  Number :subscript:`students` x 50 :subscript:`GB` + Storage in public/ :subscript:`GB`

     .. note:: We do not set per-student quotas, all students contribute to the class quota.
               A single student  can render class allocation unusable for all if exceeds the
               total storage for the class. 

     The top class directory has a specific structure where
     we provide ALL the needed class subdirectories and set ALL correct ownership and permissions.
     :underline:`Please do not change ownership and permission  to avoid problems`:
      
       * :tt:`private/` - with read/write access only by the professor and TAs.
       * :tt:`public/`  - with read access by all students and
         read/write access by the professor and TAs (to put class materials for the students).
         Let us know when requesting the class how much data you expect to  put here for the students.
       * :tt:`UCInetID/` - student class account for each UCInetID in the roster.
         A student, professor and TAs can access student class account directory.
         Each account is expected to use  50GB of total class disk space allocation.


:bluelight:`Class Students`
  1. `How to login on HPC3 <https://rcic.uci.edu/account/login.html>`_.
  #. Your class account $HOME is :tt:`/data/class/<classname>/UCInetID` and has 50GB disk quota.
     For graduate students we create :underline:`regular account` in addition to the class account.
     Regular accounts can be used after the class ends.

     If you have a :underline:`regular account` on the cluster:

     - your regular account $HOME is :tt:`/data/homezvolX/UCInetID`.
     - you have a class account in the class location (will be deleted after the class ends).
     - do not create symbolic links from your $HOME to your class account.
       Please follow `symlinks guide <https://rcic.uci.edu/guides/unix-primer.html#symbolic-links>`_.
  #. We provide guides and specific topics how to use the cluster at http://rcic.uci.edu

     * Please follow :ref:`acceptable use`
     * `Check your quotas frequently <https://rcic.uci.edu/storage/home.html#how-to-check>`_

  #. :red:`All class additions can be requested only by the professor and the designated TAs`.
  #. :red:`All class-related questions need to be directed to your class professor and TAs`. 
     We  will answer only questions regarding cluster problems. 
  #. If you wish to retain your class data, please copy what you need 
     by the time your class ends. All class accounts will be deleted after the class ends.

:bluelight:`After the class ends`
  At the beginning of the following quarter 

    * Class student accounts are removed.
    * Slurm class accounts are removed.
