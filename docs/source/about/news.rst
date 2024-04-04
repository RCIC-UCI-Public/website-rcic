
.. _news:

News & Events
=============

General information about the :ref:`maintenance`  is applicable to all
scheduled downtimes. Any additional information is outlined in
notification emails (sent to all users)  and in the events below.

Mar 27
------

| :blogtitle:`HPC3 Downtime Mar 27, 2024`
| :blogauthor:`2024-03-20 by Philip Papadopoulos`

| :red:`The next outage will be March 27, 2024, beginning at 8am`

RCIC will be performing our regular, between quarters, maintenance next Wednesday, Mar 27.
All users will be logged out, pending jobs will remain queued.

Maintenance Items:
  1. New disk arrays for dfs3b to be installed.
     RCIC taking care of data wrangling to make this as transparent as possible
  2. Reboot all Systems
  3. Internal Slurm Configuration updates

Impacts:
  - All existing logins will be terminated.
  - HPC3 and its file systems will be unavailable. You will not be able to login or access files in /dfsX or /home.
  - No jobs can run during the maintenance period.
  - Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on Wednesday will be held.
    Please see :ref:`requesting time limits <request time>` on queues.

We expect to return HPC3 to service late afternoon, late afternoon Mar 27.

