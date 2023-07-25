
.. _news:

News & Events
=============

General information about the :ref:`maintenance`  is applicable to all
scheduled downtimes. Any additional information is outlined in
notification emails (sent to all users)  and in the events below.

Jul 25
------

:blogtitle:`HPC3 Downtime Jul 25, 2023`

:blogauthor:`2023-03-12 by Philip Papadopoulos`


:red:`The next outage will be July 25, 2023, beginning at 8am`

.. note:: This is the first of two outages planned for this summer.

In this outage we will be doing the following:
  1. Reinstalling all login/compute nodes with Rocky Linux 8.8 and
     applications recompiled for Rocky Linux 8.8.
  2. Updating management/storage nodes to Rocky Linux 8.8.
  3. Updating Slurm to its most recent release.

**Effects on Jobs**
  - Prior to the maintenance, :underline:`jobs that are not guaranteed to finish
    before 8am on July 25, will be held`. All queues have default time limits
    (see the RCIC website). You can also change the time limits for your jobs
    to tell Slurm that your jobs will finish prior to 8am.
  - Queued jobs - We will endeavor to keep queued jobs during the Slurm
    upgrade. However, it is possible that any held jobs may need to be
    resubmitted after HPC3 is returned to service.

**Effects on user-compiled code**
  - In general, user-compiled code will NOT need to be recompiled.
  - However, there are some differences among Rocky 8.6 (installed last summer), Rocky
    8.7 (updated early 2023) and Rocky 8.8. You might need to rebuild your application(s).

Mar 28
------

:blogtitle:`HPC3 Downtime Mar 28, 2023`

:blogauthor:`2023-03-17 by Philip Papadopoulos`

We periodically need to perform maintenance on HPC3 where all users are logged out and all jobs are stopped.

:red:`The next outage will be March 28, 2023, beginning at 8am`

The major items on the list are the following:
  1. Upgrade All DFS servers to Rocky Linux 8.7
  2. Upgrade Home Area Server to Rocky Linux 8.7
  3. Reset BIOS on the dfs-3a-1 server
  4. Replace Failed Drive on dfs-2
  5. Replace dfs-7-1 with its now-repaired original server

  We will be touching a majority of storage servers during the downtime,
  but will not upgrade the version of BeeGFS.

**Why are we doing this now?**
  CentOS 7 (which is still present on several file servers) hits end-of-life in June 2024
  and needs to be phased out everywhere. BeeGFS has declared that now-and-future versions of BeeGFS will not support CentOS 7.

**We plan to upgrade the version of BeeGFS, cluster-wide, during a summer downtime.**

