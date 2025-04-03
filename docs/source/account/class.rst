.. _class account:

Class Accounts
==============

We provide support for some UCI classes that need computational resources. 

:bluelight:`Class Professor`
  **Before the quarter starts** please send email to hpc-support@uci.edu
  with the following info:

    * Class catalog name (example cs175) 
    * UCInetIDs of the class TAs
    * Class roster as a text file with student UCInetIDs one per line. No .xls or .csv files please. 
    * What type of computational access you need: CPU, GPU or both. 
    * What amount of shared data you expect to have publicly available to the students 
      (see :tt:`public/` below). Please note, we do not provide multiple Tbs of class storage. 

  **After the quarter ends**: please send us a confirmation email that the class has ended and we can
  remove all class associated accounts.

:bluelight:`We will create`
  * The disk quota for class allocation is Number :subscript:`students` x 50GB + Number :subscript:`Gb in public/`

    Note, this is a single class quota, we do not set student-specific quotas.
    A single student  can render class allocation unusable for all if exceeds the
    total storage for the class. 

  * Slurm class accounts and deposit a free allocation of hours:

    * *classname_class* for CPU usage, example cs175_class
    * *classname_class_gpu* for GPU usage, example cs175_class_gpu

  * Your class location is :tt:`/data/class/<classname>` directory.
    We make the needed subdirectory structure and set ALL correct ownership and permissions.
    :underline:`Please do not change them to avoid problems.`

    This class location will hold subdirectories:
      
      * :tt:`private/` - with read/write access only by the professor and TAs
      * :tt:`public/`  - with read access by all students and
        read/write access by the professor and TAs (to put materials for the students).
        Let us know when requesting the class how much data you expect to  put here for the students.
      * :tt:`UCInetID/` - student class account for each UCInetID in the roster.
        Each account has 50GB allocation of disk space.

:bluelight:`Class Students`
  * All class additions can be requested only by the professor and the designated TAs.
  * Your class account $HOME is :tt:`/data/class/<classname>/UCInetID` and has 50GB disk quota.
    Check your quotas frequently, follow https://rcic.uci.edu/storage/home.html#how-to-check.
  * If you already have a :underline:`regular account` on the cluster:

      - your $HOME is your regular account
      - you have a class account in the class location (will be deleted after the class ends).
      - do not create symbolic links from your $HOME to your class account.
        Please follow `symlinks guide <https://rcic.uci.edu/guides/unix-primer.html#symbolic-links>`_.

  * Please read and follow our `Acceptable Use Policy <https://rcic.uci.edu/account/acceptable-use.html>`_.
  * We provide guides and specific topics how to use the cluster at http://rcic.uci.edu
  * All class-related questions need to be directed to your class professor and TAs. 
    We  will answer only questions regarding cluster problems. 
  * If you wish to retain your class data, please copy what you need 
    by the time your class ends. All class accounts will be deleted after the
    class ends.

:bluelight:`After the class ends`
  At the beginning of the following quarter 

    * Slurm class accounts are removed.
    * Slurm class student accounts are removed from :tt:`/data/class/<classname>`.

