.. _crsp:

CRSP
====

.. contents::
   :local:

Overview
--------

CRSP is a network-based multi-Petabyte storage cluster for the UCI campus research community.
It is a reliable and resilient location created for researchers across UCI 
to store and share their research data.

CRSP is available across the network, it supports multiple modes of
storing and retrieving data including web browsers, "folders" on laptops or desktops,
and just another file path on UCI's High-performance computing clusters.

CRSP is funded through central campus to guarantee a fixed amount of no-cost storage to any
faculty member or staff researcher who requests space. These campus funds pay for the people,
the baseline infrastructure, and vendor maintenance required to provide the robust infrastructure.

.. important:: CRSP is only available on the UCI Network or through the campus VPN.

While there are many possible use cases, a driving one is:
   :bluelight:`A faculty researcher and the data needed to support the research lab, graduate students
   and postdocs.  In this model, a lab "area" is created on CRSP and is logically owned by the
   researcher. The lab area owner can specify additional users who have read/write capability
   on the area and how much space each could consume`

.. warning:: CRSP filesystems  must not be used to store personally-identifiable information that would fall
             under guidelines  such as `FERPA <https://studentprivacy.ed.gov/ferpa>`_
             (e.g. Student data) and `HIPAA <https://www.hhs.gov/hipaa/index.html>`_ (health-care data).

             If you are unsure if CRSP is suitable for your data, please refer to general guidance for
             `data security <https://research.uci.edu/human-research-protections/assessing-risks-and-benefits/privacy-and-confidentiality/data-security/>`_
             provided by the `UCI Office of Research <https://research.uci.edu/>`_


.. _crsp to crsp2:

CRSP to CRSP2 Transition
------------------------

On July 16, 2024 CRSP underwent a complete hardware upgrade to replace end-of-life hardware and expand capacity.
After the upgrade

* **All active user/lab files have been copied from CRSP to its replacement (CRSP2)**. If you actively access CRSP now,
  you will be able to do so after the upgrade. Your files will be in the same location as they were prior to upgrade.

* **DUO Multifactor Authentication will be required for ALL desktop clients**. Please 
  see :ref:`Using DUO with CRSP <duo crsp>` for using SSH-keys with strong passwords. Once you have set up key-based
  authentication, you need to re-configure your :ref:`CRSP Desktop Client Bookmark <windows configure share>` to use 
  your key *instead of your password*.

* **The scp (Secure Copy) interface to CRSP is no longer available**. Please 
  see :ref:`Supported Access Methods <crsp access methods>` 

* **Snapshot locations for labs will move**. This is due to an underlying configuration change. See
  :ref:`CRSP Snapshots <crsp snapshots>`.

* **Faculty labs will no longer be automatically created on CRSP2**. Instead, faculty who want to activate their *no-cost*
  CRSP allocation should send an email to hpc-support@rcic.uci.edu. 

.. _crsp technologies:

CRSP technologies
-----------------

**CRSP is a combination of several technologies**
  * It is built with industry leading storage technology to ensure data high availability and resiliency.
  * It is multi-site and is comprised of commodity server components from Dell for cost-effective scaling
    and performance.
  * The underlying parallel file system is :term:`GPFS`  (also known as IBM Spectrum Scale)
  * Additional support and integration software from `Kalray <https://www.kalrayinc.com/products/ngenea>`_.

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

All requests described below must be sent to hpc-support@uci.edu.

.. note:: A PI is a ladder-rank faculty or a researcher who has an exception granted to act as PI on federal grants
          by UCI Office of research.

:underline:`I am a PI on campus and I want to have an access`:
  You may request a no-cost 1TB lab allocation and include:

  - your UCInetID 
  - UCINetIDs and names of the people that you want to add

:underline:`I am a PI and I want to add students/postdocs to my lab`:
  You should send a request and include:

  - your existing CRSP lab name
  - UCINetIDs and names of the people you want to add

:underline:`I am a PI and I want to access my colleagues lab`:
  Your colleague must send a request to grant access to their lab and include:

  - existing CRSP lab name
  - your UCINetIDs

:underline:`I am a PI and I want colleagues outside of UCI to have access to my lab`:
  You must first sponsor a UCINetID (see :ref:`access`) then send a request to grant access.

:underline:`I am a student/psotdoc/researcher and I want to access my PI lab`:
  You should send a request and include:

  - your UCINetID
  - your PI's UCINetID or existing CRSP lab name
  - :red:`You must cc your request to the PI`. 
    Once the ticket is generated (you receive an automated email response) 
    the PI will have to respond to the cc with a confirmation.
    We will not create an account without your PI's confirmation.


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

* It has a very very small allocation per user.  Data on CRSP should be stored in *Lab Areas*
* Not used for sharing with others.
* Is required for Linux accounts and is ONLY used for an account related files.
* :red:`DO NOT use HOME for storing any data`.
* File :tt:`quotas.txt` is created and updated in your $HOME area automatically and
  provides information about your quota status for HOME and LAB areas.

.. _crsp shared:

Shared Area - LAB
^^^^^^^^^^^^^^^^^

This allocation space, called :tt:`LAB`, is a *shared space area* per Space Owner.

Space owner grants explicit access for this area to Grantees and decides how to allocate the space
among its group members.

The LAB areas provide the most flexibility for access control and sharing:

* The space owner by default has read access to every file and directory in the LAB
* Only the space owner has the ability to create files or new directories in the top-level of the LAB area.
* Grantees have a personal directory  named with their UCINetID.
  Files stored there by the grantee are viewable only by the space owner and the grantee.
* A directory called :tt:`share` is available to all members of the lab.
  Anyone in the lab can read/write files stored under it.
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

  .. figure:: images/crsp/crsp-lab-share-highlight.png
     :align: center
     :alt: crsp lab share example

     Example LAB top-level folder (using MAC CRSP Desktop)

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

If you were given an access to CRSP account, to access it via the methods
described below use:

 :login name: your UCINetID
 :password: your password associated with your UCINetID

We do not set or change passwords.

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
   | :ref:`client web browser`    | This access is used for *light weight* CRSP resource usage, supports file or directory    |
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

- **CRSP allocations are provided for UCI faculty members.**
  In general, users do not get a default CRSP allocation.
  The allocation owners can grant access to their spaces to students, postdocs, and other faculty members.
 
- Users who are granted access have $HOME area which is used only by account related files.
  This area is NOT for storing anything else.

- User who are granted access to one or more  PI's lab areas (see :ref:`crsp areas`)
  may have additional quota limits set by their PIs for the group area.

- **All CRSP quotas are enforced in two areas: total space used and number of
  files.**

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

Snapshots - Deleted Data Recovery
---------------------------------

A snapshot of a file system is a *logical, point-in-time, read-only, copy* of all files.
It's not really a complete copy. Instead, the file system keeps track of files that are *changed*
or *deleted* after the snapshot was made.  CRSP Snapshots are point-in-time copies of the CRSP file system. 

.. _crsp snapshots default:

Default settings
^^^^^^^^^^^^^^^^

By definition, **all snapshots are read-only**, meaning you cannot delete a file from a snapshot.
Restoring a file from a snapshot is as simple as copying the file back to your desired directory/folder.

On CRSP, all snapshots are labeled by date and time. The timezone is GMT (Greenwich Mean Time).

:bluelight:`Snapshots are taken:`
  - Daily, kept for 89 days 
  - .. attention:: Files that were deleted/changed more than  90 days ago are gone forever

:bluelight:`Is Snapshot a Backup?`
  Almost. Backups are generally thought of as *historical* copies of files to an *offsite location*. 
  In a traditional backup, users could go back in time months or years to recover a file. 
  A snapshot is a point-in-time *virtual* copy of a filesystem that is kept on the filesystem itself. 

  Snapshots provide some safety against the common "I accidentally deleted it" case.
  Files created and deleted in the same time interval between two snapshots are not recorded in any 
  snapshot and have no recovery.

  CRSP does not keep historical backups of data. But, there is an *offsite* copy of all CRSP data. In essence, every file
  in CRSP has *three* copies - two (one in each sub cluster) in Irvine and one (offsite) in San Diego.

  .. note::
    * *Snapshots* allow you **self-service restore** of files/folders that you have recently deleted or ovewritten.
    * *Offsite backups* protect against total failure of CRSP itself (highly unlikely). 

:bluelight:`When I've found a good snapshot, what do I do?`
  **Answer:**  Just copy the file or folders that you want to restore *from the snapshot* back to the area where you 
  want the file so that you can access it normally. 

.. _crsp snapshots location:

Locations of Snapshots
^^^^^^^^^^^^^^^^^^^^^^

* Each Lab has its own :tt:`.snapshots` directory
* To restore data into your ``$HOME`` area, you must use the web console


.. _crsp lab snapshots:

Restoring Lab Data from Snapshots 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since most CRSP data is stored in a lab area, this most likely the applicable guide for recovering your data.

:bluelight:`1. Using HPC3`
  Located at the top-level of your lab directory is the :tt:`.snapshots` directory. 
  This directory is owned by the root user and cannot be changed by any user.  

  **Navigate to the** :tt:`.snapshots` **directory**, where you will see directories that 
  have names that look like *@GMT-YYYY.MM.DD-hh.mm.ss*.  This encoding
  indicates date and time when the snapshot was taken. For
  the lab *ppapadop*, on HPC3 you would find the *ppapadop* snapshots as below:

     .. code-block:: console

        [user@login-x:~]$ ls -tr1 /share/crsp/lab/ppapadop/.snapshots
        @GMT-2024.07.15-07.00.00
        @GMT-2024.07.14-07.00.00
        @GMT-2024.07.13-07.00.00
        @GMT-2024.07.12-07.00.00
        @GMT-2024.07.11-07.00.00
        @GMT-2024.07.10-07.00.00
        @GMT-2024.07.09-07.00.00
        @GMT-2024.07.08-07.00.00
        @GMT-2024.07.07-07.00.00
        @GMT-2024.07.06-07.00.00
        @GMT-2024.07.05-07.00.00


:bluelight:`2. Using the CRSP Desktop`
  On a Mac, the :tt:`.snapshots` folder is hidden by default.  
  See :ref:`Mac connect share section <mac connect share>` for a reference how
  to view hidden folders in the :guilabel:`Finder`.

  Click on the :tt:`.snapshots` folder at the top level of your already-configured lab share:

  .. _crsp lab snaphot:

  .. figure:: images/crsp/crsp-lab-snapshot.png
     :align: center
     :alt: crsp lab .snapshots directory

     :tt:`.snapshots` directory or folder at the top-level of the lab

  Then you will see a set folders (tip: sort by name), that has the date and time when each snapshot was taken:

   .. _crsp lab snaphot nav:

   .. figure:: images/crsp/crsp-lab-snapshot-nav.png
      :align: center
      :alt: crsp lab .snapshots directory contents

      Example folders in :tt:`.snapshots` directory

  Continue navigating to a date where you believe a copy of your *deleted* or *ovewritten* file is located.
  **Copy it back to your working area.**

:bluelight:`3. Using Web Interface`
  This is very similar to the above, follow the following rough steps

  #. Open your web browser to `https://access.crsp.uci.edu/myfiles/ <https://access.crsp.uci.edu/myfiles/>`_
  #. Click on :guilabel:`My-Labs`
  #. Navigate to your lab and its :tt:`.snapshots` folder
  #. Find the date of interest, and then *download* the file(s)/folder(s) to your local system

Restoring $HOME Data
^^^^^^^^^^^^^^^^^^^^

Snapshots for the home area are kept in one place for ALL users.  If you are on HPC3,
you can see all the  home snapshots at :tt:`/share/crsp/home/.snapshots`.  This will have the same
naming format *@GMT-YYYY.MM.DD-hh.mm.ss* as shown above in :ref:`Lab Area Snapshots <crsp lab snapshots>`.
You, can navigate into one of these directories and you will see *all* user
home areas names. You will only have permission to further descend into *your home area*

:bluelight:`Using the Web Interface`
  Since ``$HOME`` areas usually don't contain signficant data, it can be a little more straightforward
  to use the Web Interface. 


  #. Open your web browser to `https://access.crsp.uci.edu/myfiles/ <https://access.crsp.uci.edu/myfiles/>`_
  #. Click on :guilabel:`Home-Snapshots`
  #. Click on the date of interest. 
     You will be looking at the state of your ``$HOME`` on that date
  #. Download the file(s)/folder(s) to your local system

  .. note:: if you don't see the :guilabel:`Home-Snapshots`, but see a folder listing instead, then click
     in the upper right on the :guilabel:`Power Icon`
