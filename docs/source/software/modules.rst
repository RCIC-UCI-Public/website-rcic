.. _modules:

Software 
=========

Overview
---------

HPC3 serves researchers from all corners of the UCI campus. At the heart of the value that RCIC adds 
to HPC3, is wide range of application software that is pre-compiled and ready for use. There are 
literally hundreds of domain-specific, community-supported, applications maintained on the cluster.

Some software is quick and easy to compile, install, and make available to users. Other applications 
have numerous (often undocumented) software requirements, unique build methods, and conflicting 
requirements when compared to other applications. The size of the problem is quite large, and grows with each new application.

HPC3 operating system is Rocky Linux 8 as of August 30, 2022. 
All installed software is compiled specifically for this OS.

For the most part, cluster users only need to know (or discover) the already-available environment 
module and load it prior to using their application.

What are Modules
-----------------

There are a few meanings for modules

1. **Language modules**  are collections of related variables, functions and subroutines that perform a set 
   of specific programming tasks. Simply put they are files consisting Perl/Python/R code. 
   To access a language module or search what is available, you need to use its language: Perl/Python/R.

2. **Environment modules** are used to activate a specific software that a user wants to use. See below how to identify and use them.
   Environment modules provide a  way to control which versions of software are active. 
   Typically, a user only needs to know which module(s) is (are) needed to gain access to their application(s). 

Using Modules
-------------

Modules are quite simple to use.

- loading a module modifies environment variables (e.g., ``PATH`` for
  executables or ``LD_LIBRARY_PATH`` for shared object libraries and others). It is used to activate the software.

- unloading a module reverses the action of load: unsets the environment variables set by loading. It is used to deactivate the software.

Which software is installed 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A very large fraction of software applications on HPC3 have a module associated with it.
To find out what software packages are available, type:

.. code-block:: bash

   module avail


To list all versions of a specific software:

.. code-block:: bash

   module avail software-name

You might not know the name of a particular module or versions available. 
You can use one of the following commands to find some information. The first
one can do a lokup for a partia;l name, the second one will find the keyword if it shows up anywhere in the module definition:

.. code-block:: bash

   module avail partial-name
   module keyword hmmer

Nearly all modules have specific version numbers. If not specified, the latest found is used. 
You should always include the version number when loading a module. This will ensure that you always get the version you intend.

