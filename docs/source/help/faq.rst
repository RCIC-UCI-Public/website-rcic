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

Who defined the policy?
~~~~~~~~~~~~~~~~~~~~~~~

* The HPC3 subcommittee of the RCIC advisory committee crafted the initial policy.
* The RCIC Advisory committee approved the policy

Please see :ref:`advisory`

How do I acknowledge RCIC?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`acknowledge`

Is there a description that can be used in grant applications?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`grant`

Does this sharing cause problems with granting agencies?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We don’t believe so.  The *condo conversion factor (0.95)* essentially enables an owner to turn
around and spend their converted hours on their owned hardware. The 5% reductions is a rational
estimate of lack of availability of hardware when accounting for software maintenance, reboots,
and other downtime. Grants should purchase the hardware capacity they require. Not more.
Please see :ref:`buy hardware` for details.

I don’t have any funds to purchase cycles or buy hardware, can I use HPC3?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, if you are faculty member, you have granted cycles that are yours to use anyway you see fit
for research. There are also the “free” queues, where jobs are not charged.
Please see :ref:`no-cost allocations` for details.

If I purchase core-hours, is overhead charged?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are actively working with UCI financial office to see if we can establish
a rate that reduces the financial impact of overhead on recharged-cycles.

:bluelight:`Accounting`
-----------------------

How can I be added to my PI's lab account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PIs have control over who can charge to their account and how much they can charge.
Please send a request to hpc-support@uci.edu
*with a cc to your PI* and ask us to add you to the PI's account.
The PI will have to confirm via email reply that this change is allowed.

How do I prevent my grad student from *draining my account* before I know about it?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RCIC will allow you to set up *charge limits* for any particular user.  If
students hit their limits, they will have to ask you for more, or use the free queue.

Will HPC3 allow long-running (multi-day/multi-week) jobs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. It is clear that substantial community of researchers requires this feature.

How does core-hour accounting impact long-running jobs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It really doesn't. Slurm will not  start the job unless there is enough
credit to start the job. For example, a job is submitted with a requirements
of *16 core-weeks* will not start unless an account has :math:`16 * 7 * 24 = 2688`
core hours.

My account reallocation is less than 100,00 core-hours, why is that?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The no-cost reallocation is calculated every 6 months based on the lab's
previous  usage. Please see details in :ref:`no-cost reallocation`.

:bluelight:`Files storage and transfer`
---------------------------------------

I have to store many files, some are pretty large. Where do I do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Please see :ref:`data transfer` section.

How do I use Filezilla with DUO?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`filezilla duo`.

I accidentally deleted some files (or directories). Can they be restored?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- First, It depends on the time between the file creation and file deletion. If
  a file was created or changed and there was a backup after that then it
  you can use snapshots to restore files and directories provided that existing
  snapshots still hold the desired data.
- The restoration method depends on where the files was originally
  located. Please see respective guides for recovery explanation:

  :$HOME:
    :ref:`home files recovery`
  :DFS:
    :ref:`selective backup recovery`
  :CRSP:
    :ref:`crsp files recovery`

:bluelight:`DFS`
----------------

What are allocations for DFS?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users have access to the private and group-shared areas on BeeGFS.
UCI Faculty members can have low-cost recharge allocation(s) to fulfill their needs.
Please see :ref:`allocations`

How do I purchase more DFS space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`buy dfs` how to purchase more DFS storage

I want to use my group DFS area, how do i do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your PI already has a group DFS area you need to submit a ticket
to hpc-support@uci.edu requesting to be be added to a specific group
for a specific DFS filesystem access, *with a cc to your PI*.
Your PI will need to reply with a confirmation in order for us to approve your request.

:bluelight:`CRSP`
-----------------

Exactly who is entitled to baseline allocation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All ladder faculty and any UCI employee who can serve as PI or Co-PI on an extramural grant.
Please see :ref:`allocations` for details.

How do I purchase more space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see how to :ref:`buy crsp`

Can I expand space more than once?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. We track when each of your space allocations expire and recharge
appropriately.  Multiple purchases can be used to expand your space.

Can the recharge be used to expand my baseline allocation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will always have your baseline allocation and you can use recharge to buy more space.
For example, if you were to purchase 10TB for 1 year ($600) and add it to your baseline, you will
have 11TB of allocated space. Please see how to :ref:`buy crsp`
and :ref:`recharge allocations` for pricing.

Can I grant access to my storage to others at UCI?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Under your control, you can add people (by the UCINetID)
to have read, write or read/write access to your storage.

Can I grant access to my storage to others outside of UCI?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to sponsor a UCINetID for your external collaborators.
They will then be able to access CRSP using normal mechanisms. Please see
:ref:`access`.

Can I add several students/postdocs to my Lab space, how do I do that?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`getting crsp account`

Can departments purchase CRSP space to store business data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. CRSP is designed and funded for research data.  Storing non-research data
will compromise CRSP status as research equipment (which has significant tax implications).

Am I charged on how much space I use on some sort of average basis?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No.  This is a capacity recharge similar to purchasing an N Terabyte disk dedicated for your use.
If you are utilizing only 1/2 of the space, you are still charged for your purchased capacity.

What happens if I can't pay for my space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will be required to bring your utilized capacity to be within your
baseline allocation.  RCIC can work with you to move data off of CRSP
in a timely manner.

If a researcher is not reducing utilized capacity, access to all data
in this space will be frozen (no read or write access). If, after multiple
attempts, the owner of the space remains unresponsive, data will be deleted
to bring it to baseline allocation.

Can researchers pool their baseline allocation to make one large space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. In extensive consultation with RCIC Executive committee, we established
the people cost of tracking and implementing such combinations outweigh the benefits.

Are there any in/out network  charges similar to commercial cloud storage?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. CRSP is connected at high-speed to the campus network and leverages this existing resource.

I can't access CRSP from home, why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All access modes of CRSP require you to be connected the UCI production network.
From home, you must use the `campus VPN <https://www.oit.uci.edu/help/vpn>`_

I downloaded Webdrive directly from their website, how do I add the UCI license?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You cannot. **You must use RCIC-provided CRSP Desktop**
which is a specialized version of Webdrive for Windows and Mac that already have the license key embedded.
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

I get file write error when saving files in my $HOME, what is wrong?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You exceeded your $HOME disk quota.
See :ref:`home quotas` that explains how to check and fix.

I cant save files in my CRSP area. How do i check my quotas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
See :ref:`crsp quotas` for explanation.

When writing files I get the “Disk quota exceeded” error on /dfsX/labY. How can it be?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You need to check your quotas and verify directories permissions.
See :ref:`dfs quotas` for instructions on checking quotas and
:ref:`data transfer` for tips on data transfers.

I am running a Slurm job and am getting the “Disk quota exceeded” error on /dfsX/labY?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is group writable area, all users who write in this area contribute to
the quota and the quota is sum total of all written files. Even if your
job output small files, others may have filled it.
You need to check your :ref:`dfs quotas` for the specific DFS filesystem.

:bluelight:`Slurm jobs`
-----------------------

Why should I request an interactive shell and how do I do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users need to use an interactive shell when they plan to run some tasks
that take longer than 20 min and are compute intensive (CPU or
memory) operations. These includes running applications (including GUI) or data
transfers. The interactive shells are simply processes that run on compute nodes
of the cluster. See how to request an :ref:`interactive job`.

How do I submit a job to the Slurm queue and see its status?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can submit a job as an interactive shell using ``srun``
command or a batch job using ``sbatch`` command and see
a status of a submitted job with ``squeue`` command.
See :ref:`slurm guide <jobs>` for examples.

What are array jobs, how do I submit an array job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Array jobs are identical independent jobs that are run using one or
more different input parameters. Instead of writing many submit scripts
one can use a single script to submit many jobs. See :ref:`array jobs <job array>`
for details.

Why am I getting emails about running my application on login node?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are causing problems for others users. Running applications on login nodes
is a violation of our  :ref:`acceptable use` policy and
:ref:`conduct rules` rules. Review both and adjust your work on the
cluster.

How do I charge my jobs to my account or my PI’s account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every user has a default account (which is *UCnetID*) and may have a few PI lab accounts.
If not specified, a default account is charged (exception is free queues).

To specify a PI's account one need to use a :tt:``-A`` Slurm directive either on
a command line when asking fort an interactive shell or in a Slurm batch
job. See :ref:`slurm guide <jobs>` for examples.

How do I buy more Slurm time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A basic allocation is explained in :ref:`allocations`.
Only PI can purchase more hours, please see :ref:`buy core-hours`.

How do I ask for more cores for my job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to specify options ``--ntasks`` or ``--cpus-per-task`` in your
job submission. See :ref:`request resources`.


If I ask for X cores does my job run X times faster?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Asking for more cores does not make your program run faster unless your program is
capable of using multiple cores.  The performance of a  given program does not
always scale with more CPUs.

How do I know if I need more cores for my job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are 2 distinct situations:

1. You have a program that is multi-CPU aware.
   Often such programs have a *parameter* that specifies the number of CPUs it will use.
   If the program has no such switch, or you don’t set the switch, your program is likely
   using 1 CPU.
2. Your job failed with OOM - out of memory errors.

See See :ref:`request resources` for explanation how to get more CPUs or more memory.

How do I know if I need more memory for a job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Your job failed with OOM - out of memory errors.
2. You have a general knowledge of how much memory your program is using
   on an input of a certain size and you have increased the input.

To find out how much memory and CPU your job is using you need
to use ``sacct``, ``seff`` and ``sstat`` commands.
See :ref:`job monitoring <job monitoring>` for details.

How do I profile my job?
~~~~~~~~~~~~~~~~~~~~~~~~

Slurm records statistics for every job, including how much memory
and CPU was used, and the usage efficiency.

Slurm provides :ref:`job monitoring <job monitoring>` capabilities
that can give an idea about consumed memory, CPU and the efficiency. For most
jobs they provide sufficient information to understand what resources are needed.

How do I see how many hours of allocation credit I have used?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to use ``sbank`` command.  See :ref:`job accounting`.

How do I see what jobs were run and what they cost over a period of time for an account ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have a ``zotledger`` tool that provides this info.
See :ref:`job accounting`.

I can't submit jobs to GPU partition, what is wrong with my account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nothing is wrong, you simply need to have a separate GPU account to submit
jobs to GPU partition.

GPU accounts are not automatically given to everyone, your faculty adviser can
request a GPU lab account.  For example, a PI *panteater* will have accounts:

| *PANTEATER_LAB* - for CPU jobs
| *PANTEATER_LAB_GPU* - for GPU jobs

All users can submit jobs to *free-gpu* partition without special GPU account.

My job failed with "out of memory error". What should i do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your job was removed by Slurm because it exceeded its memory request.
All partitions have :ref:`specific configuration <paritions structure>`
for memory, runtime, etc.
You need to increase the memory requirements for your job. See examples of
how to :ref:`request more memory <request memory>`.

For the jobs that require more memory than the
*standard/free* partitions can provide or for the jobs that require A LOT of memory
and not many CPUs, there is a limited number of higher memory nodes that are
accessible via higher memory partitions.
The :ref:`memory partitions` guide explains how to request an access.

How do I use higher memory partitions highmem/hugemem/maxmem?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :ref:`memory partitions` guide explains how to request an access.

My job is pending with reason shown as *AssocGrpCPUMinutesLimit*, what is wrong?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You don't have enough hours in your account balance to run the job. See
:ref:`job pending` for an explanation and how to fix.

My job is killed after running for 48 hours, why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All queues have specific :ref:`default and max runtime limits <paritions structure>`.
The default run time protects users from unintentionally using more CPU hours than intended.

You run your job with *a default runtime*, and Slurm killed the job once the run
time limit was reached. If your job needs longer runtime, you need to :ref:`request time`.

:bluelight:`Software`
---------------------

How do I install new software myself?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the :ref:`user installed` guide.

How do I request software installation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`software tickets`.
