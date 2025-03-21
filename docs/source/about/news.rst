
.. _news:

News & Events
=============

* General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
* Any additional information is outlined in notification emails to hpc-users@uci.edu
  (all current users) and is described in the details below.
* When the maintenance is completed all users are notified via emails to hpc-users@uci.edu.

Mar 25
------

| :blogtitle:`HPC3 Downtime March 25, 2025`
| :blogauthor:`2025-03-20 by Nadya Williams`

| The next outage will March 25, 2025, beginning at 8am.
| The cluster will be unavailable for most of the day.

Maintenance Items:
  * We will be retiring the :tt:`/dfs4` and :tt:`/dfs5`
    filesystems and migrating data to the new :tt:`/dfs10` system, specifically:

    ================== =================
       DFS4                DFS5
    ================== =================
    /dfs4/bsg          /dfs5/bio
    /dfs4/rao_col      /dfs5/weil21-lab
    /dfs4/som          /dfs5/weil21-lab2
    /dfs4/tvanerp_col  /dfs5/weil21-lab-uci-share
    /dfs4/weil21-lab1
    ================== =================

  * Daily syncs are currently running; a final sync will be run once the systems are quiet.
  * Most user directories on affected filesystems update quickly; however, a few accounts are taking 2-3 days to pick-up daily changes.
    We'll reach out to those users individually to warn them that their files will not be accessible for a few days.

Impacts:
  This is a full outage.

  #. All existing logins will be terminated.
  #. You will NOT have access to HPC3 during the planned downtime.
  #. You will have access to CRSP using `Web based File browser` or `CRSP Desktop App`.
  #. No jobs can run during the maintenance period.
  #. Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on March 25 will be held.
     Please see :ref:`requesting time limits <request time>` on queues.

After the maintenance:
  .. important:: After the change, users of the affected filesystems
	             will need to update any file references to use the :tt:`/dfs10` prefix.
