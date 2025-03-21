.. _allocations:

Resource Allocations
====================

.. contents::
   :local:

Introduction
------------

RCIC resources are funded and operated under a `shared financial model of
no-cost and recharge (pi-funded) allocations`.

**Every user**
  :ref:`no-cost allocations` :red:`one time 1000 core-hour allocation`. This allocation
  provides baseline level of computing cycles and is required to allow 
  users to access the Slurm `free` queues. It enables users who are not affiliated with 
  any research program to have meaningful access to HPC3. 
  Most users should use lab accounts instead of this one-time allocation.

**Faculty**
  | Faculty [#]_ allocations are *PI-centered* but the owners can  grant access
  | to their allocations to students, postdocs, and other faculty members.
  | :red:`Allocations can not be combined into larger group or center accounts.`

  Faculty UCI researchers can have two types of allocations: 

  .. table::
     :class: noscroll-table:

     +----------------------------------------------------------------------------------------------------------+
     |  :ref:`no-cost allocations` allocations                                                                  |
     |                                                                                                          |
     |    | Can be requested to baseline levels of:                                                             |
     |    |   * **Computing cycles**: are reallocated every 6 months. See :ref:`reallocation` for details.      |
     |    |   * **Campus Research Storage** (:term:`CRSP`): 1TB per researcher.                                 |
     +----------------------------------------------------------------------------------------------------------+
     |  :ref:`recharge allocations` allocations                                                                 |
     |                                                                                                          |
     |    | Are used when the baseline is insufficient for a particular lab.                                    |
     |    | Researchers can purchase additional capacity using grant or other funds.                            |
     |    | The recharge (PI-funded) allocations are available for:                                             |
     |    |   *  :ref:`buy computing`                                                                           |
     |    |   *  :ref:`CRSP storage <buy crsp>`                                                                 |
     |    |   *  :ref:`DFS storage <buy dfs>`                                                                   |
     +----------------------------------------------------------------------------------------------------------+

.. _no-cost allocations:

No-cost
-------

In general, the cost of administration of RCIC resources is covered in RCIC's annual budget. 
RCIC is funded through central campus to provide a baseline allocations of centralized, research computing
and data services.  

.. table:: **Summary of no-cost baseline allocations for campus researchers (faculty)**
   :class: noscroll-table

   +------------------+------------------------+--------------------+------------------+-----------------+
   | Capability       | No-cost allocation     | How often          | How to expand    | Expansion costs |
   +==================+========================+====================+==================+=================+
   | **HPC3**         | 100000 [2]_ core-hrs   | Every 6 months     | Cycle Purchase   | $.01/core-hr    |
   |                  |                        |                    |                  |                 |
   | CPU hours        |                        |                    | Hardware Purchase| ~$15K/node      | 
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **HPC3**         | 1000 [3]_  GPU-hrs     | Every 6 months     | Cycle Purchase   | $.32/core-hr    |
   |                  |                        |                    |                  |                 |
   | GPU hours        |                        |                    | Hardware Purchase| ~$47K/node      |
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **CRSP storage** | 1 TB                   |  Never Expires     | TB/year          | $50/TB/Year     |
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **DFS storage**  | N/A                    |  N/A               | TB/ 5 years      | $100/TB/5 Years |
   +------------------+------------------------+--------------------+------------------+-----------------+

.. table:: **Summary of no-cost allocations for every user**
   :class: noscroll-table

   +------------------+------------------------+--------------------+------------------+-----------------+
   | Capability       | No-cost allocation     | How often          | How to expand    | Expansion costs |
   +==================+========================+====================+==================+=================+
   | **HPC3**         | 1000 core-hrs          | One time           | N/A              | N/A             |
   |                  |                        |                    |                  |                 |
   | CPU hours        |                        | allocation         |                  |                 |
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **HOME storage** | 50 GB                  | Never Expires [4]_ | N/A              | N/A             |
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **DFS storage**  | 1 TB                   | Never Expires [4]_ | N/A              | N/A             |
   +------------------+------------------------+--------------------+------------------+-----------------+


.. _recharge allocations:

Recharge
--------

When research program needs exceed this baseline, additional capacity can be purchased through recharge. 
It should be noted, that rates apply only to UCI researchers [1]_ (faculty, research faculty, research staff).

The recharge tables below provides more details on costs and commitment.
Proposed rates for CRSP and CPU/GPU hours are in the process of being approved by the UCI recharge
rate review process. 

.. TODO (leave?) These have not been finalized.

.. _recharge storage rates:

.. table:: **Storage Related Recharges**
   :class: recharge-table

   +------------+----------------------+-------------------+-----------------------------------------------------+
   | Item       |  Rate                | Commitment        |  Notes                                              |
   +============+======================+===================+=====================================================+
   | CRSP       | $50/TB/Year          |  Year             | Two-copy storage, available on campus network.      |
   |            |                      |                   | Daily Backups available on campus network/VPN       |
   +------------+----------------------+-------------------+-----------------------------------------------------+
   | DFS        | $100/TB/5 Years      | 5 Years           | Single copy, high-performance storage.              |
   |            |                      |                   | Daily backups are accessible only from HPC3         |
   +------------+----------------------+-------------------+-----------------------------------------------------+
   | Selective  | $100/TB/5 Years      | 5 Years           | Second copy of user-selected                        |
   | backup     |                      |                   | file systems on HPC3.                               |
   +------------+----------------------+-------------------+-----------------------------------------------------+

.. _recharge rates:

.. table:: **HPC3 Computing Related Recharges**
   :class: recharge-table

   +---------------+---------------------+--------------------+-------------------------------------------------+
   | Item          | Rate                | Commitment         |  Notes                                          |
   +===============+=====================+====================+=================================================+
   | Server        | $1000               | One-time           | Researcher-owned server                         |
   | installation  |                     |                    | can be added to HPC3                            |
   +---------------+---------------------+--------------------+-------------------------------------------------+
   | Server        | ~$15K/CPU or        | Equipment warranty | Hardware purchases add capacity for the owner.  |
   | purchase      | ~$47K/CPU+GPU node  | plus 1 year        | Prices are estimates. Exact pricing depends on  |
   |               |                     |                    | node confdiguration and time of purchase.       |
   +---------------+---------------------+--------------------+-------------------------------------------------+
   | CPU hours     | $0.01/core-hour     | Minimum:           | Prepaid core-hours valid                        |
   |               |                     | 10000 core-hours   | for 1 year after purchase.                      |
   +---------------+---------------------+--------------------+-------------------------------------------------+
   | GPU hours     | $0.32/GPU-Hour      | Minimum:           | Prepaid GPU-hours valid                         |
   |               |                     | 250 GPU-hours      | for 1 year after purchase.                      |
   +---------------+---------------------+--------------------+-------------------------------------------------+


.. _buy allocation:

How to buy allocations 
----------------------

The recharge is billed annually via campus recharge and is computed on the basis of
recovering the cost of additional space (for CRSP and DFS storage). These campus funds pay for the people, the
baseline infrastructure, and vendor maintenance required to provide the robust infrastructure.

All allocation purchase requests need to be emailed by a PI to hpc-support@uci.edu telling us
what allocations are desired. Please see sections below for details. 

.. _buy computing:

Computing
^^^^^^^^^

| Computing allocation for *accounted jobs*  can be expanded through:
|   1. :ref:`buy core-hours` from RCIC.
|   2. :ref:`buy hardware`  that is placed into the cluster and converted into core-hours.

.. _buy core-hours:

Purchase core-hours
~~~~~~~~~~~~~~~~~~~

| Please send a request to hpc-support@uci.edu telling us:
|   1. Type of core-hours (CPU or GPU)
|   2. How many core-hours you need

Core-hour purchases a done through an MOU on a ``prepaid card basis``. 
RCIC does not post-bill for core hours and it is not possible to be surprised 
with a large bill at the end of a month. 

Prepaid core hours are intended to be used within one calendar year.
Unused prepaid hours are forfeit after 18 months. The current :ref:`recharge rates`
are computed to recover the cost of hardware over a 5 year period at 60% use.

.. _buy hardware:

Purchase hardware
~~~~~~~~~~~~~~~~~

:bluelight:`Hardware purchase process`
  **Hardware is purchased through RCIC and can be requested at any time**.
  When a large enough number of nodes have been requested
  (at least 4 CPU nodes and/or 1 GPU node), RCIC will obtain quote(s)
  from vendors for acceptable hardware.  Your source of funds (grant
  or other) is used to fund your share of the purchase. You can only
  purchase whole nodes, but you may use multiple sources of funds. In this
  model, we easily support two different faculty splitting the cost of a single node.

  | Hardware is commodity-based and subject to market variability, prices as of 1Q 2025:
  |     CPU nodes (48 cores) are approximately $15K.
  |     GPU-nodes (4 x NVIDIA L40S) are approximately $47K.

  .. warning:: You may not purchase hardware, send to the machine room, and then 
               expect RCIC to integrate this hardware into HPC3. Any hardware 
               purchased outside of the above process will not be integrated into HPC3
               nor will it be managed by RCIC.

:bluelight:`Outline of Purchase Process`
  1. Send a request to hpc-support@uci.edu indicating your interest in purchasing
     nodes (CPU or GPU and how many) and time frame.
  2. RCIC obtains quotes once enough requests have been aggregated.
  3. Upon your approval purchase is made and your funds are used at purchase time.
  4. $1000/node one-time integration fee is re-charged AFTER the hardware has arrived.

:bluelight:`Hardware that you purchase is converted to core-hours allocation`
  For example, a 48-core node can deliver:
        | :math:`8760 hours/year * 48 cores = 420,480 core hours/year`
        | At 95% this would become a 399,456 core-hour (SU) credit to a CPU Slurm Account

  For example, a 32-core, 4GPU  node can deliver:
        | :math:`8760 hours/year * 32 cores = 280,320 core hours/year`
        | :math:`8760 hours/year * 4 GPUs * 32SUs/GPU = 1,121,280 GPU hours/year`
        | :math:`280,320 SU + 1,121,280 SU = 1,401,600 SU`
        | At 95% this would become a 1,331,520 SU credit to a GPU Slurm Account

        .. note:: | SUs (Service Units) are not convertible between GPU and CPU accounts.
                  | An hour of a GPU requires at least 2 CPU cores.
                  | Hence, the minimum charge for a single GPU is :math:`32 + 2 = 34 SUs/hour`. 

  **The conversion rate is 95% of the theoretical core hours your hardware could deliver in a year**:
     * The 95% factor accounts for usual annual downtime through scheduled and unscheduled maintenance.
     * The 50% of this credit is applied during the 6 month reallocation each year the 
       node is in the cluster (warranty period + year)

:bluelight:`Effective costs over 6 years for purchased hardware`
  Using the above estimated costs of $15K for CPU node and  $47K for a GPU node *and* consuming all SUs every 6
  month reallocation cycle the following cost estimates of core-hour cost and GPU-hour costs would be as follows: 

  .. _effective costs:

  .. table:: **HPC3 Effective Costs for CPU and GPU hours**

     +---------------------+-------------------------------------------------+-------------------+
     | Equivalence         |   Calculation                                   | Effective rate    |
     +=====================+=================================================+===================+
     | Core Hours          | :math:`$15000/(6 Yr * 399456 SU/yr)/1SU/hour`   | $0.0062/Core-hour |
     +---------------------+-------------------------------------------------+-------------------+
     | GPU Hours (2 cores) | :math:`$47000/(6 Yr * 1331520/SU/yr)/34SU/hour` | $0.20/GPU-hour    |
     +---------------------+-------------------------------------------------+-------------------+
     | GPU Hours (8 cores) | :math:`$47000/(6 Yr * 1331520/SU/yr)/40SU/hour` | $0.25/GPU-hour    |
     +---------------------+-------------------------------------------------+-------------------+

:bluelight:`Purchasing of nodes in HPC3 does NOT give you a "private" queue`
  This means that some of your jobs may have to wait for resources, but it also gives
  you non-preempt access a larger number of cores than purchased.  In the first
  1.5 years of HPC3 operation, owners rarely wait for long periods of time.


Please see :ref:`hardware faq` for additional info about hardware purchases. 

.. _buy crsp:

Purchase CRSP storage
^^^^^^^^^^^^^^^^^^^^^

| Please send a request to hpc-support@uci.edu telling us
|   1. How much CRSP space you need (TB)
|   2. For how long (years)

We will create an MOU and sent to the PI for signing and will ask for a recharge index.
Once a PI signs an MOU for the desired amount of storage, the allocation is created
on the CRSP system.

.. _buy dfs:

Purchase DFS storage
^^^^^^^^^^^^^^^^^^^^

| Please send a request to hpc-support@uci.edu telling us
|   1. How much DFS space you need (TB)
|   2. If this is your first DFS purchase, then the initial term is 5 years.
|   3. If you have existing DFS quota, then then additional quota is priced at $20/TB/Year.  The PI has the choice of a) extending existing quota 5 years or b) Setting the expiration data of new quota to co-terminate with the existing quota end-date

We will create an MOU and sent to the PI for signing and will ask for a recharge account.
Once a PI signs an MOU for the desired amount of storage, the allocation is created
on one of the DFS systems.


.. [#] Ladder-rank faculty and any person who can serve as PI or Co-PI in extramural grants
.. [#] Max allocation as `available` hours to be used during the next 6 month
       interval. Allocation is adjusted dependent on actual use of core-hours.  Applies to faculty accounts.
.. [#] Because of limited physical resources, PI must specifically request allocation for GPU-hours.
       Applies to faculty accounts. 
.. [#] When a user no longer has an active UCInetID, files are removed.

