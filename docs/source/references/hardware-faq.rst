.. _hardware faq:

Hardware FAQ 
============

Purchasing
----------

1. :bluelight:`What does hardware purchase get me?`

   1. :underline:`A larger bank of core hours` RCIC does not allocate more core hours than the cluster can physically deliver.
      When you add hardware, you expand the capacity of the system.
   2. :underline:`Hardware hours are added to your no-cost allocation`
   3. :underline:`Consuming your core-hours does not have to be 7x24` Idle private hardware represents never-to-recovered lost
      computing capacity.  Your bank of hours can instead be spent in bursts.
   4. :underline:`The least-expensive way to add a large number of core hours`
      Using 48-core nodes and 5 year warranty ~ 2.4 Million core hours 
      would be credited over 6 years. At $11.5K (node, tax, integration),
      this is roughly $0.005/core-hour.

   Using UCI-purchased hardware as an effective buffer and a no over-allocation
   policy, if all node owners utilized 100% of their allocation, there would
   still be about 20% of the cores unused.

2. :bluelight:`Should I purchase hardware? Buy cores? Neither?`

   Our goal is to enable you to make efficient use of your grant or other funds.
   RCIC recovers only the cost of hardware through its recharges. We are fortunate at UCI,
   the people cost of administration is supported centrally by campus. Here's is advice
   that we believe is universally applicable:

   1. :underline:`Prioritize your jobs` into ones that can be killed (and hence start over from 
      the beginning) and those that are more important. Use the free queues for your
      lower priority work and your allocation for higher-priority work.
      This will allow you to make effective use of the free queues.
   2. :underline:`Analyze your own usage` to get a good feel for how long a typical job takes
      and how much memory it requires.  For, single node jobs, use the command
      ``seff -j JOBID`` to easily find out this information after a job has run.
      Note, ``seff`` doesn't produce accurate results for multi-node jobs.
   3. :underline:`Estimate how much computing time you need in the allocated (non-killable) category`.
      A typical 40-core node will credit your account with about 330,000 core hours/year.
      Determine how many whole nodes you need to purchase to meet your computing requirements
   4. :underline:`If your estimate is less than 200K core hours/year`,  you can mostly rely upon 
      the no-cost cycles (reminder, this allocation is per research lab, not per user).
   5. :underline:`If your estimate is more than 200K core hours/year but less than 400K core hours`,
      core-hour purchase will likely be the most cost-effective way to expand usage
   6. :underline:`If your estimate is more than 400K core hours/year`, then purchasing hardware is the
      least expensive way to obtain additional hours.
   7. :underline:`You should only purchase what your lab needs`.
 
3. :bluelight:`Saving or Spending core hours?`

   :underline:`You should spend your allocation`! Core-hour accounting has many positives,
   but to work effectively, the UCI community as a whole needs to spend their
   allocations at a regular rate.

.. _node type:

Node type
---------

There are two node types to consider. We give "ballpark" cost estimates that
should be sufficient for rough budgeting. Actual costs are commodity market-driven
and require firm quotes from vendors. As time progresses, the RCIC executive/advisory
committees will evaluate other hardware configurations.

*CPU-only nodes*
  Dual-Socket, Intel Ice Lake |xeon-6336y|_ processor, 256GB Memory, EDR Infiniband, 10GbE Ethernet. Dell or HPE. 
  Price: ~$10000.00.

  .. table:: **Standard Compute Node Sample Configuration**
     :class: noscroll-table

     +-----------------------+------------------------------------------------------------+
     | Component             |      Description                                           |
     +=======================+============================================================+
     | Chassis               | |dell-r650|_  1RU with Dual Power Supplies                 |
     +-----------------------+------------------------------------------------------------+
     | Processor x 2         | |xeon-6336y|_ 24-core `CPU@2.4GHz` 48 Cores total          |
     +-----------------------+------------------------------------------------------------+
     | Memory                | 16 x 16GB ECC 3200MT/s (DDR4-3200) RDIMMs Dual Rank        |
     +-----------------------+------------------------------------------------------------+
     | Interconnect          | |mellanox|_  ConnectX-6 HDR Infiniband                     |
     +-----------------------+------------------------------------------------------------+
     | Scratch Disk          | 1.92 TB NVMe Solid State Drive                             |
     +-----------------------+------------------------------------------------------------+
     | Operating System Disk | 480 GB  mixed-use SATA Solid-State Drive                   |
     +-----------------------+------------------------------------------------------------+
     | Ethernet              | 10Gb/s SFP+                                                |
     +-----------------------+------------------------------------------------------------+
     | Warranty              | 5-year Next-Business Day                                   |
     +-----------------------+------------------------------------------------------------+

*GPU-Enabled Nodes*
  Dell (or similar) chassis, 2RU, |dell-r750xa|_ with up to four A30 GPUs/chassis. Price: ~$35000

  .. table:: **Standard GPU Node Sample Configuration**
     :class: noscroll-table

     +-----------------------+------------------------------------------------------------+
     | Component             |      Description                                           |
     +=======================+============================================================+
     | Chassis               | |dell-r750xa|_  2RU with Dual 2KW Power Supplies           |
     +-----------------------+------------------------------------------------------------+
     | Processor x 2         | |xeon-6326|_ 16-core `CPU@2.4GHz` 32 Cores total           |
     +-----------------------+------------------------------------------------------------+
     | GPUs x 4              | |nvidia-a30|_  24GB HBM, 933GB/s, 9216 CUDA Cores          |
     +-----------------------+------------------------------------------------------------+
     | Memory                | 16 x 16GB ECC 3200MT/s (DDR4-3200) RDIMMs Dual Rank        |
     +-----------------------+------------------------------------------------------------+
     | Interconnect          | |mellanox|_  ConnectX-6 HDR Infiniband                     |
     +-----------------------+------------------------------------------------------------+
     | Scratch Disk          | 1.92 TB NVMe Solid State Drive                             |
     +-----------------------+------------------------------------------------------------+
     | Operating System Disk | 480 GB  mixed-use SATA Solid-State Drive                   |
     +-----------------------+------------------------------------------------------------+
     | Ethernet              | 10Gb/s SFP+                                                |
     +-----------------------+------------------------------------------------------------+
     | Warranty              | 5-year Next-Business Day                                   |
     +-----------------------+------------------------------------------------------------+


*Options beyond baseline Configs*
  Technology is always changing.  Users may opt for additional memory per node (512GB, 1024GB) at additional cost.
  Please note that you are not guaranteed access to your node, but higher core count nodes give you more core credits.
  We also recognize that different grant budgets sometimes come with special constraints. RCIC will work with you during purchase.

  .. table:: **Additional Configuration**
     :class: noscroll-table

     +------------------------------+-----------------------------------------------------------------------------------------+
     | Option                       |      Description                                                                        |
     +==============================+=========================================================================================+
     | Integration Fee              | $1000/node. This is a one-time cost that covers connection to three different networks. |
     +------------------------------+-----------------------------------------------------------------------------------------+
     | Ongoing Administrative Costs | None                                                                                    |
     +------------------------------+-----------------------------------------------------------------------------------------+
     | Lifetime in Cluster          | Period of Warranty + 1year. Most CPU nodes are purchased with 5 year warranties         |
     |                              | (a six year lifetime in the cluster). GPU nodes with 4 or 5 year warranties. If a       |
     |                              | node breaks in the extension year and isn't easily repairable, it will be removed.      |
     +------------------------------+-----------------------------------------------------------------------------------------+
     | Disposition after Lifetime   | If the hardware is still viable and space/power are not a concern, the node may run     |
     |                              | longer but *will not generate core-hour credits* for the original purchaser. In         |
     |                              | essence, it would add capacity to the "free queues".                                    |
     +------------------------------+-----------------------------------------------------------------------------------------+

.. _network type:

Network type
------------

* **The 10Gbit/s Ethernet network** is the provisioning and control network to access Ethernet-only resources.
* **The  100Gbit/s** `ConnectX-5 <https://www.mellanox.com/files/doc-2020/pb-connectx-5-vpi-card.pdf>`_  **EDR Infiniband**
  is a 2-level `Clos-Topology <https://web.stanford.edu/class/ee384y/Handouts/clos_networks.pdf>`_  with a maximum
  8:1 oversubscription: Nodes in the same rack (max 32) are connected to a full-bisection, 36-port Infiniband switch.
  Each lower-level switch is connected to two root-level switches with two links/switch.
  The subnet manager is `opensm <https://linux.die.net/man/8/opensm>`_ with LMC (Lid Mask Control) set to 2 for multi-path diversity.

.. |dell-r650| replace:: Dell R650
.. _`dell-r650`: https://www.dell.com/en-us/work/shop/povw/poweredge-r650

.. |xeon-6336y| replace:: Intel Xeon Gold 6336Y 
.. _`xeon-6336y`: https://www.intel.com/content/www/us/en/products/sku/215280/intel-xeon-gold-6336y-processor-36m-cache-2-40-ghz/specifications.html

.. |mellanox| replace:: 100Gb/s Mellanox 
.. _`mellanox`: https://www.nvidia.com/en-us/networking/ethernet/connectx-6/
     

.. |dell-r750xa| replace:: Dell R750xa
.. _`dell-r750xa`: http://www.dell.com/en-us/work/shop/povw/poweredge-r750xa

.. |xeon-6326| replace:: Intel Xeon Gold 6326 
.. _`xeon-6326`: https://www.intel.com/content/www/us/en/products/sku/215274/intel-xeon-gold-6326-processor-24m-cache-2-90-ghz/specifications.html

.. |nvidia-a30| replace:: Nvidia A30
.. _`nvidia-a30`: https://www.nvidia.com/en-us/data-center/products/a30-gpu/
