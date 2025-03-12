.. _faq:

Frequently Asked Questions
==========================

.. contents::
   :local:

..
  FAQ should be questions that actually got asked.
  Formulate them as a question and an answer.
  Consider that the answer is best as a reference to another place in the documentation.


:bluelight:`HPC3 general`
-------------------------

Who can have an account?
~~~~~~~~~~~~~~~~~~~~~~~~~
  Anyone with a valid UCInetID. Please see :ref:`get account`.

How long can I have an account after graduation/separation from UCI?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  For as long as your UCInetID is valid.
  Please see :ref:`closing account`.

Who defined the policy?
~~~~~~~~~~~~~~~~~~~~~~~
  * The HPC3 subcommittee of the RCIC advisory committee crafted the initial policy.
  * The RCIC Advisory committee approved the policy
  * Please see :ref:`advisory`

How do I acknowledge RCIC?
~~~~~~~~~~~~~~~~~~~~~~~~~~
  :ref:`acknowledge`

Is there a description that can be used in grant applications?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  :ref:`grant`

Does this sharing cause problems with granting agencies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  We don’t believe so.  The *condo conversion factor (0.95)* essentially enables an owner to turn
  around and spend their converted hours on their owned hardware. The 5% reductions is a rational
  estimate of lack of availability of hardware when accounting for software maintenance, reboots,
  and other downtime. Grants should purchase the hardware capacity they require. Not more.
  Please see :ref:`buy hardware` for details.

I don’t have any funds to buy cycles or hardware, can I use HPC3?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Yes, if you are faculty member, you can have granted cycles that are yours to use anyway you see fit
  for research. There are also the *free* queues, where jobs are not charged.
  Please see :ref:`no-cost allocations` for details.

If I purchase core-hours, is overhead charged?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  We are actively working with UCI financial office to see if we can establish
  a rate that reduces the financial impact of overhead on recharged-cycles.

:bluelight:`Accounting`
-----------------------

.. _reset password:

I can't login, can you reset my password?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | :red:`We do not store, handle or reset passwords for UCInetIDs`.
  | Your password is the one you have set for your UCInetID. 
  | Please see OIT website page `how to change passwords <https://www.security.uci.edu/how-to/passwords/>`_.

.. _add lab account:

How can I be added to my PI's Slurm lab account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  PIs have control over who can charge to their account and how much they can charge.

  * Please send a request to hpc-support@uci.edu
    *with a cc to your PI* and ask us to add you to the PI's account.
  * The PI :underline:`must` confirm via email reply to your *cc* that this change is allowed.

How do I prevent my grad student from *draining* my account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Submit a ticket and ask us to set up *charge limits* for any particular user. If
  students hit their limits, they will have to ask you for more, or use the free queue.

Will HPC3 allow long-running (multi-day/multi-week) jobs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Yes. It is clear that substantial community of researchers requires this feature.

How does core-hour accounting impact long-running jobs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  It doesn't. Slurm will not  start the job unless there is enough
  credit to start the job. For example, a job is submitted with a requirement
  of *16 core-weeks* will not start unless an account has :math:`16 * 7 * 24 = 2688`
  core hours.

Why is my account reallocation less than 100,00 core-hours?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The no-cost reallocation is calculated every 6 months based on the lab's
  previous  usage. Please see details in :ref:`no-cost reallocation`.

:bluelight:`Files storage and transfer`
---------------------------------------

Where can I store store many files, some are large?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Depending on your lab affiliation and how much space your lab has purchased
  you may have an access to personal and group-access areas in CRSP and DFS
  file systems. See :ref:`dfs` and :ref:`crsp` for information where to store and how to
  check quotas.

How do I backup important files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  It depends on what filesystem you are using:

  :$HOME:
     has automatic snapshots, you don't need to do anything special.
     Please read :ref:`zfs snapshots` for details.
  :CRSP:
     Your :tt:`$HOME` and :tt:`LAB areas` have automatic snapshots, you don't
     need to do anything special. Please see  :ref:`crsp snapshots`.
  :DFS:
     You can use :ref:`selective backup`.

How do I transfer files between a remote server and my directory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`data transfer`.

How do I use FileZilla with DUO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`filezilla duo`.

Can accidentally deleted files or directories be restored?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - First, It depends on the time between the file creation and file deletion. If
    a file was created or changed and there was a backup after that then it
    you can use snapshots to restore files and directories provided that existing
    snapshots still hold the desired data.
  - The restoration method depends on where the files was originally
    located. Please see respective guides for recovery explanation:

    - :ref:`$HOME files <home files recovery>`
    - :ref:`DFS files <selective backup recovery>`
    - :ref:`CRSP files <crsp snapshots>`

:bluelight:`DFS`
----------------

What are allocations for DFS?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | Users have access to the private and group-shared areas on DFS:
  |   * **private**: :red:`Private areas are in /pub/$USER and are for user only, not shared with anyone.`
  |   * **group-shared**: UCI Faculty members can have low-cost recharge allocation(s) and have 
        areas to fulfill their needs where they can add group members to the access.
  | Please see :ref:`allocations` for details.

How do I purchase more DFS space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`buy dfs`.

.. _add lab dfs:

I want to use my PI's group DFS area, how do i do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  * If your PI already has a group DFS area you need to submit a ticket
    to hpc-support@uci.edu requesting to be be added to a specific group
    for a specific DFS filesystem access, *with a cc to your PI*.
  * Your PI :underline:`must` confirm via email reply to your *cc* that this change is allowed.

:bluelight:`CRSP`
-----------------

.. _add lab crsp:

I want to use my PI's group CRSP area, how do i do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`getting crsp account`

Exactly who is entitled to my CRSP baseline allocation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  All ladder faculty and any UCI employee who can serve as PI or Co-PI on an extramural grant.
  Please see :ref:`allocations`.

How do I purchase more space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`buy crsp`

Can I expand space more than once?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | Yes. We track when each of your space allocations expire and recharge appropriately.
  | Multiple purchases can be used to expand your space.

Can the recharge be used to expand my baseline allocation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | You will always have your baseline allocation and you can use recharge to buy more space.
  | For example, if you were to purchase 10TB for 1 year ($600) and add it to your baseline, you will
    have 11TB of allocated space.
  | Please see how to :ref:`buy crsp` and :ref:`recharge allocations` for pricing.

Can I grant access to my CRSP storage to others at UCI?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Yes. Under your control. You can submit a ticket and ask us to
  add people (by the UCInetID) to have read, write or read/write access to your storage.

Can I grant access to my storage to others outside of UCI?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You will need to sponsor a UCInetID for your external collaborators.
  They will then be able to access CRSP using normal mechanisms.
  Please see :ref:`access`.

Can do I add several students/postdocs to my Lab space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`getting crsp account`

Can departments purchase CRSP space to store business data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  No. CRSP is designed and funded for research data.  Storing non-research data
  will compromise CRSP status as research equipment (which has significant tax implications).

Am I charged how much space I use on some average basis?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | No. This is a capacity recharge similar to purchasing an N Terabyte disk dedicated for your use.
  | If you are utilizing only 1/2 of the space, you are still charged for your purchased capacity.

What happens if I can't pay for my space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  RCIC can work with you to move data off of CRSP in a timely manner:
    * You will be required to bring your utilized capacity to be within your baseline allocation.
    * If a researcher is not reducing utilized capacity, access to all data
      in this space will be frozen (no read or write access).
    * If, after multiple attempts, the owner of the space remains unresponsive,
      data will be deleted to bring it to baseline allocation.

Can researchers pool their allocations into one large space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  No. In extensive consultation with RCIC Executive committee, we established
  the people cost of tracking and implementing such combinations outweigh the benefits.

Any in/out network charges as with commercial cloud storage?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  No. CRSP is connected at high-speed to the campus network and leverages this existing resource.

I can't access CRSP from home, why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | All access modes of CRSP require you to be connected the UCI production network.
  | From home, you must use the `campus VPN <https://www.oit.uci.edu/help/vpn>`_

Can I add the UCI license to WebDrive I got from their website?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You cannot. **You must use RCIC-provided CRSP Desktop** which is a
  specialized version of WebDrive for Windows and Mac that already have the license key embedded.
  Please see :ref:`client desktop windows` and :ref:`client desktop mac` for
  instructions how to download and use.

I want to publish some of my data on the web, can I do that?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Not yet. This is more complicated than it might appear.
  The key questions revolve around data security.

I have trouble accessing CRSP shares
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Consult our :ref:`crsp troubleshoot`.

:bluelight:`Disk Quotas`
------------------------

Why do I get file write error when saving files in my $HOME?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You exceeded your $HOME disk quota.
  See :ref:`home quotas` that explains how to check and fix.

I can't save files in my CRSP area. How do i check my quotas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  See :ref:`crsp quotas` for explanation.

I get the *Disk quota exceeded* error on /dfsX/labY. Why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You need to check your quotas and verify directories permissions.
  See :ref:`dfs quotas` for instructions on checking quotas and
  :ref:`data transfer` for tips on data transfers.

My Slurm job failed with the *Disk quota exceeded* on /dfsX/labY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  This is group writable area, all users who write in this area contribute to
  the quota and the quota is sum total of all written files. Even if your
  job output small files, others may have filled it.
  You need to check your :ref:`dfs quotas` for the specific DFS filesystem.

:bluelight:`Slurm jobs`
-----------------------

Can you give me an estimate of the expected wait times?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  It is impossible to answer because how long a job waits depends on many job-specific parameters
  and the current cluster load:

  * If one asks for a generic core on the *standard* partition, the job is likely to schedule immediately.
  * Not all nodes in HPC3 have the same physical configuration and if a job specification is such that
    only a small number of nodes can match such job request, one might wait days or even weeks.
  * It takes longer to reserve entire nodes because one has to wait for all other jobs on the node to complete.
  * It is highly dependent on the current cluster load. During the low load periods the jobs will schedule quite quickly,
    and during the high load periods the scheduling will take a bit more time.

My job failed with *out of memory (OOM)* error. What can i do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The actual message can vary depending on where and how you run your application and may contain *OOM Killed*,
  *oom_kill events* or *oom-kill*.

  OOM signifies *Out Of Memory* errors. This means you requested a certain amount
  of memory but your job went over the limit and SLURM has terminated your job.

  All partitions have :ref:`specific configuration <partitions structure>` for
  memory, runtime, CPUs:

    * You need to increase the memory requirements for your job.
      See :ref:`How to get more memory <request memory>`.
    * For the jobs that require more memory than the
      *standard/free* partitions can provide or for the jobs that require *a lot of memory
      and not many CPUs*, there is a limited number of higher memory nodes that are
      accessible via higher memory partitions.
      The :ref:`memory partitions` guide explains how to request an access.

Why should I request an interactive job and how do I do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | The interactive job are simply processes that run on compute nodes of the cluster.
  | Users need to use an interactive job when they plan to:
  
     * run some tasks that take longer than 20 min
     * run CPU or memory intensive tasks
     * run applications (including GUI)
     * do data transfers
     * do conda/mamba installs 

  See how to request an :ref:`interactive job`.

How do I submit a job to the Slurm queue and see its status?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  * Submit an interactive job with ``srun`` command 
  * Submit a batch job with ``sbatch`` command
  * See a status of a submitted job with ``squeue`` command

  See :ref:`Slurm jobs guide <jobs>` for examples.

What are array jobs and how do I submit them?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | Array jobs are identical independent jobs that are run with different input parameters.
  | Instead of writing many submit scripts one can use a single script to submit many jobs.
  | This approach is much more efficient. See :ref:`array jobs <job array>`.

Why I get emails about running my processes on login node?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You are causing problems for other users.
  Running applications on login nodes is a violation of our  :ref:`acceptable use` policy and
  :ref:`conduct rules` rules.  Review both and adjust your work.

How do I charge my jobs to my account or my PI’s account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Every user has a default account (which is *UCnetID*) and may have an access
  to PI lab accounts.  If not specified, a default account is charged (exception is free queues).

  See :ref:`slurm guide <jobs>` for examples how to specify accounts for interactive and batch jobs.

How do I buy more Slurm time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | Only PI can purchase more hours, please see :ref:`buy core-hours`.
  | A basic allocation is explained in :ref:`allocations`.

How do I ask for more cores for my job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | You need to specify options ``--ntasks`` or ``--cpus-per-task`` in your job submission.
  | See :ref:`request resources`.

If I ask for X cores does my job run X times faster?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Asking for more cores does not make your program run faster unless your program is
  capable of using multiple cores.  The performance of a  given program does not
  always scale with more CPUs.

How do I know if I need more cores for my job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  There are 2 distinct situations:

  * You have a program that is multi-CPU aware.
    Often such programs have a *parameter* that specifies the number of CPUs it will use.
    If the program has no such switch, or you don’t set the switch, your program is likely
    using 1 CPU.
  * Your job failed with OOM - out of memory errors.

  See :ref:`request resources` for explanation how to get more CPUs or more memory.

How do I know if I need more memory for a job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  * Your job failed with out of memory errors (OOM).
  * You have a general knowledge of how much memory your program is using
    on an input of a certain size and you have increased the input.

  To find out how much memory and CPU your job is using you need
  to use ``sacct``, ``seff`` and ``sstat`` commands.
  See :ref:`job monitoring <job efficiency>` for details.

How do I profile my job?
~~~~~~~~~~~~~~~~~~~~~~~~
  Slurm records statistics for every job, including how much memory
  and CPU was used, and the usage efficiency.

  Slurm provides :ref:`job efficiency monitoring <job efficiency>` capabilities
  that can give an idea about consumed memory, CPU and the efficiency. For most
  jobs job efficiency tools provide sufficient information to understand what resources are needed.

How do I see how many hours of allocation credit I have used?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You need to use ``sbank`` command.  See :ref:`job accounting`.

How to see what jobs were run and their cost over some time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  We have a ``zotledger`` tool that provides this info.
  See :ref:`job accounting`.

I can't submit jobs to GPU partition, what is wrong?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | You are likely using your regular CPU account. 
  | You need to have a separate GPU account to submit jobs to paid *gpu* partitions.
  | All users can submit jobs to *free-gpu* partition without special GPU account.

  GPU accounts are not automatically given to everyone, your faculty adviser can
  request a GPU lab account and add you to the account access. For example, a
  PI *panteater* may have accounts:

    | for CPU jobs - *PANTEATER_LAB* 
    | for GPU jobs - *PANTEATER_LAB_GPU* 


How do I use partitions highmem/hugemem/maxmem?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The :ref:`memory partitions` guide explains how to request an access.

Why is my job pending with an *AssocGrpCPUMinutesLimit*? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  | You don't have enough hours in your account balance to run the job.
  | See :ref:`job pending` for an explanation and how to fix.

My job is killed after running for 48 hours, why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You run your job with *a default runtime*, and Slurm killed the job once the run time limit was reached.
  All queues have specific :ref:`default and max runtime limits <partitions structure>`.
  The default run time protects users from unintentionally using more CPU hours than intended.

  If your job needs longer runtime, you need to :ref:`request runtime <request time>`.

My job needs longer time than 14 days, how do I request this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  * First, you  need to submit your job for the partition's
    :ref:`max runtime limits <partitions structure>`.
  * Second,  request :ref:`job time limit modification <modify job>`.

:bluelight:`Software`
---------------------

How do I install new software myself?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`user installed` guide.

How do I request software installation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Please see :ref:`software install tickets`.
