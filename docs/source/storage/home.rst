.. _home:

HOME
====

Overview
--------

| The :tt:`$HOME` is a filesystem that is associated with your login account.
| Each user :tt:`$HOME` is in **/data/homezvolX/ucinetid**

.. _home files:

Storing Files
-------------

**What to Store**
  * STORE only important files here that change relatively infrequently

:red:`What NOT to Store`
  * DO NOT store large jobs output and error files
  * DO NOT store and then delete large data files. Such data is considered *transient*
    and should be stored on DFS filesystems.
  * DO NOT store any large input data files that are used for computational jobs.
    Use DFS file systems for this data.

:red:`NO Symbolic links`
  Many users have additional space on one or more CRSP or DFS filesystems.
  As a shortcut some created soft inks from their $HOME to one or more of these
  filesystems. The links  might look similar to

  .. code-block:: console

     [user@login-x:~]$ pwd
     /data/homezvol0/panteater
     [user@login-x:~]$ ls -l
     lrwxrwxrwx 1 panteater panteater 27 Jun 12 12:18 shared_lab -> /dfsX/pilab/shared_lab
     lrwxrwxrwx 1 panteater panteater 25 Jun 12 12:18 crsplalab -> /share/crsp/lab/pilab

  **This is a DANGEROUS practice as it often leads to unnecessary increase in
  loads on both NFS filesystem where your $HOME is and on the linked CRSP or DFS filesystem**.

  The  reason is a client (any command or process you run in your $HOME or
  that needs anything from your $HOME) has to resolve this symbolic link and verify
  mount **every single time**. This involves multiple operations and system
  calls  between NFS filesystem where your $HOME is and a parallel filesystem
  (CRSP or DFS). When executed many times by many users this creates a performance issue for everyone.

  .. attention:: Remove all symbolic links from your $HOME or anywhere under its subdirectories
                 and use aliases or enviornment variables in your .bashrc to
                 create shortcuts to desired filesystems. See :ref:`symbolic links` for more info.

.. _home quotas:

Quotas
------

Your :tt:`$HOME` together with ZFS snapshots  has a fixed quota:

.. table::
   :class: noscroll-table

   +---------+-------------------+--------------+----------------------------------------------------------------------+
   | Quota   | What for          | Access       | How to use                                                           |
   +=========+===================+==============+======================================================================+
   | 50GB    | :tt:`$HOME`       | read + write | Keep it clean and organized.                                         |
   +---------+-------------------+--------------+----------------------------------------------------------------------+
   | 50GB    | ZFS snapshots     | read only    | ZFS snapshots are copies of added/deleted/rewritten data. This gives |
   |         |                   |              | you some data protection/backup capability.                          |
   +---------+-------------------+--------------+----------------------------------------------------------------------+

.. important:: The total 100GB quota works as follows. If your snapshots consume X more space  than 50GB,
               you $HOME quota is automatically reduced by that X amount.

.. _zfs snapshots:

ZFS Snapshots
^^^^^^^^^^^^^

**Snapshots are "point-in-time" copies of data**
  Your home area is snapshot daily at a random time.
  Snapshots are kept for a period of time and then automatically deleted. Under normal use, the 100GB total limit for
  :tt:`$HOME+Snapshots` is rarely reached. A file/directory is permanently deleted when the last snapshot that holds
  that file is removed.

**Snapshots do not protect you from all possible data loss**
  For example,  if you create a file and then delete it a few hours later, that file is likely irretrievable.
  Lost data can only be recovered if it existed at the time a snapshot was taken and the snapshot is still available.

**ZFS snapshots  capability is not the same as a selective backup**
  Selective backup was created for automatically saving important files that are
  located in various file paths, including DFS filesystems. See :ref:`selective backup`.

**Every time a snapshot is taken, a virtual copy of all files at that time reside in the snapshot**
  When you delete a file, it is still in the snapshot.  If you constantly create and delete files, many of the deletes
  will remain in snapshots and consume more space.

  .. important:: This is why you should never put transient files in :tt:`$HOME`.

Snapshots are kept in :tt:`$HOME/.zfs/snapshots/`. All files and
directories that you have in your  :tt:`$HOME` are included in snapshots.
You cannot exclude any file or directories from a snapshot.

**Snapshot schedule:**
  | daily, keep last 8
  | weekly, keep last 6

  Per this schedule, you have about 6 weeks before a file is permanently deleted.
  Any changes or file deletions that occurred more than 6 weeks ago are gone forever.

.. _home check quotas:

How to check
^^^^^^^^^^^^

Changes to the contents of your :tt:`$HOME` are recorded daily and result in snapshots.
How frequently and how much data you **add/delete/overwrite** affects how much data
your can store in :tt:`$HOME`.

.. attention:: If you are changing the contents very often the snapshots will go
               over the quota very quickly.

**To see your $HOME quota usage do:**
  .. code-block:: console

     $ df -h ~
     Filesystem                        Size  Used Avail Use% Mounted on
     10.240.58.6:/homezvol0/panteater   50G  3.5G   47G   7% /data/homezvol0/panteater


  The :tt:`~` is a short notation for your :tt:`$HOME`.
  The output above shows that user :tt:`panteater` used 3.5Gb of its 50Gb allocation.

  .. note:: Snapshots do not show in the quota output.

**To see the usage by files and directories in $HOME:**

  .. code-block:: console

     $ cd
     $ ls
     bin                examples     local        perl5
     biojhub3_dir       info         mat.yaml     R
     classify-image.py  keras-nn.py  modulefiles  sbank-out
     $ du -s -h *
     7.0M	bin
     166M	biojhub3_dir
     8.5K	classify-image.py
     647K	examples
     91K	info
     4.5K	keras-nn.py
     126M	local
     60K	modulefiles
     512	perl5
     1.2G	R

  The above commands are:

  1.  ``cd`` -  change to your :tt:`$HOME` directory
  2.  ``ls`` -  list contents of :tt:`*$HOME`
  3.  ``du`` -  find disk usage for all files and directories in :tt:`$HOME`.

      The output  shows disk usage in kilobytes (K), megabytes (M) or gigabytes (G).
      For directories, all their contents are included.
      For example, a directory :tt:`R` and everything in it use total 1.2Gb of disk space.

.. _home over quota:

Over quotas
^^^^^^^^^^^

Every time you change files in you $HOME you are adding to your quota.
When snapshots are taken they record **addition and removal of files**.

.. important:: Never put transient files in :tt:`$HOME*`

Once you fill your quota you will not be able to write in your :tt:`$HOME`
until some of the space is freed.  You applications and jobs  will exhibit
various errors and will fail.

Most of the errors are (but not limited to):
  | - :red:`Cannot write to ‘file name’`
  | - :red:`Disk quota exceeded`.

The only way to free space is to remove
some snapshots and the users CAN NOT do this themselves.
You will have to submit a ticket to hpc-support@uci.edu

After your snapshots are removed you will be required to free enough
space in your :tt:`$HOME` in order to continue to work.

.. _home files recovery:

Deleted Files Recovery
^^^^^^^^^^^^^^^^^^^^^^

You can use snapshots  to restore files and directories provided that
existing snapshots still hold the desired data. There is no way to restore
files changed more than 6 weeks ago. Below is an example how to restore
accidentally deleted file. A similar technique can be used for multiple files
and directories.

**File is accidentally deleted**

  .. code-block:: console

     $ ls -l out
     -rw-rw-r-- 1 panteater panteater 4004 Sep 17 15:13 out
     $ rm -rf out
     $ ls -l out
     ls: cannot access out: No such file or directory

**Check the existing snapshots**

  .. code-block:: console

     $ ls .zfs/snapshot/
     zfs-auto-snap_daily-2020-09-16-1017
     zfs-auto-snap_daily-2020-09-17-1045
     zfs-auto-snap_daily-2020-09-18-1048

  The output indicates there are 3 snapshots done at different times.
  Snapshots names include a time stamp: year, month, day, hours and minutes.

  The deleted file had a time stamp :tt:`Sep 17 15:13`
  which means the file was created or modified on that time.

  The first two snapshots timestamps :tt:`2020-09-16-1017` and
  :tt:`2020-09-17-1045` are earlier that the deleted file modification time
  so they will not have deleted file in them or will have an earlier version.

  Need to search the snapshots that have a time stamp that is later than the
  time stamp of the deleted file:

  .. code-block:: console

     $ ls .zfs/snapshot/zfs-auto-snap_daily-2020-09-18-1048/out
     .zfs/snapshot/zfs-auto-snap_daily-2020-09-18-1048/out

**Restore file from a snapshot**
  Copy found file:

  .. code-block:: console

     $ cp zfs/snapshot/zfs-auto-snap_daily-2020-09-18-1048/out .
     $ ls -l out
     -rw-rw-r-- 1 panteater panteater 4004 Sep 18 10:53 out
