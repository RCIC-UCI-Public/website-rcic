.. _hpc3:

Overview
========

HPC3 is one of UCI's shared-computing cluster that
expands upon the condo-style model of `GreenPlanet <https://ps.uci.edu/greenplanet/>`_
and the now-retired HPC clusters.
Condo clusters have one model of expanding capacity - users purchase physical hardware.

**HPC3 supports capacity expansion via:**
  1. :ref:`buy hardware`
  #. :ref:`Recharge allocations <recharge allocations>`: purchase allocations of cycles by the core-hour
  #. :ref:`No-cost allocations <no-cost allocations>`: granting of cycles from UCI-purchased hardware.
     UCI has purchased both CPU and GPU nodes hardware as part of HPC3. Annual funds are
     used to add to this resource enabling RCIC to provide no-cost :ref:`resource allocations <allocations>`
     to a larger fraction of the UCI research community.

  The most significant change from a condo-only is that :underline:`owner-dedicated queues no longer exist`.
  Instead, researchers receive an allocation of available core-hours that are
  deposited into a :underline:`bank account` [1]_.

**A bank account:**
  * Has owners, and they can designate others who can charge to their account.
  * Can have multiple authorized users and allocated jobs are charged against the account.
  * For node owners, the theoretical capacity of their hardware is converted into available core hours
    and deposited into the :underline:`bank account` in addition to any granted or purchased hours.
  * Represents computing units (CPU-hour or GPU-hour) and logically functions as a :underline:`prepaid` account.
  * Can be filled in a variety of ways

      :Granted:
        UCI core funds have purchased nodes that create the capacity for granted hours,
        or :underline:`no-cost allocations`.

      :Converted: from :underline:`hardware purchase`.
        Each node can deliver **core-hours = cores * 8760 hours/year**
        theoretical maximum. For node owners, 95% of this maximum is deposited annually
        into an account for their use on any resource in the cluster.

      :Purchased: :underline:`recharge allocations`.
        UCI researchers can purchase prepaid time to fill/augment their banks.

**Quick links to most common information requests**
  | HPC3 provides a rich collection of domain-specific :ref:`modules` software packages.
  | What are :ref:`allocations` in detail.
  | How does :ref:`reallocation` work.
  | How to use :ref:`recharge allocations` to buy core-hours or hardware.
  | Hardware :ref:`specs`.

.. _hpc3 goals policies:

Goals & Policies
----------------
The HPC3 planning committee crafted policy guidelines to meet the following goals:
  * Enable access to a larger compute/analysis system than could be reasonably afforded on an individual lab basis.
  * Enable access to specialized nodes (e.g. large memory, GPU).
  * Foster a growing community across UCI to use scalable computing (:term:`HPC` and :term:`HTC`)
    for their scientific research and teaching.
  * Provide a well-managed software environment that underpins a reproducible scientific instrument.
    Fit seamlessly into the progression of:

    :guilabel:`desktop` → :guilabel:`lab cluster` → :guilabel:`campus` → :guilabel:`national` -> :guilabel:`commercial cloud`
  * Enable construction of more-secure research environments.

HPC3 policies are needed to primarily address issues such:
  * How is *contention* for acquiring and using resources addressed?
  * How does one balance high utilization against wait times for jobs to start ?
  * What are principles to enable and support long-running jobs?
  * Are there ways to support priority boosting for jobs with specific deadlines (e.g. grants and publications)?
  * How can groups that contributed resources be ensured their fair share?

The questions above have no single right answer and this means that:
  * Any policy employed on HPC3 must be tuned to balance the wide range of needs specifically for the UCI research community.
  * Any implemented policy must be fluid and flexible.

.. The `Research Cyberinfrastructure Vision Document <http://sites.uci.edu/rci/files/2016/03/A-Vision-for-RCI-at-UCI-Document-and-Appendices.pdf>`_
   this link is no longer valid, use cached version.

Please see the following documents for more in-depth information.
  `A Vision For Research CyberInfrastructure at UCI </_static/A-Vision-for-RCI-at-UCI-Document-and-Appendices.pdf>`_
      provides the rationale for what Research Cyberinfrastructure should be and some
      new features that need to be implemented.
  `Policy/Usage Document <https://docs.google.com/document/d/1fqTC5tc29JK2PfIATPqnUfwo3SooLBCEMzogbKBjslU/edit>`_
      provides a draft document started in 2018. The RCIC began the process of crafting this document
      that could provide the framework for creating HPC3 and the principles by which it would run.
      The HPC3 subcommittee of the RCIC advisory committee edited and refined the initial version.
      Going forward, this document will continually be updated to reflect adjustments and refinements.
  `HPC3 Policy </_static/HPC-Policy-Executive-Summary.pdf>`_
      provides an executive summary.

.. _hpc3 sharing:

Fair Sharing
------------

At the heart of HPC3 sharing
is :underline:`core-hour and GPU-hour accounting` where jobs are classified as:

  :bluelight:`Accounted jobs`:
    * Time used by a job is tracked against a *bank* of hours.
      HPC3 will be able to track usage of the cluster and the overall usage is in proportion
      to how much a particular research program has contributed to the physical infrastructure.
    * The fundamental difference between accounted and free is that an accounted
      job may NOT be suspended or killed in favor of another job.
    * Once an accounted job is allocated resources, it will not be preempted.

  :bluelight:`Free jobs`:
    * Non-accounted jobs that may be killed at any time to make room for accounted jobs.

For example, a research group that has purchased 10 nodes will have over each year:

  1. About 10 nodes-worth of accounted jobs to run on the cluster.
  2. Nothing limits that group to just their 10 nodes. This means that a group can access a larger number of nodes in bursts.
  3. No *guarantee* is given that they can they can have instantaneous access to their particular purchased nodes in the cluster.
     This means that there may be times of contention where a node owner may have to wait.

  | :underline:`This combination supports the goal of access to a larger resource`:
  |      :bluelight:`When an accounted job is running on a larger number of nodes`,
  |      :bluelight:`than purchased that job cannot be killed or suspended`.

The principles can be coded into *queuing policy* to achieve reasonable balance of access,
stability and other qualities.  Some of the sharing principles include:

  * Once a job has started, predictability of run time is highly-desirable.
  * Small core-count, short-duration jobs should have little to no waiting time.
  * Very large numbers of jobs submitted at one time  by some users should not result in other
    users waiting for all those jobs to complete (HPC3 is not first-in, first-out).
  * Free (non-accounted) jobs should still be possible and encouraged if their impact to accounted jobs is minimal.

.. [1] Available balance is reset every six months and is a combination of granted, purchased,
       At the time of re-allocation, any unused hours are forfeit.
