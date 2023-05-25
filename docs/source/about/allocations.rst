.. _allocations:

Baseline Allocations
====================

UCI has purchased both CPU and GPU nodes hardware as part of HPC3. Annual funds are used to add to this
resource enabling RCIC to provide no-cost allocations to a larger fraction of the UCI research community.

RCIC resources are funded and operated under a `shared financial model of
no-cost and pi-funded allocations`.

**Faculty**
  - :ref:`no-cost allocations`: UCI researchers [#]_ may request no-cost allocations to baseline
    levels of computing cycles and campus research storage (:term:`CRSP`). 
    Computing cycles are  refilled (re-allocated) on a semi-annual 
    (every 6 months). Re-allocation is based upon a lab’s previous
    6 month utilization and available hours on UCI-purchased hardware. 

    **Faculty allocations are PI-centered** but the researcher can share their allocation 
    with their students, postdocs, and other researchers.

    .. note:: Allocations can not be combined into larger group or `center` accounts.

  - :ref:`pi-funded allocations`:  When the baseline is insufficient for a particular lab, researchers 
    can use  pi-funded allocations (<</hpc3/hpc3-expansion.txt#,_computing_>>,
    and purchase additional capacity using grant or other funds.  
    <</storage/index.txt#,_cluster storage>>, <<crsp/index.txt#,_campus research storage>>) when needed.

**Every user**
  is given a no-cost ``one time 1000 core-hour allocation``. This allocations
  provides baseline level of computing cycles and is required to allow 
  users to access the `free` queues. It enables users who are not affiliated with 
  any research program to have meaningful access to HPC3. 
  Most users should use lab accounts instead of this one-time allocation.

.. _no-cost allocations:

No-cost allocations
--------------------

In general, the cost of administration of RCIC resources is covered in RCIC's annual budget. 
RCIC is funded through central campus to provide a baseline of centralized, research computing
and data services.  

.. table:: **Summary of no-cost allocations for campus researchers (faculty)**
   :class: noscroll-table

   +------------------+------------------------+--------------------+------------------+-----------------+
   | Capability       | No-cost allocation     | How often          | How to expand    | Expansion costs |
   +==================+========================+====================+==================+=================+
   | **HPC3**         | 100000 [2]_ core-hrs   | Every 6 months     | Cycle Purchase   | $.01/core-hr    |
   |                  |                        |                    |                  |                 |
   | CPU hours        |                        |                    | Hardware Purchase| ~$10K/node [5]_ | 
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **HPC3**         | 1000 [3]_  GPU-hrs     | Every 6 months     | Cycle Purchase   | $.01/core-hr    |
   |                  |                        |                    |                  |                 |
   | GPU hours        |                        |                    | Hardware Purchase| ~$35K/node [5]_ |
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **CRSP storage** | 1 TB                   |  Never Expires     | TB/year          | $60/TB/Year     |
   +------------------+------------------------+--------------------+------------------+-----------------+
   | **DFS storage**  | N/A                    |  N/A               | TB/ 5 years      | $100/TB/5 Years |
   +------------------+------------------------+--------------------+------------------+-----------------+

.. table:: **Summary of free allocations for every user**
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


.. _pi-funded allocations:

PI-funded extension
-------------------

When research program needs exceed this baseline, additional capacity can be purchased through recharge. 
It should be noted, that rates apply only to UCI researchers (faculty, research faculty, research staff).
The recharge tables below provides more details on costs and commitment:

.. _recharge rates:

.. table:: **Storage Related Recharges**
   :class: recharge-table

   +------------+----------------------+-------------------+-----------------------------------------------------+
   | Item       |  Rate                | Commitment        |  Notes                                              |
   +============+======================+===================+=====================================================+
   | CRSP       | $60/TB/Year [6]_     |  Year             | Two-copy storage, available on campus network.      |
   |            |                      |                   | Daily Backups available on campus network/VPN       |
   +------------+----------------------+-------------------+-----------------------------------------------------+
   | DFS        | $100/TB/5 Years      | 5 Years           | Single copy, high-performance storage.              |
   |            |                      |                   | Daily backups are accessible only from HPC3         |
   +------------+----------------------+-------------------+-----------------------------------------------------+
   | Selective  | $100/TB/5 Years      | 5 Years           | Second copy of user-selected                        |
   | backup     |                      |                   | file systems on HPC3.                               |
   +------------+----------------------+-------------------+-----------------------------------------------------+

.. table:: **HPC3 Computing Related Recharges**
   :class: recharge-table

   +----------------+------------------------------+-----------------------------+-----------------------------------------------------+
   | Item           |  Rate                        | Commitment                  |  Notes                                              |
   +================+==============================+=============================+=====================================================+
   | Server         | $1000                        | One-time                    | Researcher-owned server                             |
   | installation   |                              |                             | can be added to HPC3                                |
   +----------------+------------------------------+-----------------------------+-----------------------------------------------------+
   | Server         | $10K/CPU or                  | Equipment warranty          | Hardware purchases add                              |
   | purchase       | $35K/CPU+GPU node [5]_       | plus 1 year                 | capacity for the owner.                             |
   +----------------+------------------------------+-----------------------------+-----------------------------------------------------+
   | CPU hours      | $0.01/core-hour [6]_         | Minimum:                    | Prepaid core-hours valid                            |
   |                |                              | 10000 core-hours            | for 1 year after purchase.                          |
   +----------------+------------------------------+-----------------------------+-----------------------------------------------------+
   | GPU hours      | $0.32/GPU-Hour [6]_          | Minimum:                    | Prepaid GPU-hours valid                             |
   |                |                              | 250 GPU-hours               | for 1 year after purchase.                          |
   +----------------+------------------------------+-----------------------------+-----------------------------------------------------+


TODO


.. [#] Ladder-rank faculty and any person who can serve as PI or Co-PI in extramural grants
.. [#] Max allocation as `available` hours to be used during the next 6 month
       interval. Allocation is adjusted dependent on actual use of core-hours.  Applies to faculty accounts.
.. [#] Because of limited physical resources, PI must specifically request allocation for GPU-hours.
       Applies to faculty accounts. 
.. [#] When a user no longer has an active UCINetID, files are removed.
.. [#] These are rough estimates. Exact node pricing depends upon configuration and on the time of purchase.
.. [#] Proposed rates are in the process of being approved by the UCI recharge
       rate review process. These have not been finalized.

