.. _crsp annex:

CRSP ANNEX
==========

Overview
--------

:bluelight:`20-Oct-2023`

CRSP was procured in 2018 and deployed into production in 2019 and is  *at capacity* with no practical path to expand its local 
storage to accomodate new (large) storage requests.  RCIC has been in the process of procuring a replacement for CRSP (called 
CRSP-2) to double storage capacity, have  significant room to grow, and meet the needs of UCI's research community for another 
5-6 year cycle.  This procurement process began in January 2023 and is still ongoing. 

RCIC does not want to turn away groups who want CRSP storage.  *CRSP ANNEX* allows us to bridge the gap 
between now and when CRSP-2 is online and in production.

The CRSP ANNEX is a :bluelight:`temporary storage solution the provides similar functionality to CRSP`, but is incapable or
replicating all of CRSP's features or availability.

 .. note:: RCIC will provide storage on CRSP ANNEX *only to groups who will commit to moving the data from
           the Annex to CRSP-2.*  The rate for CRSP-2 storage will be set once the procurement has been completed. 
           The Annex will be shut down once CRSP-2 is in production.

:red:`The important differences between CRSP and CRSP ANNEX:`

  * **CRSP ANNEX does not have snapshots**,  but RCIC maintains regular backups.
    Performance in CRSP ANNEX might vary from current CRSP.

  * **Files can only be accessed via the SFTP protocol or directly from HPC3**.
    There is *NO web interface* for this system. SFTP (e.g. via the CRSP Desktop) is accessed through the :tt:`crsp-annex.crsp.uci.edu`

  * **Only a lab share directory is supported**.  Individual user directories within the lab file system
    are not created.

  * **CRSP ANNEX does not have the same, two site, redundancy of CRSP** and may have occasional (planned and unplanned) outages. 

  * **This is a temporary system.** Data will be moved from CRSP ANNEX to CRSP once the new hardware is procured and 
    installed (we expect that this will be completed bo later than July 1, 2024).

Default Annex Setup
^^^^^^^^^^^^^^^^^^^

For each LAB area, the :tt:`PI` is the owner of the space.

   * :tt:`pi_lab_share`: All members of the lab including the lab owner.
   * Membership in :tt:`pi_lab_share` is identical between CRSP and CRSP ANNEX. There are no exceptions.

Accessing  CRSP ANNEX
---------------------

You must either be on the campus network or connected to the
`UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ to access CRSP.

SFTP (e.g. via the CRSP Desktop) is accessed through the :tt:`crsp-annex.crsp.uci.edu`, not through 
:tt:`access.crsp.uci.edu`. If you are familiar with accessing CRSP, then you can make the following replacements in your
access configuration:

* :tt:`access.crsp.uci.edu` --> :tt:`crsp-annex.crsp.uci.edu`
* :tt:`/mmfs1/crsp/lab/<pi>` --> :tt:`/dfs3b/crsp/lab/<pi>`
* :tt:`/share/crsp/lab/<pi>` --> :tt:`/dfs3b/crsp/lab/<pi>`

You can access  your granted CRSP storage from Windows, MAC, and Linux systems
via a few methods. The client links in the table below provide installation
instructions:

.. table::
   :widths: 35 65
   :class: noscroll-table

   +------------------------------+-------------------------------------------------------------------------------------------+
   |  Client                      | Description                                                                               |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client desktop windows`| *CRSP Desktop* clients are for accessing CRSP ANNEXfrom Windows and MacOS laptops.        |
   |                              | We provide licensed and branded version of a commercial software *Mountain Duck*.         |
   | :ref:`client desktop mac`    |                                                                                           |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client sshfs`          | *SSHFS* can be used for accessing CRSP ANNEX shares from a Linux laptop/desktop.          |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client from hpc3`      | *DFS mount* on HPC3 provides and access to the CRSP's LAB and HOME areas.                 |
   +------------------------------+-------------------------------------------------------------------------------------------+

.. attention::

   Although CRSP ANNEX could be accessed via other commercial or open source
   desktop clients such as FileZilla, WinSCP, CyberDuck, the  **CRSP Desktop** client is the currently
   supported SFTP based software. Other desktop clients support is provided only on a best effort basis.

Deleted Files Recovery
----------------------

A common mistake is an accidental file deletion. In many cases, but not all,
users can retrieve a previous copy of the file.

  .. note:: On CRSP ANNEX, you must submit a support ticket to hpc-support@uci.edu to request restoration of files or folders. 
