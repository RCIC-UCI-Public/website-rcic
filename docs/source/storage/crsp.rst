.. _crsp:

CRSP 
=====

Overview
--------

CRSP is a network-based multi-Petabyte storage cluster for the UCI campus research community.
It is being put in place so that researchers across UCI have a reliable and resilient location
to store their research data and share with defined groups.

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
  - Researchers who require more capacity than the baseline allocation, can purchase additional capacity,
    Please see  :ref:`recharge storage rates` and :ref:`buy crsp`

In general, users do not get a default CRSP allocation.
The allocation owners can grant access to their spaces to students, postdocs, and other faculty members.

The allocation is associated with an account.

.. _getting crsp account:

Getting CRSP account
--------------------

All requests described below must be sent to hpc-support@uci.edu

* **I'm a researcher on campus**
  If you are a ladder-rank faculty or have an exception granted to act as PI on federal grants
  by UCI Office of research, your account should be pre-created. If you still do not have
  access, please send us a request.
* **I'm a student/postdoc**
  Your PI should send a request and include:

  - your UCINetID
  - indicate if your space should be limited. 

  PI may combine multiple requests in a single email.

* **I'm a researcher and I want to access my colleagues lab**
  Your colleague must send a request and ask for access for you to their lab.

* **I'm a researcher and I want colleagues outside of UCI to have access to my lab**
  You must first sponsor a UCINetID (see :ref:`access`) then send a request to grant access.


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

.. note:: A :tt:`directory` meaning on Unix  is equivalent to a :tt:`folder` on MacOS, Windows.
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
There are two Unix groups pre-defined for all labs:

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
   | :ref:`client desktop windows`| *CRSP Desktop* clients are for accessing CRSP from Windows and MacOS laptops.             |
   | :ref:`client desktop mac`    | We provide licensed and branded version of a commercial software *Mountain Duck*.         |
   |                              |                                                                                           |
   |                              | .. important::                                                                            |
   |                              |                                                                                           |
   |                              |    Although CRSP storage system could be accessed via other commercial or open source     |
   |                              |    software *CRSP Desktop* is the currently supported SFTP based software. Other software |
   |                              |    support is provided only on a best effort basis (FileZilla, WinSCP, CyberDuck).        |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client web browser`    | This access is used for *lightweight* CRSP resource usage, supports file or direvtory     |
   |                              | uploads/downloads and provides in-browser edit capabilities for certain file types.       |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client sshfs`          | *SSHFS* can be used for accessing CRSP shares from a Linux laptop/desktop.                |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client from hpc3`      | *NFS mount* on HPC3 provides and access to the CRSP's LAB and HOME areas.                 |
   +------------------------------+-------------------------------------------------------------------------------------------+


TODO Consult our link:debugging.html[Troubleshooting Guide] if you have  trouble accessing your CRSP shares.

.. _crsp quotas:

Quotas
------

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
      == Storage Areas that you own  ==
      == Your use in Paths to which you have access  ==
           /mmfs1/crsp/home                        0.001 GB/     0.020 GB      6/40       files
                total bytes in use          :    115.735 GB/     0.000 GB
           /mmfs1/crsp/lab/ucinetid-pi            39.799 GB/  1024.000 GB   2900/100000   files
                total bytes in use          :    374.092 GB/  1024.000 GB

   The first command above gives an idea when the file was updated.
   The second command shows that the user *panteater*:

   * does not own any area (user is not a PI).
   * has no usage in HOME area :tt:`/mmfs1/crsp/home`, this is a correct behavior.
     The 0.001 GB is used only by account related files.
   * is a member of ucinetid-pi LAB and used 39.799 GB of the allocated 1024 GB LAB area
     in :tt:`/mmfs1/crsp/lab/ucinetid-pi`. The total usage of the LAB area by all lab members is 374.092 GB.
   
   Note the path naming on CRSP and HPC3:

   ==== ================================= ==================================
   Area Path on CRSP                      Path on HPC3
   ==== ================================= ==================================
   HOME :tt:`/mmfs1/crsp/home`            :tt:`/share/crsp/home` 
   LAB  :tt:`/mmfs1/crsp/lab/ucinetid-pi` :tt:`/share/crsp/lab/ucinetid-pi`
   ==== ================================= ==================================

  .. note:: | If you are a PI of the lab you will to see the usage of your lab quota for all lab members.
            | If you are a member of the lab you will see only what you have used from the lab quota allocation.


.. _crsp snapshots:

CRSP Snapshots
--------------

TODO


.. _crsp files recovery:

Deleted Files Recovery
-----------------------

TODO

Mistakes happen and a common one is an unintentional deletion. In many cases, but not all,
users can retrieve a previous copy of the file.  CRSP uses file system snapshots
to create  read-only copies of user data at specific points in time.

* Currently, CRSP snapshots the file system every 12 hours and retains snapshots for 1 week.
* If the file you just deleted was created prior to the most-recent snapshot, you can get a
  copy of the file as it was when the snapshot was created. *Any changes made after the most recent snapshot are lost.*
* *If you wait longer than 7 days to recover a deleted file, it is gone forever.*

To recover a lost file, please see the <<snapshot-recovery.txt#, recovery guide>>.
