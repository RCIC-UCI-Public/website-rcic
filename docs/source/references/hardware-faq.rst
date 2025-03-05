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
committees will evaluate other hardware configurations. These estimates are current as of January, 2025

*CPU-only nodes*
  Dual-Socket, Intel Ice Lake |xeon-6542y|_ processor, 256GB Memory, HDR InfiniBand, 10GbE Ethernet, local Solid-State
  Storage. Dell, Lenovo, or HPE. 
  Price: ~$15000.00.

  .. table:: **Standard Compute Node Sample Configuration**
     :class: noscroll-table

     +-----------------------+------------------------------------------------------------+
     | Component             |      Description                                           |
     +=======================+============================================================+
     | Chassis               | |dell-r660|_  1RU with Dual Power Supplies                 |
     +-----------------------+------------------------------------------------------------+
     | Processor x 2         | |xeon-6542y|_ 24-core `CPU@2.9GHz` 48 Cores total          |
     +-----------------------+------------------------------------------------------------+
     | Memory                | 16 x 16GB ECC 5600MT/s (DDR5-5600) RDIMMs Single Rank      |
     +-----------------------+------------------------------------------------------------+
     | Interconnect          | |mellanox|_  ConnectX-6 HDR Infiniband                     |
     +-----------------------+------------------------------------------------------------+
     | Scratch Disk          | 1.92 TB NVMe Solid State Drive                             |
     +-----------------------+------------------------------------------------------------+
     | Operating System Disk | 960 GB  NVMe Solid-State Drive                             |
     +-----------------------+------------------------------------------------------------+
     | Ethernet              | 10Gb/s SFP+                                                |
     +-----------------------+------------------------------------------------------------+
     | Warranty              | 5-year Next-Business Day                                   |
     +-----------------------+------------------------------------------------------------+

*GPU-Enabled Nodes*
  Dell (or similar) chassis, 2RU, |dell-r760xa|_ with up to four L40s GPUs/chassis. Price: ~$47000

  .. table:: **Standard GPU Node Sample Configuration**
     :class: noscroll-table

     +-----------------------+------------------------------------------------------------+
     | Component             |      Description                                           |
     +=======================+============================================================+
     | Chassis               | |dell-r760xa|_  2RU with Dual 2KW Power Supplies           |
     +-----------------------+------------------------------------------------------------+
     | Processor x 2         | |xeon-6526y|_ 16-core `CPU@2.8GHz` 32 Cores total          |
     +-----------------------+------------------------------------------------------------+
     | GPUs x 4              | |nvidia-l40s|_  48GB HBM, 864MB/s, 18176 CUDA Cores        |
     +-----------------------+------------------------------------------------------------+
     | Memory                | 16 x 16GB ECC 5600MT/s (DDR5-5600) RDIMMs Single Rank      |
     +-----------------------+------------------------------------------------------------+
     | Interconnect          | |mellanox|_  ConnectX-6 HDR Infiniband                     |
     +-----------------------+------------------------------------------------------------+
     | Scratch Disk          | 1.92 TB NVMe Solid State Drive                             |
     +-----------------------+------------------------------------------------------------+
     | Operating System Disk | 960 GB  NVMe Solid-State Drive                             |
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
* **The  100Gbit/s** `ConnectX-6 <https://www.nvidia.com/en-us/networking/ethernet/connectx-6/>`_  **HDR Infiniband**
  is a 2-level `Clos-Topology <https://web.stanford.edu/class/ee384y/Handouts/clos_networks.pdf>`_  with a maximum
  8:1 oversubscription: Nodes in the same rack (max 32) are connected to a full-bisection, 36-port InfiniBand switch.
  Each lower-level switch is connected to two root-level switches with two links/switch.
  The subnet manager is `opensm <https://linux.die.net/man/8/opensm>`_ with LMC (Lid Mask Control) set to 2 for multi-path diversity.

.. |dell-r660| replace:: Dell R660
.. _`dell-r660`: https://www.dell.com/en-us/work/shop/povw/poweredge-r660

.. |xeon-6542y| replace:: Intel Xeon Gold 6542Y 
.. _`xeon-6542y`: https://www.intel.com/content/www/us/en/products/sku/237559/intel-xeon-gold-6542y-processor-60m-cache-2-90-ghz/specifications.html

.. |mellanox| replace:: 100Gb/s Mellanox 
.. _`mellanox`: https://www.nvidia.com/en-us/networking/ethernet/connectx-6/
     

.. |dell-r760xa| replace:: Dell R760xa
.. _`dell-r760xa`: http://www.dell.com/en-us/work/shop/povw/poweredge-r760xa

.. |xeon-6526y| replace:: Intel Xeon Gold 6526Y
.. _`xeon-6526y`: https://www.intel.com/content/www/us/en/products/sku/237560/intel-xeon-gold-6526y-processor-37-5m-cache-2-80-ghz/specifications.html

.. |nvidia-l40s| replace:: Nvidia L40S 
.. _`nvidia-l40s`: https://resources.nvidia.com/en-us-l40s/l40s-datasheet-28413
