
.. _news:

News & Events
=============

* General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
* Any additional information is outlined in notification emails to hpc-users@uci.edu
  (all current users) and is described in the details below.
* When the maintenance is completed all users are notified via emails to hpc-users@uci.edu.

December 17, 2025
-----------------

| :blogtitle:`HPC3 Downtime December 17, 2025`
| :blogauthor:`2025-11-18 by Nadya Williams`

| The next outage will be December 17, 2025, beginning at 8am.
| The cluster will be unavailable all day.

Maintenance Items:
  1. Apply latest Rocky 9.6 OS updates on all nodes.
  #. Beegfs Upgrade to 8.2 on all DFS servers and cluster-wide
  #. Update NAS Servers to Rocky 9.6
  #. Update Remaining bioportal to 9.6

Impacts:
  :red:`This is a full outage`.

  #. All existing logins will be terminated.
  #. You will NOT have access to HPC3 during the planned downtime.
  #. You will have access to CRSP using `Web based File browser` or `CRSP Desktop App`.
  #. No Slurm jobs can run.

User Action required:
  .. attention:: Slurm jobs submitted to close to the maintenance window can result in 
     :tt:`Pending job due to ReqNodeNotAvail, Reserved for maintenance` state. 
     This means jobs that are not guaranteed (via TimeLimit) to complete before 8am on
     the day of maintenance. These jobs will need to be canceled and resubmitted after the maintenance.
     Please see :ref:`requesting time limits <request time>` on queues.

  1. Save your work:

     - cancel all Slurm jobs
     - stop any containers running via Jupyterhub portal
     - stop Any VSCode instances
  #. Logout
