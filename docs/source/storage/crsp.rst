.. _crsp:

CRSP
====

.. contents::
   :local:

Overview
--------

CRSP is a reliable and resilient network-based multi-Petabyte storage cluster
for the UCI campus research community to store and share their research data.

CRSP is funded through central campus to guarantee a fixed amount of no-cost storage to any
faculty member or staff researcher who requests space. These campus funds pay for the people,
the baseline infrastructure, and vendor maintenance required to provide the robust infrastructure.

:bluelight:`While there are many possible use cases, a driving one is`:
  A faculty researcher and the data needed to support the research lab, graduate students
  and postdocs.  In this model, a *Lab Area* is created on CRSP and is logically owned by the
  researcher. The *Lab Area Owner* can specify additional users who have read/write capability
  on the area and how much space each could consume.

  .. warning:: | CRSP filesystems  must not be used to store personally-identifiable information that
                 would fall under guidelines  such as `FERPA <https://studentprivacy.ed.gov/ferpa>`_
                 (Student data) and `HIPAA <https://www.hhs.gov/hipaa/index.html>`_ (health-care data).
               | If you are unsure that CRSP is suitable for your data, please refer to general guidance for
                 `data security <https://research.uci.edu/human-research-protections/assessing-risks-and-benefits/privacy-and-confidentiality/data-security/>`_
                 provided by the `UCI Office of Research <https://research.uci.edu/>`_

:bluelight:`CRSP is a combination of several technologies`
   * It is built with industry leading storage technology to ensure data high availability and resiliency.
   * It is multi-site and is comprised of commodity server components from Dell for cost-effective scaling
     and performance.
   * The underlying parallel file system is :term:`GPFS` (a.k.a IBM Spectrum Scale)
   * Additional support and integration software from `Kalray <https://www.kalrayinc.com/products/ngenea>`_.

:bluelight:`Features include`
  * **CRSP is only available on the UCI Network or through the campus VPN**,
  * An active-active storage system setup between two hosting locations for high availability and redundancy,
    with fully fault tolerant high speed networking.
  * End-to-End 24x7 software and hardware support.
  * A fully encrypted file system, featuring
    `encryption at REST <https://www.ibm.com/docs/en/search/encryption?scope=STXKQY>`_
    ensuring user data security.
  * A file system design that has massive scaling capabilities without compromising performance.
  * A front-end access layer design that is capable of scaling horizontally as demand grows.
  * Several user access methods are in place, with enterprise level support.
    All access mechanisms are fully load-balanced between data centers.
    User access methods for data storing and retrieval assure a superior level of user experience:

      * web browsers
      * *folders* on laptops or desktops
      * file path on UCI's High-performance computing clusters (HPC3).


.. TODO  rm image below or make a new one
.. .. centered:: A simplified illustration of CRSP architectural diagram

.. .. image:: images/crsp-arch.png
   :align: center
   :alt: crsp  architecture

:bluelight:`CRSP to CRSP2 Transition`
  On July 16, 2024 CRSP underwent a complete hardware upgrade to replace end-of-life hardware and expand capacity.
  After the upgrade:

  .. _crsp to crsp2:
  
  .. table::
     :widths: 35 65
     :class: noscroll-table

     +----------------------------------------------------+-------------------------------------------------------------------------------------+
     | Change                                             | What to do                                                                          |
     +====================================================+=====================================================================================+
     | All active user/lab files were copied from CRSP    | If you actively access CRSP now, you will be able to do so after the upgrade.       |
     | to its replacement (CRSP2)                         | Your files will be in the same location as they were prior to upgrade.              |
     +----------------------------------------------------+-------------------------------------------------------------------------------------+
     | DUO Multifactor Authentication is required for ALL | Please see :ref:`Using DUO with CRSP <duo crsp>` for using SSH-keys with strong     |
     | desktop clients                                    | passwords. Once you have set up key-based authentication, you need to re-configure  |
     |                                                    | your :ref:`CRSP Desktop Client Bookmark <windows configure share>` to use           |
     |                                                    | your ssh key *instead of your password*.                                            |
     +----------------------------------------------------+-------------------------------------------------------------------------------------+
     | The Secure Copy interface (scp)                    | Please see :ref:`Supported Access Methods <crsp access methods>`.                   |
     | is no longer available                             |                                                                                     |
     +----------------------------------------------------+-------------------------------------------------------------------------------------+
     | Lab Snapshots locations were moved                 | This is due to an underlying configuration change.                                  |
     |                                                    |                                                                                     |
     |                                                    | See :ref:`CRSP Snapshots <crsp snapshots>`.                                         |
     +----------------------------------------------------+-------------------------------------------------------------------------------------+
     | Faculty labs are no longer automatically created   | Faculty who want to activate their *no-cost*                                        |
     |                                                    | CRSP allocation please see :ref:`getting crsp account`.                             |
     +----------------------------------------------------+-------------------------------------------------------------------------------------+
 
.. _getting crsp account:

Getting CRSP Account
--------------------

All requests described below must be sent to hpc-support@uci.edu.

:underline:`I am a PI on campus and I want to have an access`:
  You may request a no-cost 1TB lab allocation and include:

  - your UCInetID
  - UCInetIDs and names of the people that you want to add

:underline:`I am a PI and I want to grant access to my lab to students/postdocs/colleagues`:
  You should send a request and include:

  - your existing CRSP lab name
  - UCInetIDs and names of the people you want to add

:underline:`I am a PI and I want to access my colleagues lab`:
  Your colleague must send a request to grant access to their lab and include:

  - existing CRSP lab name
  - your UCInetIDs

:underline:`I am a PI and I want colleagues outside of UCI to have access to my lab`:
  You must first :ref:`sponsor a UCInetID <access>` then send a request to grant access.

:underline:`I am a student/psotdoc/researcher and I want to access my PI lab`:
  You should send a request and include:

  - your UCInetID
  - your PI's UCInetID or existing CRSP lab name
  - :red:`You must cc your request to the PI`.
    Once the ticket is generated (you receive an automated email response)
    the PI will have to respond to the cc with a confirmation.
    We will not create an account without your PI's confirmation.

.. _crsp allocations:

Allocations
-----------

CRSP is funded through central campus to guarantee a fixed amount of no-cost storage to any PI
who requests space. These campus funds pay for the people, the baseline infrastructure,
and vendor maintenance required to provide the robust infrastructure.

**PI** is a ladder-rank faculty or a researcher who has an exception granted to act as PI on federal grants
by UCI Office of research.

Each CRSP allocation is associated with a UCI's PI account and is provided  as follows:
  :bluelight:`No-cost baseline allocation`
    - 1TB quota per PI

  :bluelight:`Recharge allocation`
    - PIs who require more capacity than the baseline allocation, can purchase additional capacity.
      Please see  :ref:`recharge storage rates` and :ref:`buy crsp`


Storage space on CRSP has the concepts of:
  :bluelight:`Space Owners`:
    * Are PIs and UCI employees serving as PI/Co-PI on an extramural grant
      and are all ladder faculty.
    * Are entitled to a baseline allocation and can purchase more space.
    * Can store files in their Lab and can partition Lab into shared and no-shared area.
    * Can grant access to their Lab storage space to Grantees.

  :bluelight:`Grantees`:
    * Students, postdocs, and other faculty members who are granted access by Space owners.
      There are no user owned private allocations.
    * Can access the Lab space to which they have been granted access by Space Owners and store files there

Storage space on CRSP is divided into:
  * :ref:`Private Area <crsp private>`
  * :ref:`Shared Area <crsp shared>`

.. note:: A :tt:`directory` meaning on Unix  is equivalent to a :tt:`folder` on macOS or  Windows.
          In what follows, we will use the term :tt:`file` to mean
          :tt:`file`, :tt:`folder`, or :tt:`directory`.

.. _crsp private:

Private Area - HOME
^^^^^^^^^^^^^^^^^^^

This allocation space, called :tt:`HOME`, is for $HOME directories:

  * It has a very very small allocation per user. Not used for sharing with others.
  * Is required for Linux accounts and is ONLY used for an account related files.
  * File :tt:`quotas.txt` is created and updated in your $HOME area automatically and
    provides information about your quota status for HOME and Lab areas.
  * :red:`Do not use HOME for storing any data`. All data on CRSP must be stored in *Lab Areas*.

.. _crsp shared:

Shared Area - Lab
^^^^^^^^^^^^^^^^^

This allocation space, called `Lab`, is a *shared space area* per Space Owner.
The Lab areas provide the most flexibility for access control and sharing:

  * The Allocation quota is for the  whole `Lab` area allocation and is a sum of what is stored
    in :tt:`share`  and in all personal directories.
  * Each Grantee has a personal directory (named with grantee's UCInetID). Only
    grantee and the Space Owner can read/write files in this directory.
  * A directory called :tt:`share` is available to all members of the lab.
    Anyone in the lab can read/write files stored under it.
  * The Space Owner

    * grants explicit access for this area to Grantees and decides how to allocate
      the space among its group members and can place limits on individuals Grantees.
    * has the ability to create files or new directories in the top-level of the `Lab` area.
    * by default has read access to every file and directory in the `Lab` area.

CRSP has many (and sometimes competing) goals for access, sharing, security,
manageability, and simplicity for researchers.  One of the technical complexities
of CRSP is that the underlying file system and access enforcement mechanisms are
defined in Unix, but most users access is from Mac and Windows environments.

On Unix an independent access controls to all files given to three different entities:

  * The *owner* of the file. This is the UCInetID that originally created the file
  * The *group* of the file. A group who might have access to this file
  * The *world* (or others). Everyone else on CRSP

.. important:: In CRSP Lab areas sharing is controlled by **group permissions**
               and by who is a member of the particular group. **The world has no privilege
               to read or write files in any Lab area**.

               File owners files can make files explicitly private by
               removing read/write group permissions.

.. _default crsp lab:

Default Lab Setup
^^^^^^^^^^^^^^^^^

For each Lab area, the `PI` is the owner of the space.
There are two Unix groups predefined for all labs:

  * :tt:`pi_lab`: only the lab owner is in this group
  * :tt:`pi_lab_share`: all members of the lab including the lab owner.

**Example Lab**

  In the following, we will use the Lab for a PI *ppapadop*:

  * *ppapadop* is in the group :tt:`ppapadop_lab` and is only member of this group.
  * *ppapadop* is in the group :tt:`ppapadop_lab_share`.
  * *ckhacher*, *itoufiqu*, *tandriol*, *iychang* are in the group :tt:`ppapadop_lab_share`.
    They are Lab members (grantees) that were given an access to the Lab area  by the PI.

  .. figure:: images/crsp/crsp-lab-share-highlight.png
     :align: center
     :alt: CRSP Lab share example

     Example Lab top-level folder (using MAC CRSP Desktop)

  This shows that for the :tt:`ppapadop` Lab on CRSP:

  1. User *ppapadop* who is a PI can see all files anywhere in the Lab area.
  #. All Lab members can read/write files in :tt:`share` area.
  #. Lab members in :tt:`ppapadop_lab_share` group are: *ppapadop*, *ckhacher*, *itoufiqu*, *tandriol*, *iychang*.
     Each Lab member has a folder named by UCInetID that is private to the
     user and to the PI.

     * only *ppapadop* and *itoufiqu* users can access files in the :tt:`itoufiqu` folder.
     * only *ppapadop* and *ckhacher* users can access files in the :tt:`ckhacher` folder.
     * similar access for the remaining Lab members' folders.

.. _crsp access:

Accessing  CRSP
---------------

| You must either be on the campus network or connected to the
  `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ to access CRSP.
| Your login credentials for all access methods described below are:

  :login name: your UCInetID
  :password: | your password associated with your UCInetID
             | :red:`We do not set or change passwords.`

You can access your granted CRSP storage from Windows, MAC, and Linux systems
via a few methods. The links in the table below provide installation
instructions:

.. table::
   :widths: 30 70
   :class: noscroll-table

   +----------------------------------------------------+-------------------------------------------------------------------------------------+
   |  **Method**                                        | **Description**                                                                     |
   +----------------------------------------------------+-------------------------------------------------------------------------------------+
   | :ref:`CRSP Desktop Windows<client desktop windows>`| *CRSP Desktop* clients are for accessing CRSP from Windows and macOS laptops.       |
   | :ref:`CRSP Desktop Mac <client desktop mac>`       | We provide licensed and branded version of a commercial software *Mountain Duck*.   |
   +----------------------------------------------------+-------------------------------------------------------------------------------------+
   | :ref:`client web browser`                          | This is for *light weight* CRSP resource usage, supports file or directory          |
   |                                                    | uploads/downloads and provides in-browser edit capabilities for certain file types. |
   +----------------------------------------------------+-------------------------------------------------------------------------------------+
   | :ref:`client sshfs`                                | *SSHFS* can be used for accessing CRSP from a Linux laptop/desktop.                 |
   +----------------------------------------------------+-------------------------------------------------------------------------------------+
   | :ref:`client from hpc3`                            | *NFS mount* provides and access to the CRSP's Lab and HOME areas from HPC3.         |
   +----------------------------------------------------+-------------------------------------------------------------------------------------+

.. attention::

   | The  **CRSP Desktop** client is the currently supported SFTP based software.
   | Although CRSP storage system could be accessed via other
     desktop clients such as FileZilla, WinSCP, CyberDuck, their
     support is provided only on a best effort basis.

Consult our :ref:`crsp troubleshoot` if you have trouble accessing your CRSP area.

.. _crsp quotas:

Quotas
------

All CRSP-based allocations have quotas enforced in:
:underline:`total space used` and :underline:`number of files`.

:red:`No writing in Private Area $HOME:`
  * All CRSP users have $HOME. :ref:`This very smlal area is used only by account related files <crsp private>`.

When writing in Shared Area - Lab:
  * All members of the group contribute to the quota in group area.
    It's the sum total usage that counts.
  * Users with access to :ref:`PI's lab areas <crsp shared>`
    may have separate quota limits set by their PIs.
  * Quotas can be exceeded in :underline:`number of files`, :underline:`total space used` or both.
  * When quotas are exceeded, all group users can no longer write in the affected
    filesystem  and will need to remove some files and directories to free space.

.. important:: Users can't change quotas, but can submit a ticket asking to be added to access their PI's lab.
               Please follow
               :ref:`I am a student/psotdoc/researcher and I want to access my PI lab <getting crsp account>`.

.. _crsp check quotas:

How to check
^^^^^^^^^^^^

.. note:: | **PI of the lab** will to see the usage of your lab quota for all lab members.
          | **Member of the lab** will see only what member have used from the lab quota.

There are two ways to check your quotas:

**Using a web browser:**

  * In a new browser tab or window open URL `https://access.crsp.uci.edu/quota <https://access.crsp.uci.edu/quota[https://access.crsp.uci.edu/quota>`_
  * You will be asked to authenticate yourself (DUO).
  * Once successful you  will see a simple text page with quotas for HOME and Lab areas.
  * When done, close the browser tab/window, there is no logout from this page.

**When logged on HPC3:**

  The CRSP quota  info is updated on a regular basis and is put in your $HOME area on CRSP
  in the file :tt:`/share/crsp/home/UCInetID/quotas.txt`. For example, for a user *panteater*:

  1. The ``ls`` command gives an idea when the file was updated:

     .. code-block:: console

        [user@login-x:~]$ ls -ld /share/crsp/home/panteater
        drwx-----T 7 panteater panteater 2048 May 10 15:28 /share/crsp/home/panteater

  2. The next command ``cat`` shows the file content:

     .. code-block:: console

        [user@login-x:~]$ cat  /share/crsp/home/panteater/quotas.txt
        Quota Report for panteater : 06/12/23 17:30
        == Storage Areas that you own ==                                               (see a)
        == Your use in Paths to which you have access  ==
           /mmfs1/crsp/home                 0.001 GB/     0.020 GB     6/40      files (see b)
                total bytes in use      : 115.735 GB/     0.000 GB
           /mmfs1/crsp/lab/UCInetID-pi     39.799 GB/  1024.000 GB  2900/100000  files (see c)
                total bytes in use      : 374.092 GB/  1024.000 GB

     From the above output, the user *panteater*:

       a. Does not own any area (user is not a PI).
       #. Has no usage in HOME area :tt:`/mmfs1/crsp/home`, this is a correct behavior.
          The 0.001 GB is used only by account related files. Currently the user
          used 6 out of 40 files (40 is a quota).
       #. Is a member of UCInetID-PI Lab and used 39.799 GB of the allocated 1024 GB Lab area
          in :tt:`/mmfs1/crsp/lab/UCInetID-pi` and 2900 files (quota 100000).
          The total usage of the Lab area by all lab members is 374.092 GB.

     The path naming correspondence between CRSP and HPC3:

     ==== ================================= ==================================
     Area Path on CRSP                      Corresponds to Path on HPC3
     ==== ================================= ==================================
     HOME :tt:`/mmfs1/crsp/home/UCInetID`   :tt:`/share/crsp/home/UCInetID`
     Lab  :tt:`/mmfs1/crsp/lab/UCInetID-pi` :tt:`/share/crsp/lab/UCInetID-pi`
     ==== ================================= ==================================

.. _crsp over quota:

Over quotas
^^^^^^^^^^^

When quota is filled either in used space or in number of files, the users will not be able to write any files
or directories and submitted jobs will fail with :red:`quota exceeded errors`.

For example, the following output of quotas check show the quotas exceeded for
the user *panteater* in number of files (a) in storage used (b):

.. parsed-literal::

      mmfs1/crsp/home                    0.014 GB/     0.020 GB     :red:`40/40`       files (a)
          total bytes in use        :  115.735 GB/     0.000 GB
      mmfs1/crsp/lab/UCInetID-pi      :red:`1029.799 GB/  1024.000 GB`   2900/100000   files (b)
          total bytes in use        : :red:`1029.799 GB/  1024.000 GB`

Form now on:
  * if *panteater* is trying to connect to CRSP using Desktop CRSP client, the connection will fail
  * if any other user in the lab trying to write in Shared Lab area, there will be a quota error.

.. _fix crsp overquota:

Fix over quotas
^^^^^^^^^^^^^^^

**Fix number of files**
  :underline:`The number of files  quotas are reasonably` set at the time of the account
  creation. When the quota is exceeded we recommend that users:

  * Check what they wrote and remove any temporary files.
  * Use ``tar`` or ``zip`` commands to create single files from the directories containing many small files
    and remove original small files. Compressed files use less space.
  * files number quota exceeding in :tt:`$HOME` is usually related to temporary files created
    by Jupyter for each web-based access session.

	While logged in on HPC3, check how many such files you have and remove older ones:

    .. code-block:: console

       ls -l /share/crsp/home/panteater/.local/share/jupyter/runtime/
       total 1024
       -rw-rw---- 1 panteater panteater 254 Jan 30 14:41 nbserver-114022.json
       -rw-rw---- 1 panteater panteater 562 Jan 30 14:41 nbserver-114022-open.html
       -rw-rw---- 1 panteater panteater 255 Mar 14  2022 nbserver-3966545.json
       -rw-rw---- 1 panteater panteater 562 Mar 14  2022 nbserver-3966545-open.html
       ... cut lines ...
       rm /share/crsp/home/panteater/.local/share/jupyter/runtime/nbserver-3966545*

    .. note:: If you only use web-based access for your CRSP lab space and never
       login on HPC3 you will need to submit a ticket asking us to remove such files.

**Fix space quota**
  Usually quota violations happen when:

  * Users fill space over quota. Either reduce your usage (remove  or compress some files)
    or buy additional space (see :ref:`crsp allocations`).
  * | Users run ``rsync`` or ``scp`` to transfer the files that results in wrong permissions.
    | Please see :ref:`fix DFS over quota <dfs over quota>`
      section for info how to find files with wrong group permission and how to fix them.
      The only difference for CRSP is a path to the written files.

.. _crsp snapshots:

Snapshots
---------

A snapshot of a file system is a *logical, point-in-time, read-only, copy* of all files in a given CRSP file system.
It's not really a complete copy.  Instead, the file system keeps track of files that are *changed*
or *deleted* after the snapshot was made.

:bluelight:`Default settings`
  * **All snapshots are read-only**, you cannot delete a file from a snapshot.
  * All snapshots are labeled by date and time, the timezone is GMT (Greenwich Mean Time).
    The names look like *@GMT-YYYY.MM.DD-hh.mm.ss*.
  * Snapshots are taken daily and kept for 89 days.
  * :red:`Files that were deleted/changed more than 90 days ago are gone forever`.
  * Restoring a file from a snapshot is as simple as copying the file back to your desired location.
  * Each Lab has its own :tt:`.snapshots` directory.
  * Snapshots for the home area are kept in one place for ALL users.

:bluelight:`Is Snapshot a Backup?`
  Almost. Backups are generally thought of as *historical* copies of files to an *offsite location*.
  In a traditional backup, users could go back in time months or years to recover a file.
  A snapshot is a *point-in-time virtual copy* of a filesystem that is kept on the filesystem itself.

  :Snapshots: provide some safety against the common `I accidentally deleted it` case.
              Snapshots allow you **self-service restore** of files/folders that you have recently deleted or overwritten.
              Files created and deleted in the same time interval between two snapshots are not recorded in any
              snapshot and have no recovery.

  :Offsite backups: protect against total failure of CRSP itself (highly unlikely).
           CRSP does not keep historical backups of data. But, there is an *offsite* copy of all CRSP data. In essence, every file
           in CRSP has *three* copies - two (one in each sub cluster) in Irvine and one (off site) in San Diego.

.. _crsp files recovery:

Deleted Files Recovery
-----------------------

**Restoring Lab Data from Snapshots**
  There are three ways to recover your data that was stored in the Lab area.

  :bluelight:`Using HPC3`
    Located at the top-level of your lab directory is the :tt:`.snapshots` directory.
    This directory is owned by the root user and cannot be changed by any user.

    #. Navigate to the :tt:`.snapshots` directory, where you will see directories that
       have names in the format *@GMT-YYYY.MM.DD-hh.mm.ss*.  This encoding
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

    #. Check snapshots for the presence of desired files at the desired time stamp.
    #. Once a good snapshot is identified, copy files or folders that you want to restore from
       the snapshot back to the area where you want the file so that you can access it normally.

  :bluelight:`Using the CRSP Desktop`
    On a Mac, the :tt:`.snapshots` folder is hidden by default.
    See :ref:`Mac connect share section <mac connect share>` for a reference how
    to view hidden folders in the :guilabel:`Finder`.

    #. Click on the :tt:`.snapshots` folder at the top level of your already-configured lab share:

       .. _crsp lab snapshot:

       .. figure:: images/crsp/crsp-lab-snapshot.png
          :align: center
          :alt: crsp lab .snapshots directory

          :tt:`.snapshots` folder at the top-level of the lab

    #. You will see a set folders (tip: sort by name), that have the date and time when each snapshot was taken:

       .. _crsp lab snapshot nav:

       .. figure:: images/crsp/crsp-lab-snapshot-nav.png
          :align: center
          :alt: crsp lab .snapshots directory contents

          Example folders in :tt:`.snapshots` folder

    #. Navigate to a date where you believe there is a copy of your deleted or overwritten file.
    #. Copy desired files back to your working area.

  :bluelight:`Using Web Interface`
    This is very similar to the above

    #. Open your web browser to `https://access.crsp.uci.edu/myfiles/ <https://access.crsp.uci.edu/myfiles/>`_
    #. Click on :guilabel:`My-Labs`
    #. Navigate to your lab and its :tt:`.snapshots` folder
    #. Find the date of interest, and then *download* the files/folders to your local system

**Restoring $HOME Data**

  Snapshots for the home area are kept in one place for ALL users.

  Since ``$HOME`` areas usually don't contain significant data, it can be a more straightforward
  to use the Web Interface.

  :bluelight:`Using HPC3`
    #. You can see all the home snapshots in :tt:`/share/crsp/home/.snapshots`.
       They will have naming format *@GMT-YYYY.MM.DD-hh.mm.ss*.
    #. You can navigate into one of these snapshot directories and you will see *all* user
       home areas names. **You will only have permission to further descend into your home area**.
    #. Once  a good snapshot is found, just copy files or folders that you want to restore from the snapshot back to $HOME.

  :bluelight:`Using Web Interface`

    #. Open your web browser to `https://access.crsp.uci.edu/myfiles/ <https://access.crsp.uci.edu/myfiles/>`_
    #. Click on :guilabel:`Home-Snapshots`
    #. Click on the date of interest. You will be looking at the state of your ``$HOME`` on that date
    #. Download the files/folders to your local system

    .. note:: if you don't see the :guilabel:`Home-Snapshots`, but see a folder listing instead, then click
       in the upper right on the :guilabel:`Power Icon`
