.. _news archive:

News Archive
============

.. contents::
   :local:

.. _news 2024:

2024
----

Sep 17
^^^^^^

| :blogtitle:`HPC3 Downtime Sep 17, 2024`
| :blogauthor:`2024-09-17 by Nadya Williams`

The next outage will be September 17, 2024, beginning at 8am

Maintenance items:
  1. Upgrading Slurm to version 24.03.3
  #. Replacing the Slurm scheduler node with new hardware
  #. Rebooting all nodes in HPC3

Impacts:
  1. Queued jobs should remain queued after the hardware upgrade.
     We will be transferring all slurm state to the new hardware.
     There is, however, a small chance that queued jobs will be "lost".

We don't expect this to be an all-day affair and hope to have HPC3 back in service by early afternoon.

Jul 16
^^^^^^

| :blogtitle:`HPC3 Downtime Jul 16, 2024`
| :blogauthor:`2024-07-05 by Nadya Williams`

The next outage will be July 16, 2024, beginning at 8am

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

Mar 27
^^^^^^

| :blogtitle:`HPC3 Downtime Mar 27, 2024`
| :blogauthor:`2024-03-20 by Philip Papadopoulos`

The next outage will be March 27, 2024, beginning at 8am

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

.. _news 2023:

2023 
----

Dec 19
^^^^^^

| :blogtitle:`HPC3 Downtime Dec 19, 2023`
| :blogauthor:`2023-12-14 by Philip Papadopoulos`

The next outage will be December 19, 2023, beginning at 8am

RCIC will be performing our regular, between quarters, maintenance next Tuesday, Dec 19.
All users will be logged out, pending jobs will remain queued.

**Maintenance Items**:
  1. Update BeeGFS from 7.4.1 --> 7.4.2. This addresses some known bugs within BeeGFS (used on all DFSx file systems)
  2. Move a shared directory (hpc3tools) from the older disk-based NAS to a newer all flash system
  3. Move selected labs from DFS4/DFS5 to DFS9 for space balancing
  4. Replace some switches that allow us to access hardware consoles on nodes
  5. Internal Slurm configuration update
  6. Reboot all nodes (required for BeeGFS update)

**Impacts**:
  * HPC3 and its file systems will be unavailable.
  * You will not be able to login or access files in /dfsX or /home.
  * All existing logins will be terminated.
  * No jobs can run during the maintenance period.
  * Slurm jobs that are not guaranteed (via TimeLimit) to complete before 8am on Tuesday will be held.
    Please see :ref:`requesting time limits <request time>` on queues.

We expect to return HPC3 to service late afternoon, late afternoon Dec 19.

Jul 25
^^^^^^

| :blogtitle:`HPC3 Downtime Jul 25, 2023`
| :blogauthor:`2023-03-12 by Philip Papadopoulos`

The next outage will be July 25, 2023, beginning at 8am

.. note:: This is the first of two outages planned for this summer.

In this outage we will be doing the following:
  1. Reinstalling all login/compute nodes with Rocky Linux 8.8 and
     applications recompiled for Rocky Linux 8.8.
  2. Updating management/storage nodes to Rocky Linux 8.8.
  3. Updating Slurm to its most recent release.

**Effects on Jobs**
  - Prior to the maintenance, :underline:`jobs that are not guaranteed to finish
    before 8am on July 25, will be held`. All queues have default time limits
    (see the RCIC website). You can also change the time limits for your jobs
    to tell Slurm that your jobs will finish prior to 8am.
  - Queued jobs - We will endeavor to keep queued jobs during the Slurm
    upgrade. However, it is possible that any held jobs may need to be
    resubmitted after HPC3 is returned to service.

**Effects on user-compiled code**
  - In general, user-compiled code will NOT need to be recompiled.
  - However, there are some differences among Rocky 8.6 (installed last summer), Rocky
    8.7 (updated early 2023) and Rocky 8.8. You might need to rebuild your application(s).

Mar 28
^^^^^^

| :blogtitle:`HPC3 Downtime Mar 28, 2023`
| :blogauthor:`2023-03-17 by Philip Papadopoulos`

We periodically need to perform maintenance on HPC3 where all users are logged out and all jobs are stopped.

The next outage will be March 28, 2023, beginning at 8am.

The major items on the list are the following:
  1. Upgrade All DFS servers to Rocky Linux 8.7
  2. Upgrade Home Area Server to Rocky Linux 8.7
  3. Reset BIOS on the dfs-3a-1 server
  4. Replace Failed Drive on dfs-2
  5. Replace dfs-7-1 with its now-repaired original server

  We will be touching a majority of storage servers during the downtime,
  but will not upgrade the version of BeeGFS.

**Why are we doing this now?**
  CentOS 7 (which is still present on several file servers) hits end-of-life in June 2024
  and needs to be phased out everywhere. BeeGFS has declared that now-and-future versions of BeeGFS will not support CentOS 7.

**We plan to upgrade the version of BeeGFS, cluster-wide, during a summer downtime.**

.. _news 2022:

2022 
----

Aug 01
^^^^^^

| :blogtitle:`HPC3/HPC2 Downtime Aug 30, 2022`
| :blogauthor:`2022-08-01 by Philip Papadopoulos`

**A Major OS Update will begin at 8am, on Tuesday, August 30, 2022**

This is Phase 2 of the upgrade (Phase 1 was June 15, 2022).
HPC2 and HPC3 will be upgraded to Enterprise Linux 8 (Rocky Linux) 
from the current CentOS version 7.  This is a major update to the clusters and requires:

* All Jobs to be terminated
* All Queues to be empty
* All Users to be logged out

**Phase 2 (August 30, 2022, All day)** we will:
  1. Reinstall all nodes with EL8
  2. Reinstall all rebuilt applications
  3. Update Slurm to the latest production release

**As reminder, a major OS update has significant impact, these include**
  * Most *user-compiled code* will need to be rebuilt.
  * *Some conda environments* may need to be rebuilt to work properly with new system libraries.
  * A few older applications simply will not build on EL8 and will be removed.
  * The planned updates and sunset of RCIC-installed applications are :ref:`software updates`.

**FAQ**

**Is keeping CentOS7 an option?**
  Not really. It will be end-of-life in  Jun 2024.
  We are already seeing commercial vendors ending support for CentOS7.
  The viability of CentOS7 as a functional OS will progressively diminish significantly
  over the next 12 months.

**I really need some of the removed software, what do I do?**
  Please contact us via our ticketing system. In some cases, we may be able to build a
  link:https://docs.sylabs.io/guides/3.5/user-guide/introduction.html[Singularity container] with the
  older applications and dependencies.

**Can I have queued jobs during this downtime?**
  No. The Slurm upgrade requires there to be neither queued nor running jobs.

**Can I continue using my conda environment after the upgrade?**
  It is very likely that you will need to rebuild your conda environment.
  Even if we build the same version of conda many underlying included packages
  will be different and of a newer version. This may or may not require your
  conda environment rebuild. You will have to test your environment and rebuild
  it if broken. 

  We provide a guide :ref:`Building and using conda environments <install conda>`.

May 19
^^^^^^

| :blogtitle:`HPC3/HPC2 Downtime June 15, 2022 and Aug TBD, 20202`
| :blogauthor:`2022-05-19 by Philip Papadopoulos`

We periodically need to perform maintenance on HPC3 where all users are 
logged out and all jobs are stopped.  We have two planned  outages for 
this summer. The highlights of upcoming changes addressed by these two outages include:

* DUO two-factor authentication will become standard on HPC2/3 login
* Parallel File System and ZFS updated to latest stable releases
* CentOS 7 will be sunset and Enterprise Linux 8 (EL8, Rocky Linux) will be the new OS
  The entire application software stack will be rebuilt for EL8. Older versions will be retained where possible,
  new application versions will be added
* The version of Slurm will be updated to the latest stable release

While we normally prefer to have only a single downtime, the changes are large 
enough that we will handle the changes in two distinct phases.

**Phase 1  (June 15, 2022, All day)**
  * BeeGFS and ZFS file system updates
  * Turn on Two-Factor (Duo) authentication

**Phase 2 ( Aug TBD, 2022, All day)**
  * Reinstall all nodes with EL8
  * Reinstall all rebuilt applications
  * Update Slurm

The first downtime (June 15) should only have the apparent effect on users 
that Duo authentication will now be required for password-based login to HPC3 and HPC2.

The second downtime (Aug) will be much more impactful.
In general, any user-compiled code will need to be rebuilt.
Some conda environments may also need to be rebuilt to work properly with new system libraries.
A few older applications simply will not build on EL8.
Some widely-used versions of software - e.g. R version 3, older versions of R 4 are not buildable with 
all R modules under EL8.  As the summer progresses, we will keep a list of sunset software.

**Is keeping CentOS7 an option?**  
  Not really. It will be end-of-life in Mid-2024. We are already seeing commercial vendors
  ending support for CentOS7. The viability of CentOS7 as a functional OS will progressively diminish over the next 24 months.

.. _news 2021:

2021 
-----

.. _symposium 2021:

Symposium Jun 04
^^^^^^^^^^^^^^^^

| :blogtitle:`Research Infrastructure Symposium`
| :rcicorange:`Date: 04 June 2021,  Zoom 10:00am - 2:30pm.`

You are invited to participate in the 2021 virtual symposium of UCI's Research Cyberinfrastructure Center (RCIC).
The symposium will take place on June 4th, 2021, via zoom (details below). This event aims to bring together
students, researchers, staff, instructors, and outreach partners who use or would like to use and/or contribute
to the shared campus-wide hardware and software resources as well the human expertise provided by RCIC and the
UCI libraries.

Participation is free and no registration is required, but only zoom users
with a :bluelight:`@uci.edu` email address can participate.

.. note:: This meeting will be recorded.

**Agenda**

.. table:: 
   :class: noscroll-table

   ======== =====================================================================
   :rcicorange:`UCI computing and data infrastructure`
   ------------------------------------------------------------------------------
   10:00 am Opening remarks - VCR Pramod Khargonekar
   10:05 am RCIC capabilities and operation - Phil Papadopoulos and staff
   10:50 am Madelynn Dickerson - Digital scholarship services
   11:00 am Break
   :rcicorange:`HPC and HTC applications in research`
   ------------------------------------------------------------------------------
   11:05 am Brandon Gaut - Ecology & Evolutionary Biology
   11:25 am Penghui Cao - Mechanical and Aerospace Engineering
   11:45 am Enrico Tapavicza - Computational Chemistry, CSULB
   12:05 pm Lunch Break
   :rcicorange:`HPC and HTC in teaching and outreach`
   ------------------------------------------------------------------------------
   01:00 pm Trina Norden-Krichmar - Epidemiology and Biostatistics
   01:20 pm Anthony Long - Ecology & Evolutionary Biology
   01:40 pm Break
   :rcicorange:`Discussion`
   ------------------------------------------------------------------------------
   01:45 pm Jenny Wu, PhD - Director Bioinformatics for GHTF
   02:00 pm Virtual panel Q&A with the campus computing community
   02:30 pm Closing remarks
   ======== =====================================================================

**Zoom Information**

.. table:: 

   ================== =====================================================================
   Topic:             RCIC Symposium
   Time:              Jun 4, 2021 10:00 AM Pacific Time (US and Canada)
   Join Zoom Meeting: http://uci.zoom.us/j/95381740249?pwd=ekNOMWs4YkRtTzgvVkdEY1liVFJMdz09
   Meeting ID:        953 8174 0249
   Passcode:          015678
   ================== =====================================================================

May 04
^^^^^^

| :blogtitle:`Research Infrastructure Symposium - June 4, 2021`
| :blogauthor:`2021-05-24 by Philip Papadopoulos`

You are invited to participate in the **2021 Virtual symposium 
of UCI's Research Cyberinfrastructure Center (RCIC)**.

The symposium will take place on **June 4th, 2021, via zoom (10:00am - 2:30pm)**.
This event aims to bring together students, researchers, staff, instructors, 
and outreach partners who use or would like to use and/or contribute
to the shared campus-wide hardware and software resources as well the human 
expertise provided by RCIC and the UCI libraries.

Participation is free and no registration is required, but only zoom users with
an **@uci.edu** email address can participate.
Please see the details in :ref:`symposium 2021`.

We look forward to seeing you online!

| - Filipp Furche, Professor of Chemistry
| - Phil Papadopoulos, RCIC Director


.. _news 2020:

2020 
-----

Nov 04
^^^^^^

| :blogtitle:`HPC3 Production and HPC Shutdown on 5 Jan 2021`
| :blogauthor:`2020-11-04 by Philip Papadopoulos`

| We are pleased to announce that :ref:`hpc3` is in  *production*.
| All existing HPC users have accounts on HPC3 and can get started right away.
| A short presentation `HPC3 for HPC users  </_static/HPC3_for_HPC_Users.pdf>`_
  answers some of the key questions up front.

.. attention:: 
  
   The existing HPC cluster will run until 5 Jan 2021. 

   On that day, RCIC will shut down the queuing system, kill all
   running jobs and begin the process of physically dismantling HPC, moving some hardware to HPC3, and starting the
   transition of selected *mid-life* nodes for a cluster called HPC2.

   | Users should begin their transition to HPC3 now.
   | Please note that any files in your current HPC home area will be discarded sometime in January.

Jul 15
^^^^^^

| :blogtitle:`HPC3 Production Ramp Up`
| :blogauthor:`2020-07-15 by Philip Papadopoulos`

We are pleased to announce that :ref:`hpc3` will enter its *production ramp up*
on 20 July 2020. A short presentation `Production Ramp-up </_static/Production_Ramp_Up.pdf>`_ 
describes this phase of HPC3.

To handle the transition of a large number of users to HPC3 during the ramp up, we're asking that research
groups/labs submit a single request to hpc-support@uci.edu (please see the presentation of what to include).

| Friendly users on HPC3 have consumed over 1 million core hours on 1+ million jobs.
| We expect the production ramp up to last about two months.


.. _news 2019:

2019 
-----

May 30
^^^^^^

| :blogtitle:`CRSP HAProxy load balancer maintenance on June 11, 2019`
| :blogauthor:`2019-05-30 by Imam Toufique`

CRSP HaProxy servers will undergo maintenance on June 11th 2019, between 7AM PST - 8AM PST.
There is no planned user service interruption during this time. However, if access to CRSP
is disrupted due to any unforeseen issues, service will be restored as soon as possible.

Thank you for your patience!

May 15
^^^^^^

| :blogtitle:`Campus Research Storage (CRSP) Enters Full Production`
| :blogauthor:`2019-05-15 by Philip Papadopoulos`

The :ref:`crsp` has entered full production.
Approximately 1200 faculty and researcher accounts have been created and are active.
Each faculty/researcher is allocated 1TB of highly-reliable, no-cost storage to
utilize for research purposes. Additional space can be purchased.

CRSP storage can be accessed from a standard web browser, a site-licensed
client for Windows/Mac desktops, **sshfs** for Linux, and as a directly-mounted file
system on the HPC Cluster.

.. _symposium 2019:

Symposium Apr 04
^^^^^^^^^^^^^^^^

| :blogtitle:`RCI Symposium at Calit2 04/04/2019`

**Purpose of the Symposium**

The Research Cyberinfrastructure Center was formed because of a 
`faculty-driven process <https://web.archive.org/web/20240226070259/https://sites.uci.edu/rci/>`_ and the recognition
that computing and data are key to modern research enterprise.  In 2016,
a symposium was held to gather input and ideas from the UCI research community.

Three years later, it's time to gather again and talk about RCI @ UCI.
There has been some key progress and part of the
symposium is to introduce some of the emerging capabilities to the research
community.  There will also be a panel session for group discussion and 
a poster session during lunch so that the UCI research community 
can see what kinds of projects are utilizing Cyberinfrastructure.

Please come join us and learn about the Campus Research Storage Pool (CRSP) and
the next-generation of HPC, HPC3.

Come join us and tell what kinds of Research Cyberinfrastructure you 
would like to see at UCI emerge over the next few years.

**Proposed Agenda**

.. table::
   :class: noscroll-table

   +-------------+-----------------------------------------------------------------------+
   | Time        |  Topic                                                                |
   +=============+=======================================================================+
   | 11:00-11:15 | Welcome and Introduction to RCIC,                                     |
   |             |                                                                       |
   |             | *Filipp Furche, Philip Papadopoulos*                                  |
   +-------------+-----------------------------------------------------------------------+
   | 11:15-12:00 | Research Storage and the Campus Research Storage Pool :ref:`crsp`,    |
   |             |                                                                       |
   |             | *Imam Toufique, Philip Papadopoulos_*                                 |
   +-------------+-----------------------------------------------------------------------+
   | 12:15-01:00 | Box lunch                                                             |
   +-------------+-----------------------------------------------------------------------+
   | 01:00-01:45 | :ref:`hpc3` Motivation, Procurement, Emerging Policy,                 |
   |             |                                                                       |
   |             | *Filipp Furche, Aparna Chandramowlishwaran, Philip Papadopoulos*      |
   +-------------+-----------------------------------------------------------------------+
   | 01:45-02:30 | Panel Discussion: What do you see as the largest Research Cyber*      | 
   |             |                                                                       |
   |             | *challenges over the next 3-5 years? *Ali Mortizavi, Panel Moderator* |
   +-------------+-----------------------------------------------------------------------+

Mar 21
^^^^^^

| :blogtitle:`RCI Symposium to be held at Calit2 04/04/2019`
| :blogauthor:`2019-03-21 by Philip Papadopoulos`

The RCI :ref:`symposium 2019`  has been scheduled as forum for the UCI 
community to shape Research Cyberinfrastructure. 

Filipp Furche, chair of the :ref:`advisory` sent an all campus invitation to the symposium.

Lunch will be provided for registered participants.

Jan 25
^^^^^^

| :blogtitle:`CRSP Hardware Delivered`
| :blogauthor:`2019-01-25 by Philip Papadopoulos`

Campus resource storage cluster :ref:`crsp` has been physically delivered to
UCI.  RCIC is currently working on configuration and acceptance testing.

We expect friendly users to have access near mid February.

Jan 24
^^^^^^

| :blogtitle:`HPC3 Request for Proposals Sent to Vendors`
| :blogauthor:`2019-01-24 by Philip Papadopoulos`

Using standard UCI Procurement processes, the formal RFP for HPC3 has 
been made public to vendors.  Responses are expected February 1, 2019.

The RFP is requesting bids for two sub-clusters that will be interconnected 
via Infiniband and 10 Gigabit Ethernet:

- 12-node, 4 NVidia V100 GPUs per node, minimum of 32 cores/node
- 36-node, CPU cluster, minimum of 32 cores/node


.. _news 2017:

2017 
-----

Oct 10
^^^^^^

| :blogtitle:`RCIC Joins the Coalition for Academic Scientific Computation (CASC)`
| :blogauthor:`2017-10-10 by Allen Schiano`

The UCI Research Cyberinfrastructure Center has been accepted as a member of the 
nation-wide Coalition for Academic Computing (CASC). 

As described in the CASC website (casc.org):
  Founded in 1989, the Coalition for Academic Scientific Computation (CASC) is an 
  educational nonprofit 501(c)(3) organization with 86 member institutions 
  representing many of the nation's most forward thinking universities and computing centers.
  CASC is dedicated to advocating the use of the most advanced computing technology to 
  accelerate scientific discovery for national competitiveness, global security, and 
  economic success, as well as develop a diverse and well-prepared 21st century workforce.

CASC's mission parallels the RCIC's mission:
  * disseminate information about the value of high performance computing and advanced communications technologies
  * provide an *expert resource* for the Executive Office of the President, the Congress, and government agencies
  * facilitate information exchange within the academic scientific computation and communication community

UCI joins UCLA, UC Berkeley, the Lawrence Berkeley National Laboratory, 
and UCSD's San Diego Supercomputing Center as UC members of this prestigious nationwide group.
