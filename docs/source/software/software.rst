.. _software use:

Software
========

HPC3 serves researchers from all corners of the UCI campus. At the heart of the value that RCIC adds 
to HPC3, is wide range of applications software that is compiled and ready for use. There are 
literally hundreds of domain-specific, community-supported, applications maintained on the cluster.

.. important:: | HPC3 operating system is **Rocky Linux 8** (as of August 30, 2022).
               | All installed software is compiled specifically for this OS.

:bluelight:`Already installed software`
  Most software is accessed only after loading the appropriate software modules.
  For the most part, cluster users only need to know or discover the
  already available application environment module and load
  it prior to using the application. Please see:

  * :ref:`modules` to learn how to use software modules, including 
    **how to to see the most recent software versions and availability**. 
  * :ref:`software updates` for details about installed software and their modules.
  * :ref:`job examples` for details about specific software use.

.. _licensed software:

:bluelight:`Licensed Software`
  Access to some applications requires a license.

  Current licensed software:
    | Abaqus
    | Gaussian
    | Stata 16 and 17
    | VASP 5.* and 6.*

  .. note:: While all users can view and load modules for licensed software only registered users
            (*users must be in specific groups*) can use such software.

  RCIC does not purchase or provide licenses, we only enable an access to the licenses.
  Licenses are usually bought by the PIs for their labs and the group access must be approved by a PI.

  In order to be in a specific license software  group we need a confirmation from your
  PI who bought the license and we need to have a record of such license
  (proof of license from the PI).

  When submitting a ticket requesting an access to the licensed software
  please cc your email request to your PI to assist with the confirmation processing.

:bluelight:`New software`
  Please see :ref:`user installed` :underline:`before` :ref:`software tickets`.
:bluelight:`Docker`
  .. attention:: **Docker** is not available per security vulnerability, use
                 singularity. See :ref:`install singularity` guide.
:bluelight:`Sudo and su`
  .. attention:: Commands ``sudo`` and ``su`` are not available per security vulnerability.

.. _software:

Requesting New Software
-----------------------

You may submit a request for new software to be added to HPC3 through the usual support email. RCIC cannot and does not 
say "yes" to every request. RCIC is simply not large enough to handle all software variations and/or requests.  

:bluelight:`RCIC prioritizes all software requests as follows:`
  1. Request to fix a compilation problem, security issue, or functionality issue of existing software.
  #. A new release of an already-installed software provides *significant* new capability 
  #. New software has a demonstrated need by multiple labs
  #. Staff as time availability when a request does not meet the above

:bluelight:`RCIC says NO to the following types of requests:`
  1. Software that the user wants to evaluate
  #. Licensed software that does not use the FlexLM license manager when RCIC must run the license server
  #. Software that will only be used by one or two users

How it is built
---------------

Some software is quick and easy to compile, install, and make available to users. Other applications 
have numerous (often undocumented) software dependencies, unique build methods, and conflicting 
requirements when compared to other applications.
The size of the problem is quite large, and grows with each new application.

**RCIC uses a multi-factor approach to provide a stable and flexible environment**

  * Adoption of a declarative, repeatable
    `YAML2RPM build methodology <https://github.com/RCIC-UCI-Public/yaml2rpm>`_ designed by RCIC  that
    generates reusable :term:`RPM` that can installed on any compatible CentOS system.
  * Nearly all installed software is packaged as an RPM with encoded dependencies.
    Exceptions generally fall around very large footprint software like the
    `Intel Compiler <https://software.intel.com/content/www/us/en/develop/tools/compilers.html>`_
    and `MATLAB <https://www.mathworks.com>`_ and similar.


**Why use RPMS?**
  For us, it's one extra step that comes a wide variety of benefits:

  * The package manager will not allow two different RPMs to claim ownership of the same file
    (or have conflicting permissions on a shared directory path).
  * Properly encoded dependencies help to ensure that removal of a particular package won't leave other software in a *broken* state.
  * Ease of transitioning to container definitions. One of our goals is to allow users to easily take away *subsets* of 
    the HPC3 software stack in the form of a singularity container.
  * Enable installation of  multiple versions of same software.
  * Use native OS tools for admins/users to get information about installed software.

The deployed software stack is generally added to on weekly basis. This is in response to a near-continuous
stream of requests. 

The complete stack is fairly complex and captures dependencies. 
`A Software Map (PDF) </_static/software-latest.pdf>`_ shows a snapshot
of the collections of software, software modules they provide, and build dependencies.
