
.. _news:

News & Events
=============

| General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
| Any additional information is outlined in notification emails (sent to all users) and in the events below.

| :blogtitle:`HPC3 Downtime December 18, 2024`

| :red:`The next outage will be before Christmas break, December, 2024, beginning at 8am`

Maintenance Items:
  1. OS revision update from **Rocky 8.8 to Rocky 8.10**.
  #. Full rebuild of all software, see below for software changes.
  #. Top-to-bottom re-installation of all compute and login nodes.

Impacts:
  This is a full outage

  1. All existing logins will be terminated.
  #. You will NOT have access to HPC3 or CRSP during the planned downtime.
  #. No jobs can run during the maintenance period.
  #. Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on December 18 will be held.
     Please see :ref:`requesting time limits <request time>` on queues.

Software changes:
  | Some modules will be removed because they cannot be built on a new system or are unused. 
  | Note, the table below will be periodically updated till the maintenance date.

  .. table:: **Software module changes**
     :align: center
     :class: noscroll-table

     +------------------------------+---------------------------------------+
     | Scheduled to be removed      | Use instead                           |
     +==============================+=======================================+
     | pytorch/1.5.1                | use newer version                     |
     +------------------------------+---------------------------------------+
     | miniconda3/4.8.5             | miniconda3/23.5.2                     |
     +------------------------------+---------------------------------------+
     | miniconda3/4.12.0            | miniconda3/23.5.2                     |
     +------------------------------+---------------------------------------+
