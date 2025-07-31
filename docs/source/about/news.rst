
.. _news:

News & Events
=============

* General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
* Any additional information is outlined in notification emails to hpc-users@uci.edu
  (all current users) and is described in the details below.
* When the maintenance is completed all users are notified via emails to hpc-users@uci.edu.


July 29, 2025
-------------

| :blogtitle:`HPC3 Downtime July 29, 2025`
| :blogauthor:`2025-05-13 by Nadya Williams`

| The next outage will be July 29, 2025, beginning at 8am.
| The cluster will be unavailable all day.

Maintenance Items:
  1. OS version update from **Rocky 8.10 to Rocky 9**.
  #. Top-to-bottom re-installation of all compute and login nodes.
  #. Full rebuild of all applications software, see software changes below.
  #. Full rebuild of Slurm software.

Impacts:
  This is a full outage.

  #. All existing logins will be terminated.
  #. You will NOT have access to HPC3 during the planned downtime.
  #. You will have access to CRSP using `Web based File browser` or `CRSP Desktop App`.
  #. No Slurm jobs can run or can be pending in the queue.
  #. :red:`All jobs remaining in the queue on the maintenance day will be terminated`.
  #. Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on the day of maintenance
     will need to be canceled and resubmitted after the maintenance.
     Please see :ref:`requesting time limits <request time>` on queues.

Software changes:
  The operating system update involves many changes across the software stack.
  While we try to build all the previous software versions for the new OS, some builds are
  impossible. As a result, some modules will be removed because they cannot be built on a new system or because
  the underlying requirements are no longer satisfied.

  After the maintenance:

    * :red:`User compiled and installed software will need to be recompiled and reinstalled`.
    * User installed conda environments will VERY LIKELY need to be reinstalled.
    * If you previously used a module that has been removed, you will need to use a newer version of it where available.

.. important:: Please see :ref:`Rocky 9.6 software updates <rocky 9.6 updates>` for details on system and user installed software.
