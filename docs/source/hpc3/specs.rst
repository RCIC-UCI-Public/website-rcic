.. _specs:

Specs
=====

.. _hardware configuration:

Hardware configuration
----------------------

HPC3 had an initial procurement phase through an :term:`RFP` process. After evaluation,
`Hewlett Packard Enterprise <http://www.hpe.com>`_ was awarded the bid. Since award,
additional purchases have been made to bring the cluster to its current configuration.

The system started as a 4000 core system when first constructed in June 2020.
It has expanded several times with nodes purchased by UCI and faculty.

As of August 2024, the following describes the cluster:
  * 235 Batch-accessible nodes including:

    * 14 nodes with 4 Nvidia V100 (16GB) GPUs
    * 18 nodes with 4 Nvidia A30 (24GB) GPUs
    * 4 nodes with 2 Nvidia A100 (80GB) GPUs
  * 10208 total cores (1256 AMD Epyc and 8952 Intel)
  * 67,451 GB Aggregate Memory
  * Three load-balanced login nodes
  * 96% nodes (226/225) at 100Gb/s EDR Infiniband

HPC3 heterogeneous hardware has the following unique configurations with the most common
configurations shown first.

.. Generate the following table (formatting is going to be table-like) with
.. sinfo -S  '-R -D c' -p standard,highmem,hugemem,maxmem,gpu,standard-hbm,gpu-hugemem -o "   | %4D | %4c | %9m | %38f | %12G | " -e  | sed 's/(null)/      /'
.. edit the final

.. table::
   :class: noscroll-table sortable

   +-------+------+--------+-------------------------------------------+------------+
   | Nodes | CPUs | Memory | Available features                        | GPU        |
   |       |      | (GB)   |                                           | type:number|
   +=======+======+========+===========================================+============+
   | 3     | 80   | 127    | intel,avx512,mlx5_ib,nvme,fastscratch,hbm |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 65    | 40   | 192    | intel,avx512,mlx5_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 36    | 48   | 191    | intel,avx512,mlx5_ib,nvme,fastscratch     |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 32    | 48   | 191    | intel,avx512,mlx5_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 16    | 64   | 515    | amd,epyc,epyc7601,mlx5_ib                 |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 6     | 48   | 256    | intel,avx512,mlx5_ib,nvme,fastscratch     |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 3     | 48   | 256    | intel,avx512,mlx5_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 2     | 28   | 257    | intel,avx512,mlx4_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 2     | 36   | 515    | intel,mlx4_ib                             |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 24   | 515    | intel,mlx4_ib                             |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 36   | 515    | intel,mlx5_ib                             |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 44   | 515    | intel,mlx4_ib                             |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 64   | 515    | amd,epyc,epyc7551,mlx4_ib                 |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 64   | 515    | amd,epyc,epyc7601,mlx4_ib                 |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 2     | 64   | 2063   | intel,avx512,mlx5_ib,nvme,fastscratch     |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 40   | 1547   | intel,mlx4_ib                             |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 4     | 40   | 773    | intel,avx512,mlx5_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 2     | 48   | 772    | intel,avx512,mlx5_ib,nvme,fastscratch     |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 15    | 40   | 386    | intel,avx512,mlx5_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 6     | 48   | 384    | intel,avx512,mlx5_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 48   | 385    | intel,avx512,mlx5_ib                      |            |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 64   | 3095   | intel,avx512,mlx5_ib,nvme,fastscratch     | gpu:A30:4  |
   +-------+------+--------+-------------------------------------------+------------+
   | 15    | 32   | 256    | intel,avx512,mlx5_ib,nvme,fastscratch     | gpu:A30:4  |
   +-------+------+--------+-------------------------------------------+------------+
   | 13    | 40   | 192    | intel,avx512,mlx5_ib                      | gpu:V100:4 |
   +-------+------+--------+-------------------------------------------+------------+
   | 4     | 32   | 256    | intel,avx512,mlx5_ib,nvme,fastscratch     | gpu:A100:2 |
   +-------+------+--------+-------------------------------------------+------------+
   | 2     | 32   | 257    | intel,avx512,mlx5_ib,nvme,fastscratch     | gpu:A30:4  |
   +-------+------+--------+-------------------------------------------+------------+
   | 1     | 40   | 386    | intel,avx512,mlx5_ib                      | gpu:V100:4 |
   +-------+------+--------+-------------------------------------------+------------+

.. note:: Features and GPU type and number (or GRES, e.g. Generic RESources)
          are resource specifications that can be requested in Slurm job submissions.

.. _networking:

Networking
----------

HPC3 has the following  networks attached to each node:

* 10Gbit/s  Ethernet. This is the provisioning and control network to access Ethernet-only resources.
* 100Gbit/s `ConnectX-5 <https://www.mellanox.com/files/doc-2020/pb-connectx-5-vpi-card.pdf>`_  EDR Infiniband

See more info in :ref:`network type`.

.. _nodes type:

Node Type
---------

HPC3 nodes have minimums of 56Gb/s Infiniband (most nodes are 100Gb/s), 4GB/core, and AVX-2 capability.
For additional info see :ref:`hardware faq`.

CPU only nodes
^^^^^^^^^^^^^^

Most-common configurations:

**Chassis**:

  | 1. HP
  |   HPE `Apollo 2000 Gen 10 <https://h20195.www2.hpe.com/v2/GetPDF.aspx/4AA4-8164ENW.pdf>`_.  2RU with 4 nodes/chassis
  |   Dual-Socket, `Intel Skylake 6148 <https://ark.intel.com/content/www/us/en/ark/products/120489/intel-xeon-gold-6148-processor-27-5m-cache-2-40-ghz.html>`_ 20-core `CPU@2.4GHz`. 40 Cores total.

  | 2. Dell Cascade Lake
  |   Dell `R640 1U Server <https://www.dell.com/en-us/work/shop/productdetailstxn/poweredge-r640>`_
  |   Dual-Socket, `Intel Cascade Lake 6240R <https://ark.intel.com/content/www/us/en/ark/products/199343/intel-xeon-gold-6240r-processor-35-75m-cache-2-40-ghz.html>`_ 24-core `CPU@2.4GHz`. 48 Cores total.

  | 3. Dell Ice Lake
  |   Dell `R650 1U Server <https://www.dell.com/en-us/work/shop/productdetailstxn/poweredge-r650>`_
  |   Dual-Socket, `Intel Ice Lake 6336Y <https://www.intel.com/content/www/us/en/products/sku/215280/intel-xeon-gold-6336y-processor-36m-cache-2-40-ghz/specifications.html>`_ 24-core `CPU@2.4GHz`. 48 Cores total.
  |  256GB DDR4, ECC Memory

**Interconnect**:

  Each node is connected to Ethernet and Infiniband  networks. See
  :ref:`networking` for details.


**Memory**:

  | All memory is DDR4, EEC, most common capacity is 192GB.
  | Available memory in GB:

  === === === ==== === ==== ==== ====
  192 256 384 512  768 1536 2048 3072
  === === === ==== === ==== ==== ====

GPU-Enabled Nodes
^^^^^^^^^^^^^^^^^

A node can have up to 4 GPUs of the same type.
CPU, Network, Memory, SSD  are identical to CPU only nodes.
Currently available configurations have high-bandwidth memory and PCIe connections.

**Chassis**:

  | HPE `DL380 Gen 10 <https://buy.hpe.com/au/en/servers/rack-servers/proliant-dl300-servers/proliant-dl380-server/hpe-proliant-dl380-gen10-server/p/1010026818>`_ chassis. 2RU. Up to 4 GPUs/chassis.

**GPU**:

  | Qty 4 Nvidia `V100 <https://www.nvidia.com/en-us/data-center/v100/>`_ GPU, 16GB memory
  | Qty 4 Nvidia A30 GPU, 24GB memory
  | Qty 2 Nvidia A100 GPU, 80GB memory

.. _support nodes:

Support Nodes
^^^^^^^^^^^^^

Support nodes are specialized nodes that provide very specific services:

.. table::
   :class: noscroll-table

   +---------------+----------+---------------------------------------------------------------+
   | Type          | How many | Provided Services                                             |
   +===============+==========+===============================================================+
   | Login nodes   | 3        | Point of entry  to the cluster.                               |
   |               |          | Have the same CPU, Network, Memory configuration as CPU nodes.|
   +---------------+----------+---------------------------------------------------------------+
   | Slurm server  | 1        | Slurm scheduler                                               |
   +---------------+----------+---------------------------------------------------------------+
   | Provisioning  | 1        | Management node                                               |
   +---------------+----------+---------------------------------------------------------------+
   | Firewall      | 4        | `PFSense <https://www.pfsense.org/>`_ security                |
   +---------------+----------+---------------------------------------------------------------+
   | NFS server    | 1        | Home area with `ZFS <https://zfsonlinux.org/>`_               |
   |               |          | as the underlying file system                                 |
   +---------------+----------+---------------------------------------------------------------+

.. _node details:

Node Details
------------

HPC3 is a heterogeneous cluster with several CPU types, memory footprints, Infiniband revisions.
All CPUs in HPC3 have the following *minimum requirements*:

:*AVX support*:
 AVX2
:*Cores/platform*:
 24
:*Memory/core*:
 4GB
:*IB Technology*:
 FDR (Fourteen Data Rate)

`Ganglia <http://www.ganglia.org>`_ provides real time high-level `view of
HPC3 utilization <https://hpc3.rcic.uci.edu/ganglia>`_.
You must be on the UCI/VPN Network for this link to work.

Most nodes in HPC3 have at least 40 cores/node.

You may download node details info as the `CVS file </_static/nodes.csv>`_
or browse the table below.

Click on the column header for sorting.

.. csv-table:: Nodes info updated :blogauthor:`20 Aug 2024`.
   :class: noscroll-table sortable
   :file: ../_static/nodes.csv
   :widths: 5,5,18,20,15,22,10,5
   :header-rows: 1

