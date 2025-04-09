.. _class account:

Class Accounts
==============

We provide support for some UCI classes that need computational resources. 

:bluelight:`Class Professor`
  **Before the quarter starts** please send email to hpc-support@uci.edu
  with the following info:

    * Class catalog name (example cs175) 
    * UCInetIDs of the class TAs
    * *Class roster as a text file with student UCInetIDs one per line*.
      For a short roster can copy/paste it into the email.
      Please, no :tt:`.xls` or :tt:`.csv` files or links to google docs. 
    * What type of computational access you need: CPU, GPU or both. 
    * What amount of shared data you expect to have publicly available to the students 
      (see :tt:`public/` below). Please note, we do not provide multiple Tbs of class storage. 

    If you expect to work with conda environments please follow our guide
    :ref:`installing conda environments <install conda>`.

  **After the quarter ends**: please send us a confirmation email that the class has ended and we can
  remove all class associated accounts.

:bluelight:`We will create`
  * Student class accounts per provided roster. Any student disk usage should not exceed 50GB.
  * Slurm class accounts, and deposit a free allocation of hours:

    * *classname_class* for CPU usage, example cs175_class
    * *classname_class_gpu* for GPU usage, example cs175_class_gpu

  * Your class disk storage allocation is :tt:`/data/class/<classname>` directory, and  the
    single quota for the class is Number :subscript:`students` x 50GB + Number :subscript:`GB in public/`

    Note, we do not set student-specific quotas, all students contribute to the class quota.
    A single student  can render class allocation unusable for all if exceeds the
    total storage for the class. 

    We provide all the needed class subdirectory structure and set ALL correct ownership and permissions.
    :underline:`Please do not change ownership and permission  to avoid problems`:
      
      * :tt:`private/` - with read/write access only by the professor and TAs
      * :tt:`public/`  - with read access by all students and
        read/write access by the professor and TAs (to put materials for the students).
        Let us know when requesting the class how much data you expect to  put here for the students.
      * :tt:`UCInetID/` - student class account for each UCInetID in the roster.
        A student, professor and TAs can access student class account directory.
        Each account is expected to use  50GB of total class disk space allocation.


:bluelight:`Class Students`
  * All class additions can be requested only by the professor and the designated TAs.
  * `How to login on HPC3 <https://rcic.uci.edu/account/login.html>`_.
  * Please read and follow our `Acceptable Use Policy <https://rcic.uci.edu/account/acceptable-use.html>`_.
  * Your class account $HOME is :tt:`/data/class/<classname>/UCInetID` and has 50GB disk quota.
    Check your quotas frequently, follow https://rcic.uci.edu/storage/home.html#how-to-check.
  * If you already have a :underline:`regular account` on the cluster:

      - your $HOME is your regular account
      - you have a class account in the class location (will be deleted after the class ends).
      - do not create symbolic links from your $HOME to your class account.
        Please follow `symlinks guide <https://rcic.uci.edu/guides/unix-primer.html#symbolic-links>`_.

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

