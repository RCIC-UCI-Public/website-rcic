
.. _news:

News
=====

We periodically need to perform maintenance on HPC3 where all users are logged out and all jobs are stopped.

The next outage will be March 28, 2023, beginning at 8am.

The major items on the list are the following

- Upgrade All DFS servers to Rocky Linux 8.7
- Upgrade Home Area Server to Rocky Linux 8.7
- Reset BIOS on the dfs-3a-1 server
- Replace Failed Drive on dfs-2
- Replace dfs-7-1 with its now-repaired original server

We will be touching a majority of storage servers during the downtime, but will not upgrade the version of BeeGFS.

Why are we doing this now? CentOS 7 (which is still present on several file servers) hits end-of-life in June 2024
and needs to be phased out everywhere. BeeGFS has declared that now-and-future versions of BeeGFS will not support CentOS 7.
We plan to upgrade the version of BeeGFS, cluster-wide, during a summer downtime.

