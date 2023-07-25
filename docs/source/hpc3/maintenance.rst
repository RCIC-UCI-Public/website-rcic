.. _maintenance:

Maintenance
===========

We periodically need to perform maintenance on HPC3 and storage nodes
where all users are logged out and all jobs are stopped.

There can be multiple few reasons for the maintenance, for example:

- Operating System software upgrade
- DFS servers software upgrade
- Slurm server software upgrade
- BIOS upgrade

:bluelight:`Before the maintenance`:
  * We send email notification to all users specifying the expected start/end
    time and other relevant information specific to the maintenance.
  * .. attention:: If you are submitting jobs that are not guaranteed to finish before the
                   maintenance start time, the jobs  will be held in the queue.

    All queues have default time limit, see :ref:`available partitions`.
    As the maintenance period approaches, submitting with the default time
    limit will affect more jobs.

    If you want to run something before the maintenance, resubmit your job with a shorter
    time limit, see :ref:`request time`.

  * Check the status of your submitted jobs and remove all that are held due to
    the maintenance or are in :tt:`CG` state.

:bluelight:`During the maintenance`:
  * All logins are disabled.
  * All queued jobs are stopped.
  * NO jobs can be running.
  * We will endeavor to keep queued jobs during the Slurm upgrade.
  * Please do not send us emails or tickets asking when the cluster is available. 
    We are doing everything we can to make the maintenance as short as possible
    considering the tasks at hand. You will be notified when the cluster is available.

:bluelight:`After the maintenance`:
  * We send email to all users telling when logins and jobs can resume.
  * It is possible that any held jobs may need to be resubmitted after HPC3 is returned to service.
    Check your jobs status.
