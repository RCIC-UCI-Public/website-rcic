
.. _news:

News & Events
=============

General information about the :ref:`maintenance`  is applicable to all
scheduled downtimes. Any additional information is outlined in
notification emails (sent to all users)  and in the events below.

Jul 8
------

| :blogtitle:`HPC3 Downtime Jul 16, 2024`
| :blogauthor:`2024-07-05 by Nadya Williams`

:red:`The next outage will be July 16, 2024, beginning at 8am`

| This is the first of two summer maintenance periods.
| There are two major items that we will be attending to during the downtime

Maintenance Items:
  1. Update of BeeGFS (File systems for all DFS servers) to address a segmentation fault  in the BeeGFS metadata daemon
     that results in a down file system. This has occurred about 3 times in the past 4 months.
  2. Hardware replacement of CRSP, see
     `CRSP to CRSP2 transition <https://rcic.uci.edu/storage/crsp.html#crsp-to-crsp2-transition>`_.
     CRSP hardware has reached end of life and new hardware has been delivered.

Impacts:
  1. :red:`This is a full outage.
     You will NOT have access to HPC3 or CRSP during the planned downtime`.
  2. The 8-10 hour outage of CRSP is the first time that there has been a planned full outage of CRSP.
     The last unplanned outage of CRSP was more than two years ago and lasted about 8 hours.

Data copy:
  - Users don't need to make any copies.
  - All data has been copied from the current CRSP to the new system *CRSP2*.
  - Daily changes are incrementally copied.
  - On the cut over day, the final incremental copy will happen.

