.. _software use:

Software
========

  | :ref:`cluster os`
  | :ref:`Installed Software <installed software>`
  | :ref:`Licensed Software <licensed software>`
  | :ref:`How the software is built <how is built>`
  | :ref:`Request New Software <request new software>`

HPC3 serves researchers from all corners of the UCI campus. At the heart of the value that RCIC adds 
to HPC3, is wide range of applications software that is compiled and ready for use. There are 
literally hundreds of domain-specific, community-supported, applications maintained on the cluster.

.. _cluster os:

:section:`Cluster Operating System`
  .. important:: | |hpc3-OS|
                 | |hpc3-sw|

  .. attention:: * **Docker** is not available per security vulnerability, use
                   singularity. See :ref:`install singularity` guide.
                 * ``sudo`` and ``su`` commands are not available per security vulnerability.

.. _installed software:

:section:`Installed software`
  Most software is accessed only after loading the appropriate software modules.
  Cluster users simply need to know or discover the
  already available application environment module and load
  it prior to using the application. Please see:

    * :ref:`How to use software modules <modules>`
    * :ref:`software updates`
    * :ref:`Exampels how to use spcific software <job examples>`

..
  The following table lists available software (by their associated modules)
  together with a category and a short description. Info on modules naming schema
  is available :ref:`in this page <use modules>`. 

  Click on the column header for sorting.

  .. csv-table:: Installed Software, updated :blogauthor:`14 July 2025`.
     :class: noscroll-table sortable
     :file: sw.csv
     :widths: 25,10,65
     :header-rows: 1

.. _licensed software:

:section:`Licensed Software`
  Access to the following applications requires a license:

  +--------+--------+----------+------------+----------+----------+
  | Abaqus | COMSOL | Gaussian | MATLAB     | Stata 16 | VASP 5.x |
  |        |        |          |            |          |          |
  |        |        |          |            | Stata 17 | VASP 6.x |
  +--------+--------+----------+------------+----------+----------+

  .. note:: While all users can view and load modules for licensed software only registered users
            (*users must be in specific groups*) can use such software.

            One exception to this is MATLAB.
            RCIC contributes to the UCI-wide license and
            MATLAB is available to all the HPC3 users. Users only need to load one of
            the available MATLAB modules in order to use this software.

  * **RCIC does not purchase or provide licenses**, we only enable an access to the licenses.
  * **The departments/PIs buy licenses** for their labs and the access must be approved by a PI.
  * **Users must submit a ticket** requesting :ref:`Access to Licensend Software <access licensed software>`
    in order to use to licensed applications.

.. _how is built:

:section:`How it is built`
  Some software is quick and easy to compile, install, and make available to users. Others
  have numerous (often undocumented) software dependencies, unique build methods, and conflicting 
  requirements. The size of the problem is quite large, and grows with each new application.

  **RCIC uses a multi-factor approach to provide a stable and flexible environment**
    * Adoption of a declarative, repeatable
      `YAML2RPM build <https://github.com/RCIC-UCI-Public/yaml2rpm>`_ methodology designed by RCIC which
      generates reusable :term:`RPM` that can installed on any compatible CentOS system.
    * Nearly all installed software is packaged as RPMs with encoded dependencies.
      Exceptions generally are very large footprint software like the
      `Intel Compiler <https://software.intel.com/content/www/us/en/develop/tools/compilers.html>`_
      or `MATLAB <https://www.mathworks.com>`_.

  **Why use RPMS?**
    For us, it's one extra step that comes a wide variety of benefits:

    * The complete stack is fairly complex and captures needed dependencies. 
    * Enable installation of multiple versions of same software.
    * Use native operating system tools to get information about installed software.
    * The package manager will not allow two different RPMs to claim ownership of the same file
      (or have conflicting permissions on a shared directory path).
    * Properly encoded dependencies help to ensure that removal of a particular package won't leave other software in a *broken* state.
    * Ease of transitioning to container definitions. We can easily put a *subsets* of 
      the HPC3 software stack in the form of a singularity containers.

    The deployed software stack is generally added to on weekly basis. This is in response to a near-continuous
    stream of requests. 

    `A Software Map (PDF) </_static/software-latest.pdf>`_ shows a snapshot
    of the collections of software, software modules they provide, and build dependencies.

.. _request new software:

:section:`Request New Software`
  Please see :ref:`user installed` :underline:`before` requesting new software install.

  You may :ref:`submit a request for new software <software install tickets>`  to be added to HPC3,
  however we cannot and do not say *yes* to every request.
  RCIC is simply not large enough to handle all software requests.  

  :bluelight:`RCIC prioritizes all software requests as follows:`
    1. Fix a compilation problem, security issue, or functionality issue of existing software.
    #. A new release of an already-installed software provides *significant* new capability.
    #. New software has a demonstrated need by multiple labs.

  :bluelight:`RCIC says NO to the following types of requests:`
    1. When a request does not meet the above priority criteria.
    #. Software that the user wants to evaluate.
    #. Licensed software that does not use the FlexLM license manager
       or requires RCIC to run the license server.
    #. Software that will only be used by one or two users.
    #. Software that requires MySQL, PostgreSQL, HTTP or similar server setup.

.. |hpc3-OS| replace:: HPC3 operating system is **Rocky Linux 8.10** (as of December 18, 2024).
.. |hpc3-sw| replace:: All installed software is compiled specifically for this OS.

