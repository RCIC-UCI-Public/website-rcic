
.. _storage hpc3:

Storage Systems
===============

RCIC supports several different storage systems, each with their own *sweet spot* for 
price and performance. 

All storage systems depicted below are available from the HPC3 cluster.  
:ref:`Campus Storage (CRSP) <crsp>` is unique  in that it can also be accessed from
desktops and laptops without going through HPC3.

Connectivity, file System architecture, 
and physical hardware all contribute to the performance of HPC3 storage systems:

.. figure:: images/storage.png
   :align: center
   :width: 100%
   :alt: hpc3 storage

   HPC3 Storage pictogram

.. attention:: | Storage is shared among all users.  The nature of networked-storage
			   | :underline:`makes it possible for a single user to render a file system unusable for all`.

The following summary explains what each storage system provides,
what it should be used for, and shows links for in-depth how to use guides:

.. table:: Storage Summary
   :class: noscroll-table
   :widths: 11,23,23,43
   :align: center

   +-----------------------------------+-------------------------+------------------------------+----------------------------------------------------------------+
   |   **Name**                        | **Access**              | **Performance**              | **How to use**                                                 |
   +===================================+=========================+==============================+================================================================+
   | :ref:`HOME <home>`                | On all                  | Slowest, yet is sufficient   | Store small files, compiled binaries, order of Mbs data files. |
   |                                   | nodes via NFS mount     | when used properly           |                                                                |
   |                                   |                         |                              | :red:`Not for data intensive batch jobs`                       |
   +-----------------------------------+-------------------------+------------------------------+----------------------------------------------------------------+
   | :ref:`Scratch <scratch storage>`  | Local disk space unique | Fastest performance, data    | As scratch storage ($TMPDIR) for batch jobs that repeatedly    |
   |                                   | to each compute node    | is removed when job completes| access many small files or make frequent small reads/writes.   |
   +-----------------------------------+-------------------------+------------------------------+----------------------------------------------------------------+
   | :ref:`DFS <dfs>`                  | On all nodes            | Best for processing medium/  | To keep source code, binaries. For data used in batch jobs.    |
   |                                   | via mount over BeegFS   | large data files (order of   |                                                                |
   |                                   |                         | 100's Mbs/Gbs)               | :red:`Not for writing/reading many small files`.               |
   +-----------------------------------+-------------------------+------------------------------+----------------------------------------------------------------+
   | :ref:`CRSP <crsp>`                | On all nodes            | Best for processing medium/  | To keep source code, binaries. Sometimes for data used in      |
   | (campus storage)                  | via mount over NFS      | large data files (order of   | batch jobs, usually better use DFS or Scratch.                 |
   |                                   |                         | 100's Mbs/Gbs)               |                                                                |
   |                                   |                         |                              | :red:`Not for writing/reading many small files`.               |
   +-----------------------------------+-------------------------+------------------------------+----------------------------------------------------------------+
   | :ref:`CRSP ANNEX <crsp annex>`    | On all nodes            | Best for processing medium/  | To keep source code, binaries. For data used in batch jobs.    |
   |                                   | via mount over BeegFS   | large data files (order of   | Availalbe to a handful of labs as a temporary storage.         |
   |                                   |                         | 100's Mbs/Gbs)               |                                                                |
   |                                   |                         |                              | :red:`Not for writing/reading many small files`.               |
   +-----------------------------------+-------------------------+------------------------------+----------------------------------------------------------------+

.. _crsp dfs comparison:

CRSP vs. DFS
^^^^^^^^^^^^

This section compares two available largest capacity storage systems :ref:`CRSP <crsp>` and :ref:`DFS <dfs>`.
Both are parallel filesystems but have different cost, availability, and usage models.
The table below highlights the key differences and similarities between these two systems
and can help you choose the right system (or combination of systems) to store your data.


.. table:: **Compare DFS and CRSP**
   :align: center
   :class: noscroll-table

   +--------------+------------------------------------------+---------------------------------------------+
   | **Feature**  | **CRSP**                                 | **DFS**                                     |
   +==============+==========================================+=============================================+
   | Cost         | $50/TB/Year                              |  $100/TB/5Years                             |
   +--------------+------------------------------------------+---------------------------------------------+
   | Availability | Highly-available. No routinely planned   |  Routine maintenance outage about 4X/year.  |
   |              | outages. Can survive many types of       |  Survives disk failures (RAID) only         |
   |              | hardware failures without downtime       |                                             |
   +--------------+------------------------------------------+---------------------------------------------+
   | Access       | Access from **any campus IP** or         |  Access **only** from HPC3                  |
   |              | VPN-connected laptop                     |                                             |
   +--------------+------------------------------------------+---------------------------------------------+
   | Snapshots    | Daily file system snapshots allow users  |  No Snapshots                               |
   |              | to self-recover from deletions or        |                                             |
   |              | overwrites of files                      |                                             |
   +--------------+------------------------------------------+---------------------------------------------+
   | Backups      | Backed up daily offsite with **90 day retention**                                      |
   |              | of deleted/changed files                                                               |
   +--------------+------------------------------------------+---------------------------------------------+
   | Quota        | Labs have a space and file number quotas.| All users *share the same group quota*. All |
   | Management   | Users and groups can have sub-quotas     | files must be written with the same unix    |
   |              | set within the lab                       | group id to access quota space              |
   +--------------+------------------------------------------+---------------------------------------------+
   | Performance  | High-performance but DFS is a better     | High-performance. Most common storage for   |
   |              | match for direct use from HPC3           | used on HPC3                                |
   +--------------+------------------------------------------+---------------------------------------------+
   | Encryption   |  All data is encrypted at rest.          | Only **dfs3b** is encrypted at rest.        |
   | at rest      |                                          |                                             |
   +--------------+------------------------------------------+---------------------------------------------+
   | File System  | IBM Storage Scale (aka GPFS)             | BeeGFS with Thinkparq support.              |
   |              |                                          | `Details  <https://www.beegfs.io/c/>`_      |
   +--------------+------------------------------------------+---------------------------------------------+
