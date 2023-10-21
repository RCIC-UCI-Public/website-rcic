
.. _storage hpc3:

How to use
==========

HPC3 has several storage systems available.  Connectivity, File System architecture, 
and physical hardware all contribute to performance.

.. centered::  :bluelight:`HPC3 Storage pictogram`

.. image:: images/storage.png
   :align: center
   :width: 100%
   :alt: hpc3 storage

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
  | **See details in** :ref:`CRSP ANNEX storage guide <crsp-annex>`.
  | Provides a convenience access on all nodes via mount over BeeGFS 
  | Performance is best for processing medium/large data files (order of 100s Mbs/Gbs)
  | :red:`Do not use for writing/reading many small files`
