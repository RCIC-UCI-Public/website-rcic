.. _home:

HOME
====

.. contents::
   :Local:

Overview
--------

| The :tt:`$HOME` is a ZFS-filesystem that is associated with your login account.
| Each user :tt:`$HOME` is in **/data/homezvolX/UCInetID** (where *X* is
  is a number that signifies a particular storage pool used for the account).

.. _home files:

Storing Files
-------------

**What to Store**
  * configuration files for logging in or for applications, many by default are in :tt:`$HOME`
  * Store only important files here that change relatively infrequently

:red:`What NOT to Store`
  * DO NOT store and then delete large data files. Such data is considered *transient*
    and should be stored on DFS filesystems.
  * DO NOT store any large input data files that are used for computational jobs,
    or any large output/error job files.  Use your personal :tt:`/pub/UCInetID` or your group DFS file systems.

:red:`NO Symbolic links`
  Many users have additional space on one or more CRSP or DFS filesystems.
  As a shortcut some created soft inks from their :tt:`$HOME` to one or more of these
  filesystems. The links  might look similar to this example:

  .. code-block:: console

     [user@login-x:~]$ pwd
     /data/homezvol0/panteater
     [user@login-x:~]$ ls -l
     lrwxrwxrwx 1 panteater panteater 27 Jun 12 12:18 shared_lab -> /dfsX/pilab/shared_lab
     lrwxrwxrwx 1 panteater panteater 25 Jun 12 12:18 crsplalab -> /share/crsp/lab/pilab

  How to fix
    * Remove symbolic links from :tt:`$HOME` or its
      subdirectories (here :red:`shared_lab` and :red:`crsplab`).
    * Use aliases or environment variables in your :tt:`.bashrc` to
      create shortcuts to desired filesystems. See :ref:`symbolic links` for more info.

  .. attention:: 
     **Symbolic link from ZFS filesystem to CRSP/DFS filesystem
     is a DANGEROUS practice** as it often leads to unnecessary increase in
     loads on both NFS server where your ZFS-based :tt:`$HOME` is and on the linked CRSP or DFS filesystem:

     * Any command or process you run in your :tt:`$HOME` or that needs anything from your :tt:`$HOME`
       has to **resolve this symbolic link and verify mount every single time**.
     * **This involves multiple operations and system calls** between filesystem where your :tt:`$HOME`
       is and a parallel filesystem (CRSP or DFS) where your link points.
     * **Executed many times by many users creates a performance issue** for everyone.


.. _home quotas:

Quotas
------

Your :tt:`$HOME` together with ZFS snapshots  has a fixed quota:

.. table::
   :class: noscroll-table
   :widths: 10,14,16,60
   :align: center


   +---------+---------------+--------------+---------------------------------------------------------------+
   | Quota   | What for      | Access       | How to use                                                    |
   +=========+===============+==============+===============================================================+
   | 50GB    | :tt:`$HOME`   | read + write | Keep it clean and organized.                                  |
   +---------+---------------+--------------+---------------------------------------------------------------+
   | 50GB    | ZFS snapshots | read only    | ZFS snapshots are copies of added, deleted or rewritten data. |
   |         |               |              | This gives you some data protection/backup capability.        |
   +---------+---------------+--------------+---------------------------------------------------------------+

.. important:: The total 100GB quota works as follows. If your snapshots consume X more space  than 50GB,
               you $HOME quota is automatically reduced by that X amount.

.. _zfs snapshots:

ZFS Snapshots
^^^^^^^^^^^^^

Snapshots are kept in :tt:`$HOME/.zfs/snapshots/` directory.

**Snapshot schedule:**
  :daily: keep last 14

  | Per this schedule, you have about 2 weeks before a file is permanently deleted.
  | Any changes or file deletions that occurred more than 2 weeks ago are gone forever.

**Snapshots are point-in-time copies of data**
  | All files and directories in your  :tt:`$HOME` are included in snapshots.
  | You cannot exclude any file or directories from a snapshot.
  | Your home area is snapshot daily at a random time.
  | Snapshots are kept for a period of time and then automatically deleted.
  | A file/directory is permanently deleted when the last snapshot that holds it is removed.
  | Under normal use, the 100GB total limit for :tt:`$HOME+Snapshots` is rarely reached.

**Snapshots do not protect you from all possible data loss**
  *Lost data can only be recovered if it existed at the time a snapshot was taken and the snapshot is still available*.
  If you create a file and delete it a few hours later, that file is likely irretrievable.

**ZFS snapshots  capability is not the same as a selective backup**
  Selective backup was created for automatically saving important files that are
  located in various file paths, including DFS filesystems. See :ref:`selective backup`.

**Every time a snapshot is taken, a virtual copy of all files at that time reside in the snapshot**
  When you delete a file, it is still in the snapshot. If you constantly create and delete files,
  many of the creates/deletes will remain in snapshots and consume more space.

  .. important:: This is why you should never put transient or frequently changed files in :tt:`$HOME`.

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
     10.240.61.77:/homezvol0/panteater  50G   14G   37G  27% /data/homezvol0/panteater

  The :tt:`~` is a short notation for your :tt:`$HOME`.
  The output above shows that user :tt:`panteater` used 14Gb of its 50Gb allocation.

  .. note:: Snapshots do not show in the quota output.

**To see the usage by files and directories in $HOME:**

  .. code-block:: console

     $ cd             # change to your $HOME directory
     $ ls             # list contents of $HOME
     bin              examples  maintenance  perl5   sw            tst.pl
     copy-archive.sh  info      matlab       R       sys           writing
     database.py      local     modulefiles  README  testmodfiles

     $ du -s -h *    # find disk usage for files and directories in $HOME
     98K	bin
     2.0K	copy-archive.sh
     2.0K	database.py
     1.4M	examples
     5.1M	info
     64M	local
     140K	maintenance
     1.5K	matlab
     59K	modulefiles
     88K	perl5
     918M	R
     4.0K	README
     17K	sw
     31M	sys
     2.0K	testmodfiles
     1.0K	tst.pl
     32M	writing

  The output  shows disk usage in kilobytes (K), megabytes (M) or gigabytes (G).
  For directories, all their contents are included.
  For example, a directory :tt:`R` and everything under it use total 918Mb of disk space.

  The above list does not sum to 14Gb, where did the rest of disk space go?
  The ``du -s -h *`` command does not take into an account **hidden files and directories**
  which are names that start with a dot character.

  Many applications configuration/setup files as well as shell initialization files
  by default are in $HOME. They are by design *hidden*,

  **To see the usage by hidden files and directories**:

  .. code-block:: console

     $ du -s -h .[a-z,A-Z]*  # type command as shown here
     54M	.aspera
     20K	.bash_history
     2.0K	.bashrc
     7.1M	.beast
     37M	.cache           # used by many applications to store cached data
     5.0G	.conda           # user installed conda environments and packages 
     37M	.config          # used by many applications for configuration files
     625M	.local           # user installed Python packaged  (by pip)
     2.0K	.MathWorks
     5.7M	.matlab
     1.5K	.Rhistory
     1.5K	.rnd
     42K	.rstudio
     6.5G	.singularity     # used as a cache by singularity containers
     512	.slurm
     22K	.ssh
     1.5K	.vim
     2.5K	.vscode-remote
     167M	.vscode-server   # used by VS Code 

     ... <deleted lines> ...

  The total of all hidden files and directories is close to 13Gb, most of the storage for this user.

.. _home over quota:

Over quotas
^^^^^^^^^^^

.. important:: 
   | Every time you change files in your :tt:`$HOME` you are adding to your quota.
   | When snapshots are taken they record **all files additions and removal**.
   | Never put transient files in :tt:`$HOME`!

Once you fill your quota you will not be able to write in your :tt:`$HOME`
until some of the space is freed.  You applications and jobs  will exhibit
various errors and will fail.

Most of the errors are (but not limited to):

  | :red:`Cannot write to ...`
  | :red:`Disk quota exceeded for ...`

The only way to free space is to remove
some snapshots and the users CAN NOT do this themselves.
You will have to submit a ticket to hpc-support@uci.edu

After your snapshots are removed you will be required to free enough
space in your :tt:`$HOME` in order to continue to work.

.. _home files recovery:

Deleted Files Recovery
----------------------

You can use snapshots  to restore files and directories provided that
existing snapshots still hold the desired data. There is no way to restore
files changed more than 2 weeks ago. Below is an example how to restore
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

  The output indicates there are 3 daily snapshots done at different times.
  Snapshots names include a time stamp: year, month, day, hours and minutes.

  The deleted file had a time stamp :tt:`Sep 17 15:13`
  which means the file was created or modified on that time.

  The first two snapshots time stamps :tt:`2020-09-16-1017` and
  :tt:`2020-09-17-1045` are earlier that the deleted file time stamp
  so they will not have deleted file or will have an earlier version of it.

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
