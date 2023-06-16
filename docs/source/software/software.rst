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

.. important:: | HPC3 operating system is Rocky Linux 8 (as of August 30, 2022).
               | All installed software is compiled specifically for this OS.

For the most part, cluster users only need to know (or discover) the
*already-available application environment module* and load it prior to using
the application. 

TODO [.h2copy]#Available Software on HPC3#
TODO <<modules-update.txt#, DETAILED INFO about modules update for Linux 8>>

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
  * Properly encoded dependencies help to ensure that removal of a particular package won't leave other software in a "broken" state.
  * Ease of transitioning to container definitions. One of our goals is to allow users to easily take away *subsets* of 
    the HPC3 software stack in the form of a singularity container.
  * Enable installation of  multiple versions of same software.
  * Use native OS tools for admins/users to get information about installed software.

.. _software stack:

Software Stack
--------------

The deployed software stack is generally added to on weekly basis. This is in response to a near-continuous
stream of requests. 

The complete stack is fairly complex and captures dependencies. 
`A Software Map (PDF) </_static/software-latest.pdf>`_ shows a snapshot
of the collections of software, software modules they provide, and build dependencies.

Users of HPC3 need to login and use :ref:`list modules` to see the most recent software versions and availability. 
Please see :ref:`modules` to learn how to use software modules. 

If you want to request new software, please see :ref:`software tickets`.

.. _software user installed:

User installed software
------------------------

Users often ask to add packages to :tt:`Python` / :tt:`R` / :tt:`Perl` / :tt:`conda` base installations.

| These usually need to be installed by users themselves.
| The following guides explain how to install software in user area:

===================== =========================== ================
:ref:`install conda`  :ref:`install python`       :ref:`install r`
:ref:`install perl`   :ref:`install singularity`
===================== =========================== ================

.. note:: There are a few important initial steps that are unique
          to the HPC3 and are related to using specific modules. 
          They are explained in above guides.


TODO 

Simply load  Python/R/Perl/conda module (use ``module avail`` command to
see what is installed) to access the desired language and follow your package 
installation instructions. 

