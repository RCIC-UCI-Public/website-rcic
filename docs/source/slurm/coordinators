.. _account coordinators:

Account coordinators
====================

:underline:`PIs have control over who can charge to their account and how much they can charge`

Slurm uses :tt:`account coordinators` as users who can directly
control accounts. We highly encourage PIs to assign
additional coordinators (typically postdocs or  grad students) to
manage their Slurm lab accounts access.

.. attention:: | The following common tasks can be run by account coordinators.
               | Please use them with caution.

.. _coord access control:

Access Control
--------------

1. To view your lab's Slurm account coordinators do:

   .. code-block:: console

      [user@login-x:~]$ sacctmgr show account panteater_lab withcoordinator
      [user@login-x:~]$ sacctmgr show account panteater_lab,panteater_lab_gpu withcoordinator format=Account%-25,Descr,Org,Coord

2. To add a user to your lab's Slurm account do:

   .. code-block:: console

      [user@login-x:~]$ sacctmgr add user panteater account=panteater_lab

3. To remove a user from your lab's Slurm charge account do:

   .. code-block:: console

      [user@login-x:~]$ sacctmgr remove user where user=panteater account=panteater_lab

.. _coord user limits:

Set User Limits
---------------

1. Check current limits by account or by user

   .. code-block:: console

      [user@login-x:~]$ sacctmgr list assoc account=panteater_lab
      [user@login-x:~]$ sacctmgr list assoc user=panteater

2. Limit user's CPU time on running jobs

   .. code-block:: console

      [user@login-x:~]$ sacctmgr modify user panteater set GrpCPURunMins=10000

3. Limit a specific user to have no more than 20 jobs in the system:

   .. code-block:: console

      [user@login-x:~]$ sacctmgr modify user where \
                                 name=panteater  account=panteater_lab set maxjobs=20

4. Set number of cores per user to 40 CPUs at a time:

   .. code-block:: console

      [user@login-x:~]$ sacctmgr modify user panteater set GrpCPUs=40

.. _coord clear limits:

Clear User limits
-----------------

To clear a previously set limit, reset its value to :tt:`-1`.

1. Remove user's job limit

   .. code-block:: console

      [user@login-x:~]$ sacctmgr -i modify user where name=panteater set MaxJobs=-1

.. _coord manage jobs:

Manage User Jobs
----------------

1. List jobs by account or by user

   .. code-block:: console

      [user@login-x:~]$ squeue -A panteater_lab
      [user@login-x:~]$ squeue -u panteater

2. Cancel jobs by job id:

   .. code-block:: console

      [user@login-x:~]$ scancel 1234567

3. Cancel all jobs for a specific user:

   .. code-block:: console

      [user@login-x:~]$ scancel -u panteater

3. Cancel all running jobs for a specific user:

   .. code-block:: console

      [user@login-x:~]$ scancel -u panteater --state=running

4. Cancel all pending jobs for a specific user:

   .. code-block:: console

      [user@login-x:~]$ scancel -u panteater --state=pending

5. Cancel all jobs in the account:

   .. code-block:: console

      [user@login-x:~]$ scancel -A panteater_lab

6. Hold jobs by jobid:

   .. code-block:: console

      [user@login-x:~]$ scontrol hold 1234567

7. Hold the job but allow its owner to release it:

   .. code-block:: console

      [user@login-x:~]$ scontrol uhold 1234567

8. Remove the job hold:

   .. code-block:: console

      [user@login-x:~]$ scontrol release 1234567

.. _coord check priority:

Check Priority/Fairshare
------------------------

1. Display historical fair share usage for account:

   .. code-block:: console

      [user@login-x:~]$ sshare -a -l -A panteater_lab

2. Display pending jobs sorted by priority:

   .. code-block:: console

      [user@login-x:~]$ squeue -S '-p' --state=pending | less
