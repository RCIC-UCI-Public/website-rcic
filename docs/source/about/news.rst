
.. _news:

News & Events
=============

| General information about the :ref:`maintenance` is applicable to all scheduled downtime periods.
| Specific information regarding the maintenance is described in the details below.

| All current users are notified via the mailing list hpc-users@uci.edu about:
|   Any specific maintenance scheduling
|   When the maintenance is completed 

June 16, 2026
-----------------

| :blogtitle:`HPC3 Downtime June 16, 2026`
| :blogauthor:`2026-06-01 by Nick Santucci`

| The next outage/planned downtime will be June 16, 2026, beginning at 8 am.
| The cluster will be unavailable all day.

Maintenance Items:
  1. Apply latest Rocky 9.7 OS updates on user facing cluster resources (compute, GPU, login, JupyterHub portal servers)
  #. Some of the Dell top-of-rack switches will be updated from OS9 to OS10
  #. Update all dfsX shared keys stored in HashiCorp Vault
  #. Update the munge keys (used to create/validate access between hosts running slurm) stored in HashiCorp Vault

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

March 24, 2026
-----------------

| :blogtitle:`HPC3 Downtime March 24, 2026`
| :blogauthor:`2026-02-26 by Nadya Williams`

| The next outage will be March 24, 2026, beginning at 8am.
| The cluster will be unavailable all day.

Maintenance Items:
  1. Replace core Ethernet switching infrastructure for HPC3
     (Arista switches purchased in 2019) with two Sonic-based switches
  #. Beegfs Upgrade to 8.3.0 on all DFS servers and cluster-wide
  #. Apply latest Rocky 9.7 OS updates on all cluster nodes.
  #. Update NAS Servers to Rocky 9.7
  #. Update Applications stack to Rocky 9.7

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
