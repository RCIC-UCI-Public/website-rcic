.. _dfs:

DFS 
====

.. contents::
   :local:

Overview
--------

Scalable storage on HPC3 in the :tt:`/dfsX`  and :tt:`/pub` file paths are parallel file systems running
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
    There are a few separate storage pools which are mounted on the cluster as :tt:`/dfsX`.
  * For recharge allocations please see :ref:`buy dfs`.
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

**No cost allocation -  Private area:** 
  All users have access to the Private Area. Each user is provided with a default allocation:

  | - 1TB quota per account in :tt:`/pub/ucinetid` 
  | - 1TB backup quota for a selective backup

**Recharge allocation - Group shared area:**
  UCI Faculty members (PIs) can have low-cost recharge allocation(s) to fulfill their needs.
  
  * These group areas are quota allocations in :tt:`/dfsX/group-lab-path` based on PI's purchase.
  * The PI is the storage owner. 
  * The PI can specify additional users who can have read and write access to the area.
  * Please see :ref:`Recharge Allocations <recharge allocations>` for details
    how to purchase. 

.. _dfs files:

Storing Files
-------------

**What to Store**
  * Any frequently changing files
  * Any large input data files that are used for computational jobs
  * Jobs transient input/output/error files
  * Large user-authored  or third-party software installations
  
**Where to Store**
  Pick a location depending on the type of data (private or group access):

  :tt:`/pub/ucinetid`
    * is a unique PRIVATE access area
    * :red:`is NOT shared with other users`
    * :red:`do NOT change this directory permissions`
    * the organization of files and directories is up to the user

  :tt:`/dfsX/<group-lab-path>`
    * is a specific group shared area, users may have access to one or more group areas
    * :red:`all group members have read and write access`
    * :red:`do NOT change directories permissions or sticky bit settings`, see a warning below
    * the organization of files and directories is up to the group members

**File permissions**

  | File permissions are used in determining quotas.
  | The permissions involve setting logical UNIX groups. 

  .. important:: When we create **Private areas** and  **Group shared areas** on DFS 
                 we set correct permissions on the top level directories. 

  .. _sticky warning:

  .. warning:: * Each **Group shared area** is initially configured with the **group sticky bit set**
                 so that only allowed users can access this area.
               * We advise users to NOT change permissions on the directories and files when writing in the group area.
               * :red:`Incorrect permissions can lead to quota exceeded errors`.

  Please see :ref:`unix primer`  to familiarize yourself with UNIX groups
  and make sure you understand UNIX :ref:`file permissions`.

.. _dfs quotas:

Quotas
------

All DFS-based file systems have quota enforcement for all private and group shared areas.  

- When writing in **Private area** users need to remember that:

  * Every user has a **default personal group** which is the same as their login.
  * The :tt:`1TB personal group quota` is on **/pub/ucinetid**.
  * Every user has a default :tt:`1Tb selective backup quota`.


- When writing in **Group shared area** users need to remember that:

  * All members of the group contribute to the quota. It's the sum total usage that counts.
  * :red:`There are no individual user quotas in the Group shared area`, only the group quota is used.
  * :red:`If you create file with the incorrect group, you will likely see over quota errors`.
  * When quotas are exceeded, all users in the group will no longer be able to write in the affected
    filesystem  and will need to remove some files and directories to free space.

- Users can't change quotas, but a PI can submit a ticket asking to update the
  quota. Please see :ref:`buy dfs`.

- Users can submit a ticket asking to be added to the group shared area.

  .. note:: If you are submitting a ticket requesting to
            be added to a specific group for a specific filesystem access, please note
            we will need your PI confirmation in order to approve your request.
            Use a cc to your PI when submitting a ticket. The PI must confirm 
            the requested change via email reply.

.. _dfs check quotas:

How to check
^^^^^^^^^^^^

For all DFS file systems  including selective backup one can use ``dfsquotas``
command to check user/group quotas on a particular DFS pool. 

**To see the quotas for user** :tt:`panteater` **on private allocation in** :tt:`/dfs6`:

  .. code-block:: console

     $ dfsquotas panteater dfs6

	 ==== Group quotas on dfs6 for user panteater
     ----------------------------------------------------------------------------
                    Group      ||          Size            ||    Chunk Files         
                 name | id     ||      used  | allocated   ||    used | allocated   
     -----------------------------------------------------------------------------
      panteater_lab   | 012345 ||  26.25 GiB | 1024.00 GiB || 1310459 | unlimited  # see 1
          alpha_users | 158537 ||     0 Byte | 1024.00 Gib ||       0 | unlimited  # see 2
          panteater   | 000865 || 755.59 GiB | 1024.00 GiB ||  258856 | unlimited  # see 3

  The above shows that a user :tt:`panteater` can write in its private
  area :tt:`/pub/panteater` using the above listed 3 groups:

  1. :tt:`panteater` belongs to a supplementary group :tt:`panteater_lab`, and
     wrote 26.25Gb of data.
  2. :tt:`panteater` belongs to a supplementary group :tt:`alpha_users`, and
     did not write any files  using this group, but can if needed.
  3. using a default :tt:`panteater` group  user wrote
     ~756Gb of total allocation of 1Tb (1Tb = 1024Gb).

  .. note:: Listed above groups are logical UNIX groups associated with the user account,
            and the primary use of such groups is to assign "group ownership" of files and directories.
            The 1Tb allocation is a total space that can be used by all listed
            user UNIX groups combined, not by each group individually.

**To see the quotas for user** :tt:`panteater` **in lab shared allocation in** :tt:`/dfs9`:

  .. code-block:: console

     $ dfsquotas panteater dfs9

	 ==== Group quotas on dfs9 for user panteater
     ----------------------------------------------------------------------------
                    Group      ||          Size            ||    Chunk Files         
                 name | id     ||      used  | allocated   ||    used | allocated   
     -----------------------------------------------------------------------------
        panteater_lab | 012345 ||   38.36 TiB|   40.00 TiB || 1310459 | unlimited  # see 4
          alpha_users | 158537 ||      0 byte|    1   byte ||       0 |         1  # see 5
            panteater | 000865 ||      0 byte|    1   byte ||       0 |         1  # see 5

  4. The above shows that user :tt:`panteater` can write in its group allocation on :tt:`dfs9`
     only if using UNIX group :tt:`panteater_lab` for which there is 40Tb
     allocation.  Note, the allocated space 40Tb and the used space 38.36Tb
     are totals by all users allowed to write in this area.
  5. There is 0 quota (shown as 1 byte) for a default personal group
     :tt:`panteater` or a supplemental UNIX group :tt:`alpha_users`. If a user tries
     to write  using these UNIX groups it will result in permissions and over the quota errors.

..  next two blocks are commented out 

..  **To see the quotas for selective backup:**

     .. code-block:: console

        $ dfsquotas panteater sbak

**To see the quotas on all DFS filesystemss**:

  .. code-block:: console

     $ dfsquotas panteater all

     ==== Group quotas on dfs3b for user panteater
     No quotas to report

     ==== Group quotas on dfs4 for user panteater
     No quotas to report

     ==== Group quotas on dfs5 for user panteater
     No quotas to report

	 ==== Group quotas on dfs6 for user panteater
     ----------------------------------------------------------------------------
                    Group      ||          Size            ||    Chunk Files         
                 name | id     ||      used  | allocated   ||    used | allocated   
     -----------------------------------------------------------------------------
      panteater_lab   | 012345 ||  26.25 GiB | 1024.00 GiB || 1310459 | unlimited
          alpha_users | 158537 ||     0 Byte | 1024.00 Gib ||       0 | unlimited
          panteater   | 000865 || 755.59 GiB | 1024.00 GiB ||  258856 | unlimited

     ==== Group quotas on dfs7 for user panteater
     No quotas to report

     ==== Group quotas on dfs8 for user panteater
     No quotas to report

	 ==== Group quotas on dfs9 for user panteater
     ----------------------------------------------------------------------------
                    Group      ||          Size            ||    Chunk Files         
                 name | id     ||      used  | allocated   ||    used | allocated   
     -----------------------------------------------------------------------------
        panteater_lab | 012345 ||   38.36 TiB|   40.00 TiB || 1310459 | unlimited
          alpha_users | 158537 ||      0 byte|    1   byte ||       0 |         1
            panteater | 000865 ||      0 byte|    1   byte ||       0 |         1


  When you see **No quotas to report** it means there are no quotas for the
  user on this specific DFS filesystem.


.. _dfs over quota:

Over quotas
^^^^^^^^^^^

When quota is filled, the users will not be able to write any files 
or directories and submitted jobs will fail with :red:`quota exceeded errors`.

Quota is enforced by the file system based upon the :tt:`Unix group membership`
of a particular file.  For example:

.. code-block:: console

   $ ls -l
   total 55524423
   drwxrwsr-x  7 panteater bio                 7 Aug  5  2019 biofiles
   -rw-r--r--  1 panteater panteater  4294967296 May 31  2019 performance.tst
   drwxrwsr-x  3 panteater panteater           2 Oct  8 17:11 myfiles


The user :tt:`panteater` is storing files under two different groups:

- the files in the subdirectory **biofiles** are charged to the :tt:`bio` group quota.
- the file **performance.tst** and subdirectory **myfiles** are charged to the :tt:`panteater` group quota

Examine the permissions of the directories: :tt:`drwxrwsr-x`. Notice the :tt:`s` for 
the group execute permissions (character positions 5-7). This is called the **sticky bit** for the directory.
It is subtle, but important difference: :tt:`x` instead of :tt:`s` in the group execute permission.
Compare to permissions without sticky bit: 


.. _sticky bit:

.. table::
   :widths: 15,15,70
   :class: noscroll-table

   +------------+---------------------------------------+-----------------------------------------------------------------+
   | Sticky  bit| Directory mode                        | Description                                                     |
   +============+=======================================+=================================================================+
   |            | :gray:`drwx`:red:`rws`:gray:`r-x`     | In the origin directory, created files and directories are      |
   | is set     |                                       | written with the group permissions :red:`rws` of the origin     |
   |            |                                       | directory. The sticky bit :red:`s` is set.                      |
   +------------+---------------------------------------+-----------------------------------------------------------------+
   |            |:gray:`drwx`:bluelight:`rwx`:gray:`r-x`| In the origin directory, created files and directories are      |
   |            |                                       | written with the active UNIX group permissions :bluelight:`rwx` |
   | is NOT set |                                       | of the origin directory, which defaults to your login.          |
   +------------+---------------------------------------+-----------------------------------------------------------------+

The Unix command ``newgrp`` can be used to change the active Unix group.

For example, the user :tt:`panteater` by default has a group :tt:`panteater`.
The following sequence of simple commands shows the ownership of the files
created under different groups and shows how to use ``newgrp`` command.

.. code-block:: console

   $ id panteater
   uid=1234567(panteater) gid=1234567(panteater) groups=1234567(panteater),158571(bio)
   $ touch aaa
   $ ls -l aaa
   -rw-rw-r-- 1 panteater panteater 0 Nov  3 14:57 aaa

   $ newgrp bio
   $ touch bbb
   $ ls -l bbb
   -rw-rw-r-- 1 panteater bio 0 Nov  3 14:57 bbb

Please type ``man newgrp`` to learn about this command.

**Reasons for Over Quota**
  1. Under normal operation, when the sticky bit is set on a directory, the correct quota enforcement 
     occurs automatically because files and subdirectories are written with
     correct group, no ``newgrp`` command is needed.  When all space is used over quota is issued.
  2. The most common quota problems on DFS result from:

     * inadvertently removing the sticky bit on a directory and then writing with the default personal group.
     * changing the group ownership of a file or directory and then trying to write to it with the default personal group.

     In these cases writing files and running jobs can fail.
  3. Moving data to HPC3 with software that overrides the sticky bit by explicitly setting 
     permissions in the most common way a sticky bit becomes unset.

     .. note:: Please see :doc:`data-transfer` for information how to 
               move data to the cluster.


.. _fix dfs overquota:

Fix over quotas
^^^^^^^^^^^^^^^

**Fixing Permissions**
  You can use the ``chmod`` command to fix directories that don't have a sticky bit set,
  but should have. The following command  will add the sticky bit to a particular directory.

  .. code-block:: console

     $ chmod g+s directory-name

  You can use the ``find`` command to find all directories in a subtree and
  combine it with ``chmod`` command to set the sticky bit on all found
  directories:

  .. code-block:: console
  
     $ find . -type d -exec chmod g+s {} \; -print

**Fixing Group Ownership**
  You can also use the ``chgrp``  and ``chown`` commands to change the group ownership of
  a file or directory. For example, to change the group from :tt:`panteater` to :tt:`bio`
  on a specific file or directory:

  .. code-block:: console
  
     $ ls -l
     total 55524423
     drwxrwsr-x  7 panteater bio                 7 Aug  5  2019 biofiles
     -rw-r--r--  1 panteater panteater  4294967296 May 31  2019 performance.tst
     drwxrwsr-x  3 panteater panteater           2 Oct  8 17:11 myfiles

     $ chgrp bio performance.txt
     $ chown -R panteater:bio myfiles
     $ ls -l
     total 55524423
     drwxrwsr-x  7 panteater bio                 7 Aug  5  2019 biofiles
     -rw-r--r--  1 panteater bio        4294967296 May 31  2019 performance.tst
     drwxrwsr-x  3 panteater bio                 2 Oct  8 17:11 myfiles


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

.. table::
   :widths: 15,85
   :class: noscroll-table

   +------------------------------------------------------+-------------------------------+
   | Where                                                | What                          |
   +======================================================+===============================+
   | /sbak/zvolX/backups/ucinetid/data/homezvolX/ucinetid | user $HOME                    |
   +------------------------------------------------------+-------------------------------+
   | /sbak/zvolX/backups/ucinetid/pub/ucinetid            | /pub/$USER/                   |
   +------------------------------------------------------+-------------------------------+
   | /sbak/zvolX/backups/ucinetid/DELETED-FILES           | deleted files by date         |
   |                                                      | (counts towards backup quota) |
   +------------------------------------------------------+-------------------------------+
   | /sbak/zvolX/logs/$DATE/ucinetid                      | backup logs by date,          |
   |                                                      | available for the past Y days |
   +------------------------------------------------------+-------------------------------+

.. note:: | The :tt:`X` in :tt:`/sbak/zvolX`  maps to the volume number shown
            in your :tt:`$HOME` variable. In other words, the mapping is:
          |     /data/homezvol0 ->  /sbak/zvol0/backups
          |     /data/homezvol1 ->  /sbak/zvol1/backups
          |     /data/homezvol2 ->  /sbak/zvol2/backups
          |     /data/homezvol3 ->  /sbak/zvol3/backups

          | The number of days :tt:`Y` is defined by :tt:`HPC_KEEP_DELETED=Y` in your :tt:`.hpc-selective-backup`

.. _selective backup recovery:

Deleted Files Recovery
----------------------

.. note:: | Deleted files and directories can be recovered provided they exist in the selective backup.
          | You have to be on a login node to access backup files.

Below is a general procedure for user :tt:`panteater` to restore accidentally
deleted from :tt:`/pub/panteater` directory :tt:`spring-2022` and files in it.

.. code-block:: console

   $ cd /sbak/zvol0/backups/panteater/DELETED-FILES                  # see 1
   $ find . -type d -name spring-2022                                # see 2
   ./2024-0214/pub/panteater/spring-2022
   ./2024-0213/pub/panteater/spring-2022

   $ ls ./2024-0214/pub/panteater/spring-2022/                       # see 3
   schedule1    schedule1.sub   slurm.template

   $ cp -p -r ./2024-0214/pub/panteater/spring-2022 /pub/panteater   # see 4

The above commands mean:

1. The ``cd``  command puts you at the top level of a backup directory for your files.
2. The ``find`` command finds all backups by date where the desired directory exists.
   Here, two snapshots are found by date: :tt:`2024-0214` and :tt:`2024-0213`.
3. Run ``ls`` command for the specific snapshot to see if it has needed files.
4. If needed files exists in the backup, user can use ``cp`` command to copy the
   files back to the pub directory.  It is recommended to use ``-p`` and ``-r``
   options. Option ``-p`` makes sure that copy command preserves the time stamp
   and the ownership of a file.  Option ``-r`` means "copy recursively", this is
   needed when copying a directory and its contents.

One can restore in a similar way files and directories deleted from $HOME.
