.. _dfs:

DFS 
====

Overview
--------

Scalable storage on HPC3 in the **/dfsX**  and **/pub** file paths are parallel file systems running
`BeeGFS <https://www.beegfs.io/c/>`_ on top of `ZFS <https://zfsonlinux.org/>`_. 
This is a network-based multi-Petabyte storage cluster for the UCI campus research community.
It is put in place so that researchers across UCI have a reliable and resilient location
to store their research data and share with defined groups.

Performance of each file system is quite good (5-6 GByte/s) **when used properly**. 
Currently, there are multiple DFS systems with an aggregate throughput of more than 30 GByte/s.

.. important:: While each file system is capable, it is not too difficult for a single user to
               exceed the inherent capabilities and completely wreck performance for everyone.

It is beyond the scope of this document to describe parallel file systems in detail, but one 
should `start learning more <https://en.wikipedia.org/wiki/BeeGFS>`_ to make better use of the
file systems. 

**Take-home concepts about DFS parallel files systems are:**
  * They perform well when reading/writing large files in good-sized (> 128KB) chunks.
  * They perform very poorly when reading/writing many small files.
  * All DFS systems are *single copy, high-performance storage* intended for scratch data. 
    No special backup is available. Deleted data are gone forever.
  * Accessible only from HPC3 as a regular filesystem for storing data on the cluster.
    There are a few separate storage pools which are mounted on the cluster as **/dfsX**.
  * For recharge allocations please see buying :ref:`buy dfs`.
  * .. warning :: DFS filesystems  must not be used to store personally-identifiable information that would fall
                 under guidelines  such as `FERPA <https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html>`_
                 (e.g. Student data) and `HIPAA <https://www.hhs.gov/hipaa/index.html>`_ (health-care data).

                 If you are unsure if DFS is suitable for your data, please refer to general guidance for
                 `data security <https://research.uci.edu/compliance/human-research-protections/researchers/data-security.html>`_
                 provided by the `UCI Office of Research <https://www.research.uci.edu/>`_

.. _dfs allocations:

Allocations
-----------

There is NO separate account for DFS filesystems. 
:ref:`dfs quotas` are enforced using groups.

**No cost Private area:** 
  | All users have access to the Private Area. Each user is provided with a default allocation:
  | - 1TB quota per account in :tt:`/pub/ucinetid` (it is a short name for :tt:`/dfs8/pub/ucinetid`).
  | - 1TB backup quota for a selective backup

**Recharge allocation - Group Shared area:**
  UCI Faculty members can have low-cost recharge allocation(s) to fulfill their needs.
  These group areas are quota allocations in **/dfsX/group-lab-path** based on PI's purchase.
  The storage owner (PI) can specify additional users who have read/write capability on the filesystem.

  .. note:: If you are submitting a ticket requesting to
            be added to a specific group for a specific filesystem access, please note
            we will need your PI confirmation in order to approve your request.
            Use a cc to your PI when submitting a ticket. 

.. _dfs files:

Storing Files
-------------

**What to Store**
  * Any frequently changing files
  * Any large input data files that are used for computational jobs
  * Jobs transient input/output/error files
  * Large user-authored software installations
  
**Where to Store**
  Pick a location depending on the type of data (personal or group access)

  1. The **/pub/ucinetid** is a unique private access area. Use this for data you don't need to share with anyone.
  2. Most users have access to one or more group-shared areas in **/dfsX/<group-lab-path>**.
     Within this area, all group members have read and write access.
     The organization is up to the group members with one exception: :red:`do not change sticky bit settings`. 

**File permissions**

  .. important:: File permissions are used in determining quotas.
                 When we creat **Private area** and  **Group shared area** on DFS 
                 we set correct permissions on the top level directories. 


  .. warning:: Each group lab area is initially configured with the **group sticky bit set**
               so tht only allowed users can access this area. We advise users to NOT change
               permissions on the directories and files when writing in the group area.
               :red:`Incorrect permissions can lead to quota exceeded errors`.


  Please make sure you understand UNIX :ref:`file permissions`.


.. _dfs quotas:

Quotas
------

All DFS-based file systems have quota enforcement.  

- Every user has a default **personal group** which is the same as their login.
  The only :tt:`1TB personal quota` is on **/pub/ucinetid**, the rest are group quotas.

- Every user has a default :tt:`1Tb selective backup quota`.

- Users have :tt:`1 byte quota` on all DFS systems (except personal quota), it is the group quota
  that is used. :red:`If you create file with the incorrect group, you will likely
  see over quota errors`.

- When writing in group area users need to remember that all members of the
  group contribute to the quota. It's the sum total usage that counts.
  When quotas are exceeded, users can no longer write in the affected
  filesystem  and will need to remove some files and directories to free space.

- Users can't change quotas, but can submit a ticket asking to be added
  to the group quotas provided there is a confirmation from the PI about the change.

.. _dfs check quotas:

How to check
^^^^^^^^^^^^

For all DFS file systems  including selective backup one can use ``dfsquotas``
command to check user/group quotas on a particular DFS pool. 

**To see the quotas for user** :tt:`panteater` **on** :tt:`/dfs6`:

  .. code-block:: console

     $ dfsquotas panteater dfs6

     ==== [Group Quotas on dfs6]

     Quota information for storage pool Default (ID: 1):

           user/group     ||           size          ||    chunk files
          name     |  id  ||    used    |    hard    ||  used   |  hard
     --------------|------||------------|------------||---------|---------
      panteater_lab|012345||   26.25 TiB|   50.00 TiB||  1310459| 18500000  # see 1
        alpha_users|158537||      0 Byte|      1 Byte||        0|        1  # see 2
          panteater|000865||  755.59 GiB| 1024.00 GiB||   258856|unlimited  # see 3

  The above shows that a user :tt:`panteater`:

  1. can write in the allocation for the group :tt:`panteater_lab`
     where the total space is 50Tb and ~26Tb of it is already used. Note, space
     used by the group include all users allowed to write in this area.
  2. :tt:`panteater` belongs to a supplementary group :tt:`alpha_users`, this group
     has no allocation (1 byte) and the user will not be able to store any files
     that have this group ownership.
  3. can write in personal :tt:`/pub/panteater` area, where the default allocation
     is 1Tb (1Tb = 1024Gb) and ~756Gb is already used by the user.

**To see the quotas for selective backup:**

  .. code-block:: console

     $ dfsquotas panteater sbak

**To see the quotas for** :tt:`dfs6` **and selective backup:**

  .. code-block:: console

     $ dfsquotas panteater "dfs6 sbak"


.. _dfs over quota:

Over quotas
^^^^^^^^^^^

When quota is filled, the users will not be able to write any files 
or directories and submitted jobs will fail with :red:`quota exceeded errors`

Quota is enforced by the file system based upon the :tt:`Unix group membership`
of a particular file.  For example,

.. code-block:: console

   $ ls -l
   total 55524423
   drwxrwsr-x  7 panteater bio                 7 Aug  5  2019 biofiles
   -rw-r--r--  1 panteater panteater  4294967296 May 31  2019 performance.tst
   drwxrwsr-x  3 panteater panteater           2 Oct  8 17:11 myfiles


The user :tt:`panteater` is storing files under two different groups:
- the file :tt:`performance.tst` is charged to the :tt:`panteater` group quota
- the files in the subdirectory :tt:`biofiles` are charged to the :tt:`bio` group quota.

Examine the permissions of the directories: :tt:`drwxrwsr-x`. Notice the :tt:`s` for 
the group execute permissions (character positions 5-7). This is called the **sticky bit** for the directory.
It is subtle, but important difference: :tt:`x` instead of :tt:`s` in the group execute permission.
Compare to permissions without sticky bit: 

.. _sticky bit:

.. table::
   :class: noscroll-table

   +--------------+------------------+-----------------------------------------------------------------+
   |  Sticky  bit | Directory mode   | Description                                                     |
   +==============+==================+=================================================================+
   |              | :tt:`drwxrwsr-x` | In the origin directory, created files and directories are      | 
   | is set       |                  | written with the group permissions :tt:`rws`  of the origin     |
   |              |                  | directory and the sticky bit is set.                            |
   +--------------+------------------+-----------------------------------------------------------------+
   |              | :tt:`drwxrwxr-x` | In the origin directory, created files and directories are      |
   |              |                  | written with the active UNIX group permissions :tt:`rwx` of the |
   | is not set   |                  | origin directory, which defaults to your login.                 |     
   +--------------+------------------+-----------------------------------------------------------------+

The Unix command ``newgrp`` can be used to change the active Unix group.
Please type ``man newgrp`` to learn about this command.

**Reasons for Over Quota**
  1. Under normal operation, when the sticky bit is set on a directory, the correct quota enforcement 
     occurs automatically because files and subdirectories are written with correct group.
     When all space is used over quota is issued. 
  2. The most common quota problems on DFS result from inadvertently removing 
     the sticky bit on a directory and then writing with the default (user personal group).
     In this case writing files and running  jobs can fail.
  3. Moving data to HPC3 with software that overrides the sticky bit by explicitly setting 
     permissions in the most common way a sticky bit becomes unset.

     .. note:: Please see :doc:`data-transfer` for information how to 
               move data to the cluster.


.. _fix dfs overquota:

Fix over quotas
^^^^^^^^^^^^^^^

**Fixing Permissions**
  You can use the ``chmod`` command to fix directories that don't have a sticky bit set,
  but should.  The following command  will add the sticky bit to a particular directory.

  .. code-block:: console

     $ chmod g+s directory-name

  You can use the ``find`` command to find all directories in a subtree and
  combine it with ``chmod`` command to set the sticky bit on all found
  directories:

  .. code-block:: console
  
     $ find . -type d -exec chmod g+s {} \; -print

**Fixing Group Ownership**
  You can also use the ``chgrp`` command to change the group ownership of 
  a file or directory. For example, to change the group from :tt:`panteater` to :tt:`bio`
  on a specific file (or directory):

  .. code-block:: console
  
     $ ls -l performance.txt
     -rw-r--r--  1 panteater panteater  4294967296 May 31  2019 performance.tst
     $ chgrp bio performance.txt
     $ ls -l performance.txt
     -rw-r--r--  1 panteater bio        4294967296 May 31  2019 performance.tst

  The :tt:`ls -l` command is used to show permissions before and after the change. 

.. _selective backup:

Selective Backup
----------------

*We cannot backup everything on the cluster*. Selective Backup allows the
users to choose what is important and have it automatically saved. The physical
location of the backup server is different from the cluster location for extra protection.

.. note:: You will want to backup only critical data such as scripts, programs, etc.

.. warning:: DO NOT backup data you can get from other sources, especially large data-sets.

.. important:: If you go past your backup quota then backups stops
               for your account. The backup will fail as no new data
               can be written to the backup server since you reached your limit.

.. _selective backup default:

Default settings
^^^^^^^^^^^^^^^^

The Selective Backup is based on ``rsync`` in conjunction with GNU Parallel. The combination
maximizes the network throughput and server capabilities in order to backup hundreds of
user accounts from multiple public and private filesystems.

The Selective Backup process will automatically start saving your home directory
as well as some public and private disk spaces. 

.. note:: | For a majority of users defauls are sufficient. 
          | There is nothing for you to do if you like the defaults.

Users manage their Selective Backup via two **control files** located in their
:tt:`$HOME` directory:

1. **.hpc-selective-backup**
   This file  lists (1) backup options and the (2) files/directories names to be saved in order of
   priority from the most to the least important. All backup options are initially commented out.

   The files are backed in the order as they are listed. That way, if a user runs out of
   selective disk quota before all listed files have been backed up, at least their most
   prized data are saved.  By default, this file contains :tt:`$HOME` and
   :tt:`/pub` areas of your account:

   .. code-block:: bash

      /data/homezvolX/ucinetid
      /pub/ucinetid

   The following table lists all available backup options:

   .. table::
      :class: noscroll-table
   
      +--------------------------+------------------------------------------------------------------+
      |  Selective Bakup Option  | What it does                                                     |
      +==========================+==================================================================+
      | HPC_SEND_EMAIL_SUMMARY   | Sends you daily email summaries of your saves.                   | 
      |                          | *Default is NO summary email notifications*.                     |
      +--------------------------+------------------------------------------------------------------+
      | HPC_SEND_EMAIL_ON_ERROR  | You will receive an email only if rsync completes with an error. |
      |                          | Error being non-zero exit status from rsync.                     |
      |                          | Consult the ``man rsync`` page for error values and meaning.     | 
      |                          | *Default is NO email notifications.*                             |
      +--------------------------+------------------------------------------------------------------+
      | HPC_KEEP_DELETED=X       | Keep deleted files on the backup server for X days where X       |
      |                          | is a number in 0-90 range.  Deleted files are files you removed  |
      |                          | from the source location.  *Default is 14 days.*                 |
      +--------------------------+------------------------------------------------------------------+

2. **.hpc-selective-backup-exclude**
   This file lists file/directories names you want to exclude from backup.
   By default, this file excludes ZFS  snapshots from :tt:`$HOME`:

   .. code-block:: bash

      $HOME/.zfs

   For more information on ``rsync`` exclude patterns please see the "ANCHORING
   INCLUDE/EXCLUDE PATTERNS” section of ``man rsync`` command output.


.. _selective backup custom:

Custom settings
^^^^^^^^^^^^^^^

To customize, edit control files with your favorite editor.
We highly recommend the following:

1. **request email notifications** to make sure things are working

   Choose one of two *SEND_EMAIL* options in :tt:`.hpc-selective-backup` file
   and uncomment it (remove the :tt:`#` sign at the beginning of the line).
   For example, if you choose to receive email notifications in the event of errors,
   edit your configuration file and change the line:

   .. code-block:: console

      # HPC_SEND_EMAIL_ON_ERROR

   to:

   .. code-block:: console

      HPC_SEND_EMAIL_ON_ERROR

2. **perform some spot checks** of what you think is being saved
   to make sure your data is indeed being backed-up.

.. _selective backup location:

Where backups are
^^^^^^^^^^^^^^^^^

A user can access backup files on the login nodes of the cluster
from the following paths:

**/sbak/selective-backup/hpc-backups/ucinetid/data/homezvolX/ucinetid**
  for user $HOME
**/sbak/selective-backup/hpc-backups/ucinetid/pub/ucinetid**
 for /pub/$USER/
**/sbak/selective-backup/hpc-backups/ucinetid/DELETED-FILES/$DATE**
  for deleted files by date, count towards backup quota.
**/sbak/selective-backup/hpc-logs/$DATE/ucinetid**
  for backup logs are available for the past X days where X is defined
  in *HPC_KEEP_DELETED=X* in your :t:`.hpc-selective-backup` 
  
.. _selective backup recovery:

Deleted files recovery
^^^^^^^^^^^^^^^^^^^^^^

.. note:: Deleted files and directories can be recovered provided they exist in the selective backup.
          Note: You have to be on a login node to access backup files.

Here is a general procedure for user :tt:`panteater` to restore accidentally 
deleted directory :tt:`spring-2022` and files in it.

.. code-block:: console

   $ cd /sbak/selective-backup/hpc-backups/panteater/DELETED-FILES   # see 1
   $ find . -type d -name spring-2022                                # see 2
   ./2022-0621/pub/panteater/spring-2022
   ./2022-0629/pub/panteater/spring-2022
   $ ls ./2022-0629/pub/panteater/spring-2022/                       # see 3
   schedule1    schedule1.sub   slurm.template
   $ cp -p -r ./2022-0629/pub/panteater/spring-2022 /pub/panteater   # see 4

The above commands mean:

1. This command puts you at the top level of a backup directory for your files.
2. This command finds all backups by date where the desired directory exists.
3. Run ``ls`` command for the specific snapshot to see if it has needed files.
4. If needed files exists in the backup, user can copy the files back to the pub directory.
   It is recommended to use ``-p`` and ``-r`` options. Option ``-p`` makes sure that
   copy command preserves the time stamp and the ownership of a file. 
   Option ``-r`` means "copy recursively", this is needed when copying a directory and its contents.
