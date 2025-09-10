
.. _news:

News & Events
=============

* General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
* Any additional information is outlined in notification emails to hpc-users@uci.edu
  (all current users) and is described in the details below.
* When the maintenance is completed all users are notified via emails to hpc-users@uci.edu.

September 18, 2025
------------------

| :blogtitle:`HPC3 Downtime September 18, 2025`
| :blogauthor:`2025-09-10 by Nadya Williams`

| The next outage will be September 18, 2025, beginning at 8am.
| The cluster will be unavailable all day.

Maintenance Items:
  1. BeegFS version upgrade on all DFS servers and cluster-wide.
  #. Slurm version upgrade cluster-wide.

Impacts:
  :red:`This is a full outage`.

  #. All existing logins will be terminated.
  #. You will NOT have access to HPC3 during the planned downtime.
  #. You will have access to CRSP using `Web based File browser` or `CRSP Desktop App`.
  #. No Slurm jobs can run or can be pending in the queue.
     All jobs remaining in the queue on the maintenance day will be terminated.
  #. Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on the day of maintenance
     will need to be canceled and resubmitted after the maintenance.
     Please see :ref:`requesting time limits <request time>` on queues.
