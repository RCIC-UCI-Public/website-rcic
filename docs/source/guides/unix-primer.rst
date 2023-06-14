.. _unix primer:

UNIX primer
===========

The information is intended for **new HPC3 users** and
for **users that are new to Linux/UNIX-like operating systems.**
Please consult the rest of the user guides for information that is not covered here.

This page contains info to provide some familiarity with Linux/UNIX
but it is not an exhaustive guide.

.. _file permissions:

File permissions
----------------

.. important:: File permissions are used in determining quotas.

Our cluster and storage systems are running one of the  :term:`UNIX` operating
systems.  All data in Unix is organized into **files**, all files are organized into
**directories** and the directories are organized into a tree-like structure called the **filesystem**.

:bluelight:`There are three basic types of files`:

:ordinary file:
  is a file on the system can contains data, text, program instructions.
:directory:
  directories store special and ordinary files. Unix directories are equivalent to folders on Windows or Mac OS.
:special file:
  file that can provide access to hardware such as hard drives, symbolic links.

:bluelight:`Every file has the following access modes`:

:read:
  denoted as **r**, the capability to read or view the contents of the file.
:write:
  denoted as **w**, the capability to modify and remove the content of the file.
:execute:
  denoted as **x**, the capability to run a file as a program.
:sticky bit:
  denoted as **s**, additional  capability to set permissions for Set User ID (SUID) and Set Group ID (SGID) bits.

:bluelight:`Every file has the following attributes or permissions`:

:owner:
  determine what actions the owner of the file can perform on the file.
:group:
  determine what actions a user, who is a member of the group that a file belongs to, can perform on the file.
:other (world):
  determine what action all other users can perform on the file.

File permissions can be displayed when using ``ls -l`` command:

.. code-block:: console

   $ ls -l
   total 55524423
   drwxrwsr-x  7 panteater bio               127 May 12 16:29 biofiles
   -rw-r--r--  1 panteater panteater  4294967296 May 31  2022 performance.tst

In the output, a first line labeled **total** shows number of blocks
used in the file system by the files which are listed as the directory's contents.
The default block size is 512 bytes.

The remaining lines are the listing of a directory's contents.
The following information is displayed for each file (example of the second line):

:file mode:
  ``drwxrwsr-x``
:number of links:
  7
:owner name:
  panteater
:group name:
  bio
:number of bytes in the file:
  127
:abbreviated month:
  May
:day-of-month file was last modified:
  12
:hour file last modified:
  16
:minute file last modified:
  29
:pathname:
  biofiles

The first filed in the output, a file mode, represents file type and its associated
permissions. For example, file mode ``drwxrwsr-x`` for **biofiles**:

.. table::
   :class: noscroll-table

   +-----------+-----------------------------------------------------------------------------+
   | character |  meaning                                                                    |
   +===========+=============================================================================+
   | 1         | ``d`` is a file type, in this case a directory                              |
   +-----------+-----------------------------------------------------------------------------+
   | 2-4       | ``rwx``  are the owner permissions. The owner                               |
   |           | has read (r), write (w) and execute (x) permissions.                        |
   +-----------+-----------------------------------------------------------------------------+
   | 5-7       | ``rws`` are the group permissions. The group has read (r),                  |
   |           | write (w), execute (x) permissions, the sticky bit ``s`` is set.            |
   +-----------+-----------------------------------------------------------------------------+
   | 8-10      | ``r-x`` are the world permissions (everyone else). Everyone has read (r)    |
   |           | and execute (x) permissions.                                                |
   +-----------+-----------------------------------------------------------------------------+

To learn more about files permissions execute command ``man ls``.

.. _special characters:

Special Characters
------------------

.. important:: Avoid using special characters in file or directory names.

Special characters are used by :tt:`bash` and have an alternative, non-literal meaning.
For example, a **white space** is one such special characters and can be  represented by:

===== ======= === ============ =============== =========
space newline tab vertical tab carriage return form feed
===== ======= === ============ =============== =========

Please see a
`list of special characters <https://www.oreilly.com/library/view/learning-the-bash/1565923472/ch01s09.html>`_
and avoid using them in file and directory names.
