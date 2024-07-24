
.. _storage hpc3:

Storage Systems
===============

RCIC supports several different storage systems, each with their own "sweet spot" for 
price and performance. 

The storage systems depicted below are all available from the HPC3 cluster.  
:ref:`Campus Storage (CRSP) <crsp>` is unique in that it can also be accessed from desktops, laptops, 
and other systems without going through HPC3.

The two major *parallel* file systems are DFS and CRSP and the section on :ref:`comparing CRSP and DFS <crsp dfs comparison>` can help
you choose the right system (or combination of systems) to store your data.

Of the multiple HPC3 storage systems available, connectivity, file System architecture, 
and physical hardware all contribute to performance.

.. figure:: images/storage.png
   :align: center
   :width: 100%
   :alt: hpc3 storage

   HPC3 Storage pictogram

.. attention:: | Storage is shared among all users. 
               | The nature of networked-storage makes is possible for
               | a single user to render a file system unusable for all.

The following summary explains what each storage system provides,
what it should be used for, and shows links for in-depth how to use guides.

:bluelight:`Home`
  | **See details in** :ref:`HOME storage guide <home>`.
  | Provides a convenience access on all nodes via mount over NFS
  | Slowest performance, yet is sufficient when used properly
  | Use to keep small source code or compiled binaries
  | Use for small (order of Mbs) data files
  | :red:`Do not use for data intensive batch jobs`

:bluelight:`Scratch`
  | **See details in** :ref:`Scratch storage guide <scratch storage>`.
  | Local disk space unique to each compute node 
  | Fastest performance, data is removed when job completes
  | Use as scratch storage for batch Jobs that repeatedly access many small files or make frequent small reads/writes:
  | :red:`Not available on login nodes`

:bluelight:`Parallel`
  | **See details in** :ref:`DFS storage guide <dfs>`.
  | Provides a convenience access on all nodes via mount
  | Performance is best for processing medium/large data files (order of 100s Mbs/Gbs)
  | Use for batch jobs, most common place for data used in batch jobs
  | Use to keep source code, binaries
  | :red:`Do not use for writing/reading many small files`

:bluelight:`Campus Storage`
  | **See details in** :ref:`CRSP storage guide <crsp>`.
  | Provides a convenience access on all nodes via mount over NFS
  | Performance is best for processing medium/large data files (order of 100s Mbs/Gbs)
  | Use sometimes for batch Jobs, usually better to use DFS or local $TMPDIR storage
  | Use to keep source code, binaries
  | :red:`Do not use for writing/reading many small files`

:bluelight:`Campus Storage Annex`
  | **See details in** :ref:`CRSP ANNEX storage guide <crsp annex>`.
  | Provides a convenience access on all nodes via mount over BeeGFS 
  | Performance is best for processing medium/large data files (order of 100s Mbs/Gbs)
  | :red:`Do not use for writing/reading many small files`

.. _crsp dfs comparison:


CRSP vs. DFS
^^^^^^^^^^^^

The largest capacity storage systems available are :ref:`CRSP <crsp>` and :ref:`DFS <dfs>`. Both are parallel filesystems but have different
cost, availability, and usage models.   The table below highlights the key differences and similarities between
these two systems. 


.. table:: **Compare DFS and CRSP**
   :align: center
   :class: noscroll-table

   +---------------------------+-----------------------------------------+---------------------------------------------+
   |   **Feature**             | **CRSP**                                | **DFS**                                     |
   +===========================+=========================================+=============================================+
   |   :bluelight:`Cost`       | $50/TB/Year                             |  $100/TB/5Years                             |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`Availability` | Highly-available. No routinely planned  |  Routine maintenance outage about 4X/year.  |
   |                           | outages. Can survive many types of      |  Survives disk failures (RAID) only         |
   |                           | hardware failures without downtime      |                                             |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`Access`       | Access from **any campus IP** or        |  Access **only** from HPC3                  |
   |                           | VPN-connected laptop                    |                                             |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`Snapshots`    | Daily file system snapshots allow users |  No Snapshots                               |
   |                           | to self-recover from deletions or       |                                             |
   |                           | overwrites of files                     |                                             |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`Backups`      | Backed up daily offsite with **90 day retention**                                     |
   |                           | of deleted/changed files                                                              |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`Quota`        | Labs have a space/#files quota. Users   | All users *share the same group quota*. All |
   | :bluelight:`Management`   | and groups can have (sub)quotas set     | files must be written with the same unix    |
   |                           | within the lab                          | group id to access quota'ed space           |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`Performance`  | High-performance but DFS is a better    | High-performance. Most common storage for   |
   |                           | match for direct use from HPC3          | used on HPC3                                |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`Encryption`   |  All data is encrypted at rest.         | Only **dfs3b** is encrypted at rest.        |
   | :bluelight:`at rest`      |                                         |                                             |
   +---------------------------+-----------------------------------------+---------------------------------------------+
   | :bluelight:`File System`  | IBM Storage Scale (aka GPFS)            | BeeGFS with Thinkparq support.              |
   |                           |                                         | `Details  <https://www.beegfs.io/c/>`_      |
   +---------------------------+-----------------------------------------+---------------------------------------------+
