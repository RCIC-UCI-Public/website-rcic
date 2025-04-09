.. _get account:

Getting an account
==================

| Anyone with a **valid UCInetID** can have an account.
| There is no cost for a user to obtain an account on HPC3 cluster.

1. Please send email (from your UCInetID email) to hpc-support@uci.edu and provide:

   * Your name
   * Your UCInetID (different from student ID)
   * Optionally,

     **If you are affiliated with a PI lab and want to use PI lab resources**
     you need to check with your PI what resources are available to the group
     (some PIs don't have all resources) and need to specify what resources
     you are requesting, for a reference see:

         | :ref:`How to be added to PI group Slurm account <add lab account>`
         | :ref:`How to be added to PI group DFS access <add lab dfs>`
         | :ref:`How to be added to PI group CRSP access <getting crsp account>`

     **You must cc** your email to your PI.
     We will need a confirmation from your PI to add you to the lab resources
     access and cc keeps everything on the same ticket for simplicity.

#. The email opens a ticket in our ticketing system.
   Once your account is created you will be notified by email.

#. After you get a confirmation email about your account being created please review:

   * :ref:`acceptable use`
   * :ref:`login`

.. attention::

   | :bluelight:`Your account` is your **UCInetID** (lower case alphanumeric)
   | :bluelight:`Your password` is **your regular password** that you use for your UCInetID
   | :red:`We do not store, handle or reset passwords for UCInetIDs.`

.. _closing account:

Closing an account
==================

For as long as you have a valid UCInetID and you use your account it remains active.
When you separate from UCI your UCInetID will become inactive some time after
the separation.

The accounts are closed when one of the following is true:
  * Your account has no activity for 1 year.
  * When your UCInetID loses student status.
    Most student alumni keep student status for up to 1 year after the graduation.
  * When your UCInetID loses staff/researcher/PI affiliation.


.. _data after account deletion:

What happens to data when an account is closed?
-----------------------------------------------

:bluelight:`The following applies to students (undergraduate, graduate, and post-doctoral researchers)`

RCIC *must* follow university policy for data related to students.  There are two types of data that might be
associated with a student and it revolves around who owns the intellectual property to that data. ``<UCINetID>`` below
means the OIT-supplied unique identifier for the student.

1. *Private* - any data held in ``$HOME`` (CRSP and HPC3) or ``/pub/<UCINetID>``.   
       This data is private 
       to the student and **cannot** be copied or moved from this area without their explicit permission.  Data stored
       in these locations is the intellectual property of the student.

#. *University Owned* - any data held in a CRSP lab area or a DFS lab area (e.g., ``/dfs9/faculty-lab``). 
     This data is
     the intellectual property of the University of California.  The faculty member who "owns" the lab area is the
     steward of that data. A student *may not* remove or make a copy of that data without the explicit permission of
     the University (the faculty member can give (or deny) permission as they are have the best understanding of the
     intrinsic value of the data). Data stored here is most-often the result of funded research. 

.. note::
   *Private* data also has limits. All users of (and all data stored on) University systems must comply with permissable use. 
   In all cases, RCIC follows the rules of the University when giving access to data stored on the systems that
   it manages. For example, if access to private data is required for any sort of legal action, RCIC must make
   that requested data available. 

:bluelight:`What happens the actual data when a student is no longer at UCI?`

When a student has their UCINetID deactivated by the university, RCIC at some time after the deactivation will do 
the following:

  * Remove the student `<UCINetID>` from HPC3 and/or CRSP.  This automatically removes them from any unix groups, too.

  * Archive *private* data for 6 months.  After 6 months, *private* data is permanently deleted and cannot be recovered.

  * Leave *University Owned* data untouched. In other words, that data is neither archived nor deleted.  If access to
    the data is required, then the faculty steward must open a support ticket to request any changes that
    they cannot perform themselves. These changes might include: unix account ownership of any
    files/directories (recommended); adjust access permissions on any/all files directories, and/or delete data. Since
    the University owns the data, access can be immediately granted to the faculty steward. 
     

:bluelight:`Can I get a copy of the student's private data?`

**Only a faculty member at UCI can make a request** to obtain a copy of private student data.
Access will be granted only if the student gives explicit permission (usually via an email 
request from a faculty member and a copy of a positive reply from the student). Under 
extenuating circumstances, RCIC can declare *private data* as *abandoned*.  In that case, RCIC will work with 
the faculty member to determine which, if any, files and directories are research
related.  Only research-related data can be copied.  

:bluelight:`What happens to non-student (e.g., employee, faculty, contractor) data?`

  * RCIC will remove the user from HPC3 and/or CRSP and archive data in ``$HOME`` and ``/pub/<ucinetid>``

  * There is no such thing as *private* data for regular employees. However, if someone requests access to 
    this data after a non-student departs,  RCIC errs on the side of caution and treats those requests as it does 
    for students, requesting permission prior to granting access. Even though data is not private, that does imply
    that anyone at UCI can access this data. In all cases, RCIC follows University policy. 



