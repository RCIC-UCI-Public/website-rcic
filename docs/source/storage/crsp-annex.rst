.. _crsp annex:

CRSP ANNEX
==========

.. contents::
   :local:

Overview
--------

CRSP was procured in 2018 and deployed into production in 2019 and is  *at capacity* with no practical path to expand its local 
storage to accommodate new (large) storage requests.  RCIC has been in the process of procuring a replacement for CRSP (called 
CRSP-2) to double storage capacity, have  significant room to grow, and meet the needs of UCI's research community for another 
5-6 year cycle.  This procurement process began in January 2023 and is still ongoing. 

RCIC does not want to turn away groups who want CRSP storage.  *CRSP ANNEX* allows us to bridge the gap 
between now and when CRSP-2 is online and in production.

:bluelight:`The CRSP ANNEX is a temporary storage solution the provides similar functionality to CRSP`, but is incapable or
replicating all of CRSP's features or availability.

 .. note:: RCIC will provide storage on CRSP ANNEX *only to groups who will commit to moving the data from
           the CRSP ANNEX to CRSP-2.*  The rate for CRSP-2 storage will be set once the procurement has been completed. 
           **The CRSP ANNEX will be shut down once CRSP-2 is in production**.

:red:`The important differences between CRSP and CRSP ANNEX:`

  1. **This is a temporary system.** Data will be moved from CRSP ANNEX to CRSP-2 once the new hardware is procured and
     installed. We expect that this will be completed no later than July 1, 2024.

  2. **Files can only be accessed via the SFTP protocol or directly from HPC3**.

     * SFTP (via the CRSP Desktop) is accessed through the :tt:`crsp-annex.crsp.uci.edu`
     * From HPC3 access is :tt:`/dfs3b/crsp/lab/<pi>`
     * There is *NO web interface* for this system

  3. **CRSP ANNEX does not have snapshots**,  but RCIC maintains regular backups.
     Performance in CRSP ANNEX might vary from current CRSP.

  4. **CRSP ANNEX does not have the same, two site, redundancy of CRSP** and may have occasional (planned and unplanned) outages.

  5. **Only a lab share directory is supported**. Individual user directories within the lab file system
     are not created.

Default CRSP ANNEX Setup
^^^^^^^^^^^^^^^^^^^^^^^^

For each LAB area, the :tt:`PI` is the owner of the space.

   * Group :tt:`pi_lab_share`: all members of the lab including the lab owner.
   * Membership in group :tt:`pi_lab_share` is identical between CRSP and CRSP ANNEX. There are no exceptions.

Accessing  CRSP ANNEX
---------------------

You must either be on the campus network or connected to the
`UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ to access CRSP ANNEX.

SFTP (via the CRSP Desktop) is accessed through the :tt:`crsp-annex.crsp.uci.edu`.

If you are familiar with accessing CRSP, then you can make the following replacements in your
access configuration:

.. table:: **Replacements for CRSP-ANEX access configuration**
   :align: center
   :class: noscroll-table

   +-----------------------+----------------------------+
   | CRSP access           | CRSP ANNEX access          |
   +=======================+============================+
   | access.crsp.uci.edu   | crsp-annex.crsp.uci.edu    |
   +-----------------------+----------------------------+
   | /mmfs1/crsp/lab/<pi>  | /dfs3b/crsp/lab/<pi>       |
   +-----------------------+----------------------------+
   | /share/crsp/lab/<pi>  | /dfs3b/crsp/lab/<pi>       |
   +-----------------------+----------------------------+

CRSP ANNEX clients
------------------

You can access your granted CRSP ANNEX storage from Windows, MAC, and Linux systems
via a few methods. Most clients are the same as for accessing CRSP. The client links in the table below provide installation
instructions:

.. table::
   :widths: 35 65
   :class: noscroll-table

   +------------------------------+-------------------------------------------------------------------------------------------+
   |  Client                      | Description                                                                               |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client desktop windows`| *CRSP Desktop* clients are for accessing CRSP ANNEX from Windows and macOS laptops.       |
   |                              | We provide licensed and branded version of a commercial software *Mountain Duck*.         |
   | :ref:`client desktop mac`    |                                                                                           |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | :ref:`client sshfs`          | *SSHFS* can be used for accessing CRSP ANNEX shares from a Linux laptop/desktop.          |
   +------------------------------+-------------------------------------------------------------------------------------------+
   | Access from HPC3             | On HPC3, CRSP ANNEX shares are mounted in :tt:`/dfs3b/crsp/lab/<pi>`                      |
   +------------------------------+-------------------------------------------------------------------------------------------+

.. attention::

   Although CRSP ANNEX could be accessed via other commercial or open source
   desktop clients such as FileZilla, WinSCP, CyberDuck, the  **CRSP Desktop** client is the currently
   supported SFTP based software. Other desktop clients support is provided only on a best effort basis.

.. _configure crsp annex:

Configure CRSP Desktop
----------------------

.. important:: This section applies only to the
               users who have an access to :ref:`crsp annex`.

Configuring CRSP Desktop App to access data on :ref:`crsp annex` is very similar
to adding CRSP new shares.

Configure Step 1
  Create a new connection  per your platform
  :ref:`add share on macOS <mac add shares>` or :ref:`add share on Windows <windows add shares>`. 

Configure Step 2
  You will edit 5 fields in the default bookmark: connection type (from the menu) 
  :guilabel:`Nickname`, :guilabel:`Server`, :guilabel:`Username`, and :guilabel:`Path`.
  Here the image shows default bookmark editing on macOS (the image is almost identical on Windows):

  .. figure:: images/crsp/mac-crsp-annex-default.png
     :align: center
     :width: 60%
     :alt: CRSP Annex configuration default

     Default template

  .. attention:: 
            * :guilabel:`CRSP Lab` - change the connection type to :guilabel:`SFTP (SSH File Transfer Protocol)`
              via choosing it from the menu.
            * :guilabel:`Nickname` - we recommend that you change it to **CRSP Annex - <pi>**
            * :guilabel:`Server` - set as :tt:`crsp-annex.crsp.uci.edu`
            * :guilabel:`Username` - your UCINetID
            * :guilabel:`Path` - set the path as :tt:`/dfs3b/crsp/lab/<pi>`
            * The **URL** is created automatically from the information you type in other fields,
              you don't directly change it. This URL is for  using the SFTP protocol to access

Configure Step 3
   After the editing configured bookmark should look similar to the ones below (with your information).

   The following show this set up for a particular user (*ppapadop*) and a particular pi (*npw*):

   on MacOS
     Click :guilabel:`Connect` to connect to your CRSP Annex share:

     .. figure:: images/crsp/mac-crsp-annex.png
        :align: center
        :width: 60%
        :alt: macOS CRSP Annex configuration

        macOS: CRSP Annex configuration

   on Windows
     Click :guilabel:`OK` to connect to your CRSP Annex share:

     .. figure:: images/crsp/win-crsp-annex.png
        :align: center
        :width: 60%
        :alt: CRSP Annex configuration

        Windows: CRSP Annex configuration

Deleted Files Recovery
----------------------

A common mistake is an accidental file deletion. In many cases, but not all,
users can retrieve a previous copy of the file.

  .. note:: On CRSP ANNEX, you must submit a support ticket to hpc-support@uci.edu to request restoration of files or folders. 
