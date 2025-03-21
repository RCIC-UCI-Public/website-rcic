.. _dfs:

DFS
===

.. contents::
   :local:

Overview
--------

This is a network-based multi-Petabyte storage put in place
so that researchers across UCI have a reliable and resilient location
to store their research data and share it with defined groups.

Parallel file systems running `BeeGFS <https://www.beegfs.io/c/>`_ on top of `ZFS <https://zfsonlinux.org/>`_
provide scalable data storage on HPC3 in the :tt:`/dfsX`  and :tt:`/pub` file paths.

.. warning:: DFS filesystems  must not be used to store personally-identifiable information that would fall
   under guidelines  such as `FERPA <https://studentprivacy.ed.gov/ferpa>`_
   (Student data) and `HIPAA <https://www.hhs.gov/hipaa/index.html>`_ (health-care data).

   If you are unsure that DFS is suitable for your data, please refer to general guidance for
   `data security <https://research.uci.edu/human-research-protections/assessing-risks-and-benefits/privacy-and-confidentiality/data-security/>`_
   provided by the `UCI Office of Research <https://research.uci.edu/>`_

:Performance: *  Of each file system is quite good (5-6 GByte/s) **when used properly**,
                 :red:`but it is not too difficult for a single user to
                 exceed the inherent capabilities and completely wreck performance for everyone`
              *  Multiple DFS systems provide an aggregate throughput > 30 GByte/s.

**Take-home concepts about DFS parallel files systems are:**
  * They perform well when reading/writing large files in good-sized (> 128KB) chunks.
  * They perform very poorly when reading/writing many small files.
  * All DFS systems are *single copy, high-performance storage* intended for scratch data.
    No special backup is available. Deleted data are gone forever.
  * Accessible only from HPC3 as a regular filesystem for storing data on the cluster.
    There are a few separate storage pools which are mounted on the cluster as :tt:`/dfsX`.
  * For recharge allocations please see :ref:`buy dfs`.

.. It is beyond the scope of this document to describe parallel file systems in detail, but one
   should `start learning more <https://en.wikipedia.org/wiki/BeeGFS>`_ to make better use of the file systems.

.. _dfs allocations:

Allocations
-----------

There is no separate account for DFS filesystems.
:ref:`dfs quotas` are enforced using groups.

**No cost allocation -  Private area**
  All users have access to the Private Area. Each user gets a fixed default allocation:

  * 1TB quota per account in :tt:`/pub/UCInetID`.
  * 1TB backup quota for a selective backup.

**Recharge allocation - Group shared area**
  UCI Faculty members (PIs) can purchase low-cost recharge allocation(s) to fulfill their needs:

  * These group areas are quota allocations in :tt:`/dfsX/group-lab-path` based on PI's purchase.
  * The PI is the storage owner:

    * can specify additional users who will have read and write access to the area.
    * can :ref:`Purchase Recharge Allocations <recharge allocations>`.

  * Users can :ref:`request to be added to the PI's group shared area <add lab dfs>`.

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

  :tt:`/pub/UCInetID`
    * is a unique *Private area*, never shared with other users
    * the organization of files and directories is up to the user
    * :red:`do NOT change this directory permissions`

  :tt:`/dfsX/<group-lab-path>`
    * is a specific *Group shared area*, users may have access to one or more group areas
    * the organization of files and directories is up to the group members
    * all group members have read and write access
    * :red:`do NOT change directories permissions or sticky bit settings`, see a warning below

**File permissions**
  | File permissions are used in determining quotas.
  | The permissions involve setting logical UNIX groups.

  .. _sticky warning:

  .. warning:: * When we create **Private areas** and  **Group shared areas** on DFS
                 we set correct permissions on the top level directories.
               * Each **Group shared area** is initially configured with the **group sticky bit set**
                 so that only allowed users can access this area.
               * We advise users to NOT change permissions on the directories and files when writing in the group area.
                 :red:`Incorrect permissions lead to quota exceeded errors`.

  Please see :ref:`unix primer`  to learn about UNIX groups
  and understand UNIX :ref:`file permissions`.

.. _dfs quotas:

Quotas
------

| All DFS-based file systems have quotas for all private and group shared areas.
| Quotas are enforced using UNIX groups.

**When writing in Private area**:
  * Every user has a *default personal group* which is the same as their UCInetID (login).
  * :tt:`1TB personal group quota` on **/pub/UCInetID**.
  * :tt:`1Tb selective backup quota` (a default for each user).

**When writing in Group shared area**:
  * All members of the group contribute to the quota. It's the sum total usage that counts.
  * :red:`There are no individual user quotas`, only the group quota is used.
  * :red:`If you create file with the incorrect group, you will likely see over quota errors`.
  * :red:`When quotas are exceeded, all users in the group will no longer be able to write` in the affected
    filesystem  and will need to remove some files and directories to free space.

.. important::  Users can't change quotas and can't request quotas.
                A PI can submit a ticket asking to update the quota based on purchasing. Please see :ref:`buy dfs`.

.. _dfs check quotas:

How to check
^^^^^^^^^^^^

For all DFS file systems  including selective backup one can use ``dfsquotas``
command to check user/group quotas on a particular DFS pool.

**To see the quotas for user** `panteater` **on private allocation in** :tt:`/dfs6`:

  .. code-block:: console

     $ dfsquotas panteater dfs6
     ==== Group quotas on dfs6 for user panteater
     ----------------------------------------------------------------------------
                    Group      ||          Size            ||    Chunk Files     
                 name | id     ||       used | allocated   ||    used | allocated
     ----------------------------------------------------------------------------
        panteater_lab | 012345 ||  26.25 GiB | 1024.00 GiB || 1310459 | unlimited
          alpha_users | 158537 ||     0 Byte | 1024.00 Gib ||       0 | unlimited
            panteater | 000865 || 755.59 GiB | 1024.00 GiB ||  258856 | unlimited

  The above shows that a user `panteater` can write in its private
  area :tt:`/pub/panteater` using the groups listed in the output:

     * `panteater_lab`: a supplementary group; user wrote 26.25Gb of data.
     * `alpha_users`: a supplementary group; user wrote no files, but can if needed.
     * `panteater`: a default group; user wrote ~756Gb of data.

  .. note:: Groups listed in the output are logical UNIX groups associated with a user account.
            The primary use of such groups is to assign *group ownership* of files and directories.
            The 1Tb quota allocation is a total space that can be used by all listed
            user UNIX groups *combined*, not by each group individually.  :math:`1Tb = 1024Gb`.

**To see the quotas for user** `panteater` **in lab shared allocation in** :tt:`/dfs9`:
  .. code-block:: console

     $ dfsquotas panteater dfs9
     ==== Group quotas on dfs9 for user panteater
     ----------------------------------------------------------------------------
                    Group      ||          Size            ||    Chunk Files     
                 name | id     ||      used  | allocated   ||    used | allocated
     -----------------------------------------------------------------------------
        panteater_lab | 012345 ||   38.36 TiB|   40.00 TiB || 1310459 | unlimited
          alpha_users | 158537 ||      0 byte|    1   byte ||       0 |         1
            panteater | 000865 ||      0 byte|    1   byte ||       0 |         1

  The above shows that user `panteater` can write in its group allocation on :tt:`dfs9`

     * only if using UNIX group `panteater_lab` for which there is 40Tb
       allocation.  Currently, the used space by all users allowed to write in
       this area is 38.36Tb.
     * there is 0 quota (shown as 1 byte) for a default personal group
       `panteater` or a supplemental group `alpha_users`. If a user tries
       to write  using these UNIX groups it will result in permissions and over the quota errors.

..  next two blocks are commented out

..  **To see the quotas for selective backup:**

     .. code-block:: console

        $ dfsquotas panteater sbak

**To see the quotas on all DFS filesystemss**:

  .. code-block:: console

     $ dfsquotas panteater all

  The output will show information for all available DFS filesystems.
  When a user has no quota on a particular filesystem it will show as *No quotas to report*.

  For more info on using this command, try:

  .. code-block:: console

     $ dfsquotas -h

.. _dfs over quota:

Over quotas
^^^^^^^^^^^

When quota is filled, the users will not be able to write any files
or directories and submitted jobs will fail with :red:`quota exceeded errors`.

Quota is enforced by the file system based upon the **UNIX group membership**
of a particular file:

  For example, a listing of a current directory shows

  .. code-block:: console

     $ ls -l
     total 55524423
     drwxrwsr-x  7 panteater bio                 7 Aug  5  2019 biofiles
     -rw-r--r--  1 panteater panteater  4294967296 May 31  2019 performance.tst
     drwxrwsr-x  3 panteater panteater           2 Oct  8 17:11 myfiles

  The user `panteater` is storing files under two different groups:

    - `bio`: the files in the subdirectory :tt:`biofiles` with its content are charged to the group `bio` quota.
    - `panteater`: file **performance.tst** and subdirectory **myfiles** with its content are charged to the group `panteater` quota

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
     | is set     |                                       | written with the group permissions :red:`rws`.                  |
     |            |                                       | The sticky bit :red:`s` is set.                                 |
     +------------+---------------------------------------+-----------------------------------------------------------------+
     |            |:gray:`drwx`:bluelight:`rwx`:gray:`r-x`| In the origin directory, created files and directories are      |
     |            |                                       | written with the active UNIX group permissions :bluelight:`rwx` |
     | is NOT set |                                       | which defaults to the user login.                               |
     +------------+---------------------------------------+-----------------------------------------------------------------+

The UNIX command ``newgrp`` can be used to change the active UNIX group:

  For example, the user `panteater` by default has a group `panteater`.
  The following sequence of simple commands shows the ownership of the files
  created under different groups and changed when using the ``newgrp`` command.

  .. code-block:: console

     $ id panteater                  # list user and group IDs
     uid=1234567(panteater) gid=1234567(panteater) groups=1234567(panteater),158571(bio)
     $ touch aaa                     # create a new empty file
     $ ls -l aaa                     # check file permisisons
     -rw-rw-r-- 1 panteater panteater 0 Nov  3 14:57 aaa

     $ newgrp bio                    # change to a new group
     $ touch bbb                     # create a new empty file
     $ ls -l bbb                     # check file permissions
     -rw-rw-r-- 1 panteater bio 0 Nov  3 14:57 bbb

  Please type ``man newgrp`` to learn about this command.

**Reasons for Over Quota**
  1. Under normal operation, when the sticky bit is set on a directory, the correct quota enforcement
     occurs automatically because files and subdirectories are written with
     correct group, no ``newgrp`` command is needed.  When all space is used over quota is issued.
  2. Very common quota problems on DFS result from:

     * inadvertently removing the sticky bit on a directory and then writing with the default personal group.
     * changing the group ownership of a file or directory and then trying to write to it with the default personal group.

     In these cases writing files and running jobs will fail with quota exceed errors.
  3. Transferring data to HPC3 with software that explicitly sets
     permissions is the most common way a sticky bit becomes overwritten.

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


  The ``ls -l`` command is used to show permissions before and after the change.

.. _selective backup:

Selective Backup
----------------

*We cannot backup everything on the cluster*. Selective Backup allows the
users to choose what is important and have it automatically saved. The physical
location of the backup server is different from the cluster location for extra protection.

.. Important::
   * You will want to backup only critical data such as scripts, programs, etc.
   * DO NOT backup data you can get from other sources, especially large data-sets.
   * If you go past your backup quota then backups stops
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

.. note:: | For a majority of users, defaults are sufficient.
          | There is nothing for you to do if you like the defaults.

Users manage their Selective Backup via two *control files* located in their
:tt:`$HOME` directory:

1. :tt:`.hpc-selective-backup`
   file  lists (1) backup options and the (2) files/directories names to be saved in order of
   priority from the most to the least important. All backup options are initially commented out.

   The files are backed up in the order as they are listed. That way, if a user runs out of
   selective disk quota before all listed files have been backed up, at least their most
   prized data are saved.  By default, this file contains :tt:`$HOME` and
   :tt:`/pub` areas of your account:

   .. code-block:: bash

      /data/homezvolX/UCInetID
      /pub/UCInetID

   The following table lists all available backup options:

   .. table::
      :class: noscroll-table

      +--------------------------+------------------------------------------------------------------+
      |  Selective Backup Option | What it does                                                     |
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

2. :tt:`.hpc-selective-backup-exclude`
   This file lists file/directories names you want to exclude from backup.
   By default, this file excludes ZFS  snapshots from :tt:`$HOME`:

   .. code-block:: bash

      $HOME/.zfs

   For more information on exclude please see the *ANCHORING INCLUDE/EXCLUDE PATTERNS*
   section of the ``man rsync`` output.


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
   | /sbak/zvolX/backups/UCInetID/data/homezvolX/UCInetID | user $HOME                    |
   +------------------------------------------------------+-------------------------------+
   | /sbak/zvolX/backups/UCInetID/pub/UCInetID            | /pub/$USER/                   |
   +------------------------------------------------------+-------------------------------+
   | /sbak/zvolX/backups/UCInetID/DELETED-FILES           | deleted files by date         |
   |                                                      | (counts towards backup quota) |
   +------------------------------------------------------+-------------------------------+
   | /sbak/zvolX/logs/$DATE/UCInetID                      | backup logs by date,          |
   |                                                      | available for the past Y days |
   +------------------------------------------------------+-------------------------------+

.. note:: | The :tt:`X` in :tt:`/sbak/zvolX`  maps to the volume number shown in your :tt:`$HOME` variable. In other words:
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

   $ cd /sbak/zvol0/backups/panteater/DELETED-FILES                  # 1
   $ find . -type d -name spring-2022                                # 2
   ./2024-0214/pub/panteater/spring-2022
   ./2024-0213/pub/panteater/spring-2022

   $ ls ./2024-0214/pub/panteater/spring-2022/                       # 3
   schedule1    schedule1.sub   slurm.template

   $ cp -p -r ./2024-0214/pub/panteater/spring-2022 /pub/panteater   # 4

The above commands mean:

  1. The ``cd``  puts you at the top level of a backup directory for your files.
  2. The ``find`` finds all backups by date where the desired directory exists.
     Here, two snapshots are found by date: :tt:`2024-0214` and :tt:`2024-0213`.
  3. Run ``ls`` for the specific snapshot to see if it has needed files.
  4. | If needed files exists in the backup, user can use ``cp`` to copy the
       files back to the pub directory.  It is recommended to use ``-p`` and ``-r`` options:
     |    ``-p`` copy preserves the time stamp and the ownership of a file.
     |    ``-r`` *copy recursively*, this is needed when copying a directory and its contents.

One can restore in a similar way files and directories deleted from $HOME.
