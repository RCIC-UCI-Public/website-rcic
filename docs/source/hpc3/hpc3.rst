.. _hpc3:

Overview
========

HPC3 is one of UCI's shared-computing cluster that
expands upon the condo-style model of `GreenPlanet <https://ps.uci.edu/greenplanet/>`_
and the now-retired HPC clusters. 
Condo clusters have one model of expanding capacity - users purchase physical hardware.

**HPC3 supports expansion through hardware purchase and enables additional capacity via:**
  | :ref:`no-cost allocations` allocations granting of cycles from UCI-purchased hardware
  | :ref:`recharge allocations` purchase allocations of cycles by the core-hour

The most significant change from a condo-only is that :underline:`owner-dedicated queues no longer exist`.
Instead, researchers receive an allocation of available core-hours that are deposited into a "bank account" [1]_ 

A bank account can have multiple authorized users and allocated jobs are charged against the bank.
For node owners, the theoretical capacity of their hardware is converted into available core hours
and deposited into the bank account in addition to any granted or purchased hours.

The bank represents computing units (e.g. core-hour or GPU-hour) and logically functions
as a :underline:`prepaid account`.  Accounts have owners, and they can designate others 
who can charge to their account.  A "bank" can be filled in a variety of ways:

:Granted:
  UCI core funds have purchased (and will likely add more) nodes that create the capacity for granted hours.

:Converted:
  Each node has a maximum delivery of **core-hours = cores * 8760 hours/year**.
  For node owners, 95% of this theoretical maximum is deposited annually [2]_ 
  into an account for their use on any resource in the cluster.

:Purchased:
  UCI researchers can purchase prepaid time to fill/augment their banks.


**Quick Guide to Most Common Information Requests**
  | What are :ref:`allocations` in detail
  | How does :ref:`reallocation` work
  | How to use :ref:`recharge allocations` for buying core-hours or hardware
  | Hardware :ref:`specs` 

TODO  rm next lines:
  | :ref:`reference guide` HPC3 Reference Guide Jump off point for Quick Start
  | :ref:`ssh guide` Logging into HPC3. Sub guide to using ssh-agent effectively
  | :ref:`slurm`  How to use the Job Scheduler

.. _hpc3 goals:

Goals
-----

The HPC3 planning committee crafted policy guidelines to meet the following goals:

- Enable access to a larger compute/analysis system than could be reasonably afforded on an individual lab basis
- Enable access to specialized nodes (e.g. large memory, GPU)
- Foster a growing community across UCI to use scalable computing (:term:`HPC` and :term:`HTC`)
  for their scientific research and teaching
- Provide a well-managed software environment that underpins a reproducible scientific instrument. 
  Fit seamlessly into the progression of:

  :guilabel:`desktop` → :guilabel:`lab cluster` → :guilabel:`campus` → :guilabel:`national` -> :guilabel:`commercial cloud`
- Enable construction of more-secure research environments

.. _hpc3 policies:

Policies
--------
HPC3 policies are needed to primarily address issues such

* How is *contention* for acquiring and using resources addressed?
* How does one balance high utilization against wait times for jobs to start ?
* What are principles to enable and support long-running jobs
* Are there ways to support priority boosting for jobs with specific deadlines (e.g. grants and publications)
* How can groups that contributed resources be ensured their fair share?

The questions above have no single right answer and this means that any policy employed on HPC3 must be tuned to
balance the wide range of needs specifically for the UCI research community.  It also means, that any implemented
policy must be fluid and flexible.

The `Research Cyberinfrastructure Vision Document <http://sites.uci.edu/rci/files/2016/03/A-Vision-for-RCI-at-UCI-Document-and-Appendices.pdf>`_
(`cached </_static/A-Vision-for-RCI-at-UCI-Document-and-Appendices.pdf>`_) provides the rationale for 
what Research Cyberinfrastructure should be and some new features that need to be implemented.
This document was the output of a faculty-lead committee, who completed their work in 2016.

In 2018, the RCIC began the process of crafting a 
`policy/usage document <https://docs.google.com/document/d/1fqTC5tc29JK2PfIATPqnUfwo3SooLBCEMzogbKBjslU/edit>`_
that could provide the framework for creating HPC3 and the principles by which it would run.
The HPC3 subcommittee of the RCIC advisory committee edited and refined the initial version.
Going forward, this document will continually be updated to reflect adjustments and refinements.

An `HPC3 executive summary </_static/HPC-Policy-Executive-Summary.pdf>`_ and a longer draft policy document
can be consulted for a more in-depth treatment. 

.. _hpc3 sharing:

Fair Sharing
------------

At the heart of HPC3 sharing
is :underline:`core-hour and GPU-hour accounting` where jobs are classified as either:

:Accounted:
  time used by a job is tracked against a "bank" of hours

:Free:
  jobs may be killed at any time to make room for accounted jobs.

.. note:: The fundamental difference between accounted and free is that an accounted 
          job may NOT be suspended or killed in favor of another job. Once an
          accounted job is allocated resources, it will not be pre-empted.

Accounted jobs simply says that HPC3 will be able to track usage of the cluster and the overall usage is in proportion
to how much a particular research program has contributed to the physical infrastructure. 

For example, a research group that has purchased 10 nodes will have over each year: 
  1. About 10 nodes-worth of accounted jobs to run on the cluster.
  2. Nothing limits that group to just their 10 nodes. This means that a group can access a larger number of nodes in bursts.
  3. No *guarantee* is given that they can they can have instantaneous access to their particular purchased nodes in the cluster.
     This means that there may be times of contention where a node owner may have to wait.

This combination supports the goal of access to a larger resource:
  :bluelight:`When an accounted job is running on a larger number of nodes than purchased,
  that job cannot be killed/suspended`.

The principles can be coded into "queuing policy" to achieve reasonable balance of access,
stability and other qualities.  Some of the sharing principles include:

* Small core-count, short-duration (e.g. debugging) jobs should have little to no waiting time
* Very large numbers of jobs submitted at one time  by some users should not result in other
  users waiting for all those jobs to complete (HPC3 is not first-in, first-out)
* Once a job has started, predictability of run time is highly-desirable
* Free (non-accounted) jobs should still be possible (and encouraged) if their impact to accounted jobs is minimal

.. [1] Available balance is reset every six months and is a combination of granted, purchased, equivalent hours of condo hardware.
.. [2] Account balances are reallocated every 6 months. At the time of re-allocation, any unused hours are forfeit.
