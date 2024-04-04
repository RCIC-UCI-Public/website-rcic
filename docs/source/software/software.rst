.. _software:

Software 
=========

HPC3 serves researchers from all corners of the UCI campus. At the heart of the value that RCIC adds 
to HPC3, is wide range of application software that is pre-compiled and ready for use. There are 
literally hundreds of domain-specific, community-supported, applications maintained on the cluster.

Some software is quick and easy to compile, install, and make available to users. Other applications 
have numerous (often undocumented) software dependencies, unique build methods, and conflicting 
requirements when compared to other applications.
The size of the problem is quite large, and grows with each new application.

**RCIC uses a multi-factor approach to provide a stable and flexible environment**

  * Adoption of a declarative, repeatable
    `YAML2RPM build methodology <https://github.com/RCIC-UCI-Public/yaml2rpm>`_ designed by RCIC  that
    generates re-usable :term:`RPM` that can installed on any compatible CentOS system.
  * Nearly all installed software is packaged as an RPM with encoded dependencies.
    Exceptions generally fall around very large footprint software like the
    `Intel Compiler <https://software.intel.com/content/www/us/en/develop/tools/compilers.html>`_
    and `MATLAB <https://www.mathworks.com>`_ and similar.
  * Most software is accessed only after loading the
    appropriate software modules.


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

.. _software use:

How to use
==========

.. important:: | HPC3 operating system is **Rocky Linux 8** (as of August 30, 2022).
               | All installed software is compiled specifically for this OS.

**Already installed software**
  For the most part, cluster users only need to know or discover the
  already available application environment module and load
  it prior to using the application. Please see:

  * :ref:`modules` to learn how to use software modules, including 
    how to to see the most recent software versions and availability. 
  * :ref:`software updates` for details about installed software and their modules.

**Licensed Software**
  Access to some applications requires a license. Only registered users can
  use such software. We do not purchase or provide licenses.
  Licenses are usually bought by the PIs for their groups group and the access must be approved by a PI.

  When submitting a ticket requesting an access to the licensed software
  please cc your email request to the PI to assist with the confirmation processing.

  Current licensed software:
    | Abaqus
    | Gaussian
    | Stata 16 and 17
    | VASP 5.* and 6.*


**New software**
  If you want to request new software, please see :ref:`user installed` :underline:`before` :ref:`software tickets`.

**Docker**
  .. attention:: **Docker** is not available per security vulnerability, use
                 singularity. See :ref:`install singularity` guide.

**Sudo and su**
  .. attention:: Commands ``sudo`` and ``su`` are not available per security vulnerability.



