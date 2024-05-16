.. _CRSP2 Administration:

Purpose
=======

The purpose of this guide is to provide a written set of processes and procedures for managing the CRSP2 System.
The major areas need to be covered are:

I. :ref:`User and Lab Storage <User and Lab Storage>`

   * Storage Area Creation
   * User Account Management
   * Group ID management (relationship to HPC3)
   * Quota management 
   * Snapshots and Offsite Backup

II. System Configuration via Ansible and Salt

   * DUO-based authentication
   * Key-based authentication
   * Quota Reporting
   * NFS Exports
   * SFTP configuration
   * Web interface for file access
   * HA-Proxy Configuration
   * PF-Sense NAT Firewall Configuration
   * Networking Configuration

III. Operational Procedures for 

   * Submitting Tickets to Kalray for Supportable Items
   * Controlled upgrade of software/firmware without total system outage
   * Checking and fixing CTDB/NFS Server Issues
   * Controlled Shutdown of CRSP2
   * Reboot in case of disaster 

.. Templates should provide the following items
   * Name of procedure labeled with "_pname <name of procedure>"
   * Date of Revision
   * Overview in sentence or two labeled with _poverview <name of procedure>
   * Details labeled with _pdetails <name of procedure>
   * Repository of code (if applicable)


.. _User and Lab Storage:

I. User and Lab Storage
=======================

.. _pname Create Lab:

Create  Lab
-----------

* Created by:  ppapadop@uci.edu
* Repository:  https://github.oit.uci.edu/RCIC-UCI/crsp-admin
* Script:  :tt:`create-lab.sh`

Overview
^^^^^^^^

The script :tt:`create-lab.sh` will create a lab area owned by a particular UCINetID. It creates the lab with
default quota (1TB) and  files (400000).  Should these need to be adjust, follow the procedure for setting lab quotas.
If needed it will create the :tt:`<ucinetid>_lab` and :tt:`<ucinetid>_lab_share` unix groups (warns if they already 
exist). If the fileset (:tt:`<ucinetid>_lab`) exists, the script will exit in error. 

.. _pdetails Create Lab:

Example Usage
^^^^^^^^^^^^^


.. parsed-literal::

   :bluelight:`create-lab.sh basolo`

    Found UCInetID [ basolo ] [ 75237 ] (Mary Victoria Basolo) in UCI LDAP DataBase.

    > Running Verification checks.

    > Account & Groups Created.
    Fileset basolo_lab created with id 439 root inode 4194307.
    Fileset basolo_lab linked at /mmfs1/crsp/lab/basolo
    > Top 'Buckets' for [ basolo ] created.
    > All Done.

If the lab and lab_share groups already exist, an additional warning will be emitted as in the following example

.. parsed-literal::

   :bluelight:`create-lab.sh basolo`

   Found UCInetID [ basolo ] [ 75237 ] (Mary Victoria Basolo) in UCI LDAP DataBase.

   > Running Verification checks.

    ***************************************************************************
    *** << WARNING >>
    *** Group ID ( basolo_lab ) already exists in /etc/group
    *** basolo_lab:x:158897:basolo
    ***
    ***************************************************************************
    
    ***************************************************************************
    *** << WARNING >>
    *** Group ID ( basolo_lab_share ) already exists in /etc/group
    *** basolo_lab_share:x:158898:basolo
    ***
    ***************************************************************************
    > Account & Groups Created.
    Fileset basolo_lab created with id 439 root inode 4194307.
    Fileset basolo_lab linked at /mmfs1/crsp/lab/basolo
    > Top 'Buckets' for [ basolo ] created.
    > All Done.

.. _pname Find Active Labs:

Find Active Labs
----------------

* Created by:  ppapadop@uci.edu
* Repository:  https://github.oit.uci.edu/RCIC-UCI/crsp-admin
* Script: :tt:`util/find-labs-in-use.sh`

Overview
^^^^^^^^

The script :tt:`util/find-labs-in-use.sh` will create a CSV output that lists each fileset in the :tt:`mmfs1` 
filesystem that has a non-zero number of files.  It uses :tt:`mmrepquota` to select fileset name, number of files, 
files quota, storage used, and storage quota.  Output can be used for other processing steps


.. _pdetails Find Active Labs:

Example Usage
^^^^^^^^^^^^^


.. parsed-literal::

   :bluelight:`util/find-labs-in-use.sh`
   fileset,used,quota,files,filequota
   shasun_lab,1273,2048,2080,100000
   baolinw1_lab,49,2048,216,350000
   mednicks_lab,16249,24576,36844,350000
   shupengz_lab,604,2048,100000,100000
   shz_lab,715,2048,100000,100000
   jabarret_lab,1,2048,19,100000
   yhliang_lab,1615,2048,92764,350000
   pilau_lab,1,2048,7,100000
   cmhoo_lab,257,2048,2499,350000
   baldwij1_lab,1887,2048,703,350000
   jlipkova_lab,408,2048,6646,350000
   kyokomor_lab,24347,30720,869376,8750000
   dalawson_lab,86917,98304,5981475,18000000
   fmamdani_lab,1,2048,16,350000
 
