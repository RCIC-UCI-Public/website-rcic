.. _crsp:

CRSP
====

Overview
--------

CRSP is a network-based multi-Petabyte storage cluster for the UCI campus research community.
It is a reliable and resilient location created for researchers across UCI 
to store and share their research data.

CRSP is available across the network, it supports multiple modes of
storing and retrieving data including web browsers, "folders" on laptops or desktops,
and just another file path on UCI's High-performance computing clusters.

While there are many possible use cases, a driving one is:
   :bluelight:`A faculty researcher and the data needed to support the research lab, graduate students
   and postdocs.  In this model, a lab "area" is created on CRSP and is logically owned by the
   researcher. The lab area owner can specify additional users who have read/write capability
   on the area and how much space each could consume`

.. warning:: CRSP filesystems  must not be used to store personally-identifiable information that would fall
             under guidelines  such as `FERPA <https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html>`_
             (e.g. Student data) and `HIPAA <https://www.hhs.gov/hipaa/index.html>`_ (health-care data).

             If you are unsure if DFS is suitable for your data, please refer to general guidance for
             `data security <https://research.uci.edu/compliance/human-research-protections/researchers/data-security.html>`_
             provided by the `UCI Office of Research <https://www.research.uci.edu/>`_

.. _crsp technologies:

CRSP technologies
-----------------

**CRSP is a combination of several technologies**
  * It is built with industry leading storage technology to ensure data high availability and resiliency.
  * It is multi-site and is comprised of commodity server components from Dell for cost-effective scaling
    and performance.
  * The underlying parallel file system is :term:`GPFS`
  * Additional support and integration software from `Arcastream <https://www.arcastream.com/>`_.

**Features include**
  * An active-active storage system setup between two hosting locations for high availability and redundancy,
    with fully fault tolerant high speed networking.
  * End-to-End 24x7 software and hardware support.
  * A fully encrypted file system, featuring
    `encryption at REST <https://www.ibm.com/docs/en/search/encryption?scope=STXKQY>`_
    ensuring user data security.
  * Several user access methods are in place, with enterprise level support.
    All access mechanisms are fully load-balanced between data centers.
  * A file system design that has massive scaling capabilities without compromising performance.
  * A front-end access layer design that is capable of scaling horizontally as demand grows.
  * Multiple user access methods, assuring a superior level of user experience.

.. TODO  rm image below or make a new one
.. .. centered:: A simplified illustration of CRSP architectural diagram

.. .. image:: images/crsp-arch.png
   :align: center
   :alt: crsp  architecture

.. _crsp allocations:

Allocations
-----------

CRSP is funded through central campus to guarantee a fixed amount of no-cost storage to any faculty member
or staff researcher who requests space. These campus funds pay for the people, the baseline infrastructure,
and vendor maintenance required to provide the robust infrastructure.

CRSP allocations are provided for UCI faculty members as follows:

**No cost baseline allocation**
  - 1TB quota per researcher

**Recharge allocation - Lab area**
  - Researchers who require more capacity than the baseline allocation, can purchase additional capacity.
    Please see  :ref:`recharge storage rates` and :ref:`buy crsp`

In general, users do not get a default CRSP allocation.
The allocation owners can grant access to their spaces to students, postdocs, and other faculty members.

The allocation is associated with an account.

.. _getting crsp account:

Getting CRSP Account
--------------------

All requests described below must be sent to hpc-support@uci.edu

* **I'm a researcher on campus and I want to have an access**
  If you are a ladder-rank faculty or have an exception granted to act as PI on federal grants
  by UCI Office of research, your account should be pre-created. If you still do not have
  access, please send us a request.

* **I'm a researcher and I want to access my colleagues lab**
  Your colleague must send a request and ask for access for you to their lab.

* **I'm a researcher and I want colleagues outside of UCI to have access to my lab**
  You must first sponsor a UCINetID (see :ref:`access`) then send a request to grant access.

* **I'm a researcher and I want to add students/postdocs to my lab**
  You should send a request and include:

  - your existing CRSP lab name
  - UCINetIDs and names of the people that you want to add
  - indicate any of these people should have individual limits
	and what the limits are. The default behavior is no individual limit.

* **I'm a student/postdoc**
  Your PI should send a request and include:

  - your UCINetID
  - indicate if your space should have an individual limit.

  PI may combine multiple requests in a single email.


.. _crsp areas:

Private and Shared Areas
------------------------

Storage space on CRSP has the concepts of:

:tt:`Space Owners`:
  * Are entitled to a baseline allocation and are all ladder faculty, PIs and
    UCI employee serving as PI/Co-PI on an extramural grant.
  * Can store files in their LAB and can partition LAB into shared and no-shared area.
  * Can grant access to their LAB storage space to Grantees: students, postdocs, and other faculty members.
  * Can purchase more space.

:tt:`Grantees`:
  * Are those who are granted access by Space owners (lab students, postdocs, etc).
  * Can access the LAB space to which they have been granted access by Space Owners
    and store files there.

.. note:: A :tt:`directory` meaning on Unix  is equivalent to a :tt:`folder` on macOS, Windows.
          In what follows, we will use the term :tt:`file` to mean
          :tt:`file`, :tt:`folder`, or :tt:`directory`.

Storage space on CRSP is divided into :tt:`Private` and :tt:`Shared` areas.

.. _crsp private:

Private Area - HOME
^^^^^^^^^^^^^^^^^^^

This allocation space, called :tt:`HOME`, is for $HOME directories:

* Not used for sharing with others.
* Is required for Linux accounts and is ONLY used for an account related files.
* :red:`DO NOT use HOME for storing any data`.
* File :tt:`quotas.txt` is created and updated in your $HOME area automatically and
  provides information about your quota status for HOME and LAB areas.

.. _crsp chared:

Shared Area - LAB
^^^^^^^^^^^^^^^^^

This allocation space, called :tt:`LAB`, is a *shared space area* per Space Owner.

Space owner grants explicit access for this area to Grantees and decides how to allocate the space
among its group members.

The LAB areas provide the most flexibility for access control and sharing:

* The space owner by default has read access to every file and directory in the LAB
* Only the space owner has the ability to create files or new directories in the top-level of the LAB area.
* Grantees have a personal directory  named with their UCINetID.
  Files stored here are viewed only by the space owner and the grantee.
* A directory called :tt:`share` is available to all members of the lab
  who can read/write all files stored under it.
* Quota is for the  whole LAB area allocation and is a sum of what is stored
  in :tt:`share`  and in all personal directories.

CRSP has many (and sometimes competing) goals for access, sharing, security,
manageability, and simplicity for researchers.  One of the technical complexities
of CRSP is that the underlying file system and access enforcement mechanisms are
defined in Linux, but most users access is from Mac and Windows environments.

On Linux (Unix) an independent access controls to all files given to three different entities:

* The *owner* of the file. This is the UCINetID that originally created the file
* The *group* of the file. A group who might have access to this file
* The *world* (or others). Everyone else on CRSP

.. important:: In CRSP LAB areas sharing is controlled by **group** permissions
               and by who is a member of the particular group. The *world* has *no privilege*
               to read or write files in any LAB area.

.. note:: Owners of files may make their files explicitly private by removing all read/write permissions from group

.. _default crsp lab:

Default Lab Setup
^^^^^^^^^^^^^^^^^

For each LAB area, the :tt:`PI` is the owner of the space.
There are two Unix groups predefined for all labs:

* :tt:`pi_lab`: Only the lab owner is in this group
* :tt:`pi_lab_share`: All members of the lab including the lab owner.

**Example Lab**

In the following, we will use the lab for a PI *ppapadop* as an example:

* *ppapadop* is in the group :tt:`ppapadop_lab` and is only member of this group.
*    *ppapadop* is in the group :tt:`ppapadop_lab_share`.
* *ckhacher*, *itoufiqu*, *tandriol*, *iychang* are in the group :tt:`ppapadop_lab_share`.
  They are lab members (grantees) that were given an access to the LAB area  by the PI.

  .. centered:: Example: LAB top-level folder (using MAC CRSP Desktop)

  .. image:: images/crsp-lab-share-highlight.png
     :align: center
     :alt: crsp lab share example

This shows that for the :tt:`ppapadop` Lab on CRSP:

1. Each user in the LAB has a folder named by UCNetID that is private to the
   user and to the PI. These are LAB members  who are in the group
   :tt:`ppapadop_lab_share`: *ppapadop*, *ckhacher*, *itoufiqu*, *tandriol*, *iychang*.
2. User *ppapadop* who is a PI can see all files.
3. User *itoufiqu* can only see files in the :tt:`itoufiqu` and :tt:`share` folders.
   Similarly, user *ckhacher* cn only see see files in the :tt:`ckhacher` and :tt:`share` folders.

.. _crsp access:

Accessing  CRSP
---------------

You must either be on the campus network or connected to the
`UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ to access CRSP.

You can access  your granted CRSP storage from Windows, MAC, and Linux systems
via a few methods. The client links in the table below provide installation
instructions:

.. table::
   :widths: 30 70
   :class: noscroll-table

   +------------------------------+-------------------------------------------------------------------------------------------+
   |  Client                      | Description                                                                               |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client desktop windows`| *CRSP Desktop* clients are for accessing CRSP from Windows and macOS laptops.             |
   | :ref:`client desktop mac`    | We provide licensed and branded version of a commercial software *Mountain Duck*.         |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client web browser`    | This access is used for *light weight* CRSP resource usage, supports file or direvtory    |
   |                              | uploads/downloads and provides in-browser edit capabilities for certain file types.       |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client sshfs`          | *SSHFS* can be used for accessing CRSP shares from a Linux laptop/desktop.                |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client from hpc3`      | *NFS mount* on HPC3 provides and access to the CRSP's LAB and HOME areas.                 |
   +------------------------------+-------------------------------------------------------------------------------------------+

.. attention::

   Although CRSP storage system could be accessed via other commercial or open source
   desktop clients such as FileZilla, WinSCP, CyberDuck, the  **CRSP Desktop** client is the currently
   supported SFTP based software. Other desktop clients support is provided only on a best effort basis.


Consult our :ref:`crsp troubleshoot` if you have trouble accessing your CRSP shares.

.. _crsp quotas:

Quotas
------

All CRSP-based file systems have quota enforcement.

- CRSP allocations are provided for UCI faculty members.
  In general, users do not get a default CRSP allocation.
  The allocation owners can grant access to their spaces to students, postdocs, and other faculty members.
 
- Users who are granted access have $HOME area which is used only by account related files.
  This area is NOT for storing anything else.

- User who are granted access to one or more  PI's lab areas (see :ref:`crsp areas`)
  may have additional quota limits set by their PIs for the group area.

- All CRSP quotas are enforced in two areas: total space used and number of
  files.

- When writing in group area users need to remember that all members of the
  group contribute to the quota. It's the sum total usage that counts.
  When quotas are exceeded, users can no longer write in the affected
  filesystem  and will need to remove some files and directories to free space.

- Users can't change quotas, but can submit a ticket asking to be added
  to the group quotas provided there is a confirmation from the PI about the change.

.. _crsp check quotas:

How to check
^^^^^^^^^^^^

There are two ways to check your quotas:

1. Using a web browser go to the
   `https://access.crsp.uci.edu/quota <https://access.crsp.uci.edu/quota[https://access.crsp.uci.edu/quota>`_
   You will be asked to authenticate yourself (DUO) and once successful you
   will see a simple text page indicating your quotas for HOME and LAB areas.

2. When you are logged on HPC3 you can simply view your CRSP quota.
   File :tt:`/share/crsp/home/USERNAME/quotas.txt` in your CRSP HOME area provides quotas info:

   .. code-block:: console

      [user@login-x:~]$ ls -ld /share/crsp/home/panteater
      drwx-----T 7 panteater panteater 2048 May 10 15:28 /share/crsp/home/panteater

      [user@login-x:~]$ cat  /share/crsp/home/panteater/quotas.txt
      Quota Report for panteater : 06/12/23 17:30
      == Storage Areas that you own  ==                                                   (1)
      == Your use in Paths to which you have access  ==
         /mmfs1/crsp/home                    0.001 GB/     0.020 GB      6/40       files (2)
              total bytes in use        :  115.735 GB/     0.000 GB
         /mmfs1/crsp/lab/ucinetid-pi        39.799 GB/  1024.000 GB   2900/100000   files (3)
              total bytes in use        :  374.092 GB/  1024.000 GB

   | The first ``ls`` command above gives an idea when the file was updated.
   | The second ``cat`` command shows that the user *panteater*:

   | (1) does not own any area (user is not a PI).
   | (2) has no usage in HOME area :tt:`/mmfs1/crsp/home`, this is a correct behavior.
   |     The 0.001 GB is used only by account related files. Currently the user
   |     used 6 out of 40 files (40 is a quota).
   | (3) is a member of ucinetid-pi LAB and used 39.799 GB of the allocated 1024 GB LAB area
   |     in :tt:`/mmfs1/crsp/lab/ucinetid-pi` and 2900 files (quota 100000). 
   |     The total usage of the LAB area by all lab members is 374.092 GB.

   Note the path naming on CRSP and HPC3:

   ==== ================================= ==================================
   Area Path on CRSP                      Path on HPC3
   ==== ================================= ==================================
   HOME :tt:`/mmfs1/crsp/home`            :tt:`/share/crsp/home`
   LAB  :tt:`/mmfs1/crsp/lab/ucinetid-pi` :tt:`/share/crsp/lab/ucinetid-pi`
   ==== ================================= ==================================

  .. note:: | If you are a PI of the lab you will to see the usage of your lab quota for all lab members.
            | If you are a member of the lab you will see only what you have used from the lab quota allocation.

.. _crsp over quota:

Over quotas
^^^^^^^^^^^

When quota is filled either in used space or in number of files, the users will not be able to write any files
or directories and submitted jobs will fail with :red:`quota exceeded errors`

For example, the following output in quotas check  show the quotas exceeded for the user in number
of files (a) in storage used (b):

.. parsed-literal::

      mmfs1/crsp/home                    0.014 GB/     0.020 GB     :red:`40/40`       files (a)
          total bytes in use        :  115.735 GB/     0.000 GB
      mmfs1/crsp/lab/ucinetid-pi      :red:`1029.799 GB/  1024.000 GB`   2900/100000   files (b)
          total bytes in use        : :red:`1029.799 GB/  1024.000 GB`


.. _fix crsp overquota:

Fix over quotas
^^^^^^^^^^^^^^^

**Fix number of files**

The number of files  quotas are reasonably set at the time of the account
creation. When the quota is exceeded we recommend that users:

* check what they wrote and remove any temporary files
* use ``tar`` or ``zip`` commands to create single files from the directories containing many small files
  and remove original small files. 
* files number quota exceeding in $HOME  is usually related to temp files that
  Jupyter  puts for each web-based access session.  Check how many such files
  you have and remove older files 
  while logged in on HPC3:

  .. code-block:: console

     ls -l /share/crsp/home/npw/.local/share/jupyter/runtime/
     total 1024
     -rw-rw---- 1 panteater panteater 254 Jan 30 14:41 nbserver-114022.json
     -rw-rw---- 1 panteater panteater 562 Jan 30 14:41 nbserver-114022-open.html
     -rw-rw---- 1 panteater panteater 255 Mar 14  2022 nbserver-3966545.json
     -rw-rw---- 1 panteater panteater 562 Mar 14  2022 nbserver-3966545-open.html
     ... cut lines ...
     rm /share/crsp/home/npw/.local/share/jupyter/runtime/nbserver-3966545*

   if you never login on HPC3 but use web-based access only for your CRSP lab
   space you will need to submit a ticket asking us to remove such files. 

**Fix space quota**

Usually quota violations happen when:

* users fill space over quota. Either reduce your usage or buy additional space (see :ref:`crsp allocations`). 
* users use ``rsync`` or ``scp`` commands to transfer the files that results
  in wrong ownership permissions.

  Please see :ref:`fix DFS over quota <dfs over quota>` section that provides info on how to find
  offending files (wrong group permission) and how to fix. 
  The only difference is a path to he written files. 


.. _crsp snapshots:

Snapshots
---------

A snapshot of a file system is a logical, point-in-time, read-only, copy of all files.
It's not really a complete copy. Instead, the file system keeps track of files that are *changed*
or *deleted* after the snapshot was made.  Snapshots are point-in-time copies of the CRSP file system. 

.. _crsp snapshots default:

Default settings
^^^^^^^^^^^^^^^^

By definition, **all snapshots are read-only**, meaning you cannot delete a file from a snapshot.
Restoring a file from a snapshot is as simple as copying the file back to your desired directory/folder.

On CRSP, all snapshots are labeled by date and time. The timezone is GMT (Greenwich Mean Time).

:bluelight:`Snapshots are taken:`

    - daily, keep last 14
    - weekly, keep last 8

.. attention:: Files that were deleted more than 8 weeks ago are gone forever

:bluelight:`Is Snapshot a Backup?`

Not really. Backups are generally thought of as historical copies of files and users could go to a backup to
recover a file from many months ago. Snapshots provide some safety against the common "accidentally deleted" use case.
Files created and deleted in the same time interval between two snapshots are not recorded in any snapshot and have no recovery.
CRSP does not keep historical backups of data.

.. _crsp snapshots location:

Location
^^^^^^^^

Due to the architecture of the underlying filesystem (GPFS)
you must first navigate to the **top level of the CRSP file system**
and then navigate downwards to the correct snapshot to find yours.

This means that you will see names of all possible labs or home area folders (and there are 1000s of them on CRSP).
Rest assured that only you and those you designate can see any files inside.

.. important:: All access permissions are fully enforced, even when navigating snapshots.

Each snapshot is a directory  that is named after its creation date.
The snapshots are held in:

* :tt:`HOME-SNAPSHOTS` - directory for HOME area snapshots
* :tt:`LAB-SNAPSHOTS` - directory for LAB area snapshots

1. **From HPC3**

   Top level of the CRSP file system is mounted as :tt:`/share/crsp` thus
   the snapshots are available in :tt:`/share/crsp/HOME-SNAPSHOTS` and
   :tt:`/share/crsp/LAB-SNAPSHOPTS`.

   For example, a user *panteater* can find HOME area snapshots as:

   .. code-block:: console

      [user@login-x:~]$ ls /share/crsp/HOME-SNAPSHOTS
      @GMT-2021.07.11-10.00.00  @GMT-2021.08.06-01.00.14  @GMT-2021.08.10-13.00.07
      @GMT-2021.07.18-10.00.00  @GMT-2021.08.07-01.00.14  @GMT-2021.08.11-01.00.14
      @GMT-2021.07.25-10.00.00  @GMT-2021.08.08-01.00.14  @GMT-2021.08.11-13.00.07
      @GMT-2021.08.01-10.00.00  @GMT-2021.08.08-10.00.00  @GMT-2021.08.12-01.00.14
      @GMT-2021.08.03-01.00.14  @GMT-2021.08.09-01.00.14  @GMT-2021.08.12-13.00.07
      @GMT-2021.08.04-01.00.14  @GMT-2021.08.09-13.00.07  @GMT-2021.08.13-01.00.14
      @GMT-2021.08.05-01.00.14  @GMT-2021.08.10-01.00.14  @GMT-2021.08.13-13.00.07

   And then browse the contents of a specific snapshot using your UCINetID as:

   .. code-block:: console

      [user@login-x:~]$ ls /share/crsp/HOME-SNAPSHOTS/@GMT-2021.08.08-10.00.00/panteater

2. **From CRSP Desktop**

   In your *CRSP Desktop* application connect to the crsp-top-level
   share connection (it is predefined in the *CRSP Desktop* installation).
   See :ref:`client desktop windows` or :ref:`client desktop mac` for
   detailed instructions.

   Once at the top level, you will find snapshots labeled by their creation date
   in the folders labeled :guilabel:`HOME-SNAPSHOTS` and :guilabel:`LAB-SNAPSHOTS`.

3. **From web browser**

   In your :ref:`client web browser` interface navigate to the CRSP top level,
   you will see a folder structure that is similar to the following:


   .. _crsp lab top level:

   .. figure:: images/crsp-lab-top-level.png
      :align: center
      :alt: crsp lab top level

      File browser top level

   Snapshots are held in the folders labeled :guilabel:`HOME-SNAPSHOTS` and :guilabel:`LAB-SNAPSHOTS`.
   To find available snapshots for LAB area click on :guilabel:`LAB-SNAPSHOTS`:


   .. _crsp lab snapshots:

   .. figure:: images/crsp-lab-snapshots.png
      :align: center
      :alt: crsp lab snapshots

      File browser LAB-SNAPSHOTS

   In this example, the most recent snapshot is the last listed.  Its name indicates the
   time stamp when this snapshot was taken: May 05, 2021 at 19:00:01 (GMT).
   This translates to May 5, 2021 11:00:01 AM (PST).
   This snapshot contains logical copy of all CRSP lab folders, as they were at that point in time.

.. _crsp files recovery:

Deleted Files Recovery
----------------------

A common mistake is an accidental file deletion. In many cases, but not all,
users can retrieve a previous copy of the file.

* If the file you just deleted was created prior to the most-recent snapshot, you can get a
  copy of the file as it was when the snapshot was created.
* *Any changes made after the most recent snapshot are lost.*
* If you wait longer than time specified in :ref:`crsp snapshots default` to recover a deleted file, it is gone forever.

The following steps explain how to recover a deleted file from a snapshot
using different access methods.

1. **From CRSP Desktop**

   Use your CRSP Desktop application to connect to the desired share
   (see :ref:`client desktop windows` or :ref:`client desktop mac` for instructions) then
   use it just like a folder or network drive to copy desired files and folders from a
   specific snapshot.

2. **From HPC3**

   One can use usual Unix commands ``ls``, ``cd``, ``cp`` to find and copy
   desired files and directories from the snapshot to the location where you
   need to restore them.

   For example, a user *panteater*  who has an access to *peterlab* can restore a single file accidentally
   deleted from its LAB area:

   .. code-block::

      [user@login-x:~]$ cd /share/crsp/lab/peterlab/panteater
      [user@login-x:~]$ cp /share/crsp/LAB-SNAPSHOTS/@GMT-2021.08.08-10.00.00/peterlab/panteater/important-file important-file

3. **From web browser**

   In order to recover the file, you must navigate into the
   :ref:`crsp lab top level` and :ref:`crsp lab snapshots`.
   At this point, find the snapshot (folder) that has a copy of your file.

   In the following example the path starts with :guilabel:`LAB-SNAPSHOTS / @GMT-2019.5.13-19.00.1`,
   this indicates that we navigated into a specific snapshot :guilabel:`@GMT-2019.5.13-19.00.1`
   in the LAB area. The rest of the path is the desired file *module-hpc.log-20201011* location.

   Once the desired file is found:

   | (1) select desired files by checking the box left of the file name
   | (2) click :guilabel:`Download` to download selected files to your desired *writable folder*.

   .. centered:: Selecting files in snapshots

   .. image:: images/crsp-lab-snapshot-file.png
      :align: center
      :alt: selecting files in snapshot

   At that point, you have restored from the snapshot your desired files.

   You may also copy the file in your usual manner  per your host operating system
   `Windows <https://www.lifewire.com/how-do-i-copy-a-file-in-windows-2619210>`_,
   `macOS <https://alvinalexander.com/mac-os-x/mac-copy-files-mac-finder-copy-files>`_
   and `Linux <https://www.cyberciti.biz/faq/copy-command>`_.
