
.. _data transfer:

Data transfer
=============

If you need to bring some data from your laptop or another host to the
cluster you will mainly need to use ``scp`` (there is an equivalent for
Windows)  or ``rsync`` commands. 

You will need to give extra command-line parameters to ensure that
the data transfer program you use will respect the sticky bit 
and not cause quota issues.

.. _scp data:

Using scp
---------

The ``scp`` is a secure file transfer protocol. Scp allows one to connect to a remote server
and transmit desired files via the connection. 

.. danger:: When files are transferred the destination sticky bits on directories
            are not inherited.

- This is not a problem if the users are copying files to :tt:`/pub/ucinetid`
- This is a problem when copying to :tt:`/dfsX/group-lab-path` area and usually
  results in :red:`quota exceeded errors`.

There are 2 ways to deal with this.

:bluelight:`Scenario 1`
   Scp needed files (using recursive directives if needed).
   For example, a user has an access to a group allocation :tt:`/dfsX/panteater_lab/panteater`
   and want to transfer data there.

   On your laptop or other server run ``scp`` command:

   .. code-block:: console

      $ scp -r mydata panteater@hpc3.rcic.uci.edu:/dfsX/panteater_lab/panteater

   On HPC3 check the permissions on the transferred directory:

   .. code-block:: console

      $ ls -l /dfsX/panteater_lab/panteater
      total 138
      drwxr-xr-x 6 panteater panteater_lab     18 Feb 18 13:10 mydata

   Note, the permissions :tt:`drwxr-xr-x` are missing *s* (sticky bit is not set)
   and this means all subdirectories under *mydata* are also missing it.
   Will need to fix the permissions on *mydata*:

   .. code-block:: console

      $ chmod g+s /dfsX/panteater_lab/panteater/mydata*

   Similarly, repeat ``chmod`` on all subdirectories under it.

:bluelight:`Scenario 2`
   This requires less work and is more accurate.

   On your laptop (or remote server) create a compressed tar file of the
   files you want to transfer and then scp this compressed file:

   .. code-block:: console
  
      $ tar czvf mydata.tar.gz mydata
      $ scp -r mydata.tar.gz panteater@hpc3.rcic.uci.edu:/dfsX/panteater_lab/panteater

   On the cluster, uncompress transferred file and check permissions:

   .. code-block:: console
  
      $ cd /dfsX/panteater_lab/panteater
      $ tar xzf mydata.tar.gz
      $ ls -l
      total 138
      drwxr-sr-x 6 panteater panteater_lab     18 Feb 18 13:12 mydata

      $ ls -l mydata
      total 124
      -rw-r--r--  1 panteater panteater_lab 17075 Jul 21  2020 desc.cvs
      -rwxr-xr-x  1 panteater panteater_lab  7542 Jul 21  2020 README
      drwxr-sr-x  2 panteater panteater_lab     4 Feb 18 12:03 common
      drwxr-sr-x  2 panteater panteater_lab     3 Feb 18 12:03 images
   
   Note, the permissions :tt:`drwxr-sr-x` on **mydata** include :tt:`s` and all directories
   under **mydata** inherited it.  Delete transferred **mydata.tar.gz** after verification.

.. _rsync data:

Using rsync
-----------

The ``rsync``  is a program that allows to greatly speed up file transfers.
See ``man rsync`` for more information and options to use.

There are two options in ``rsync`` command that will overwrite the destination
permissions and is a common issue the users encounter when transferring data:

- ``-p, --perms`` preserve permissions
- ``-a, --archive`` archive mode; same as ``-rlptgoD``, implies ``-p``

.. important:: When ``-p`` option is used, ``rsync`` preserves the permissions of the source and
               this is not correct for the files and directories  in destination that need to comply with
               user:group permissions.

               Avoid using ``-p, -a`` options when running ``rsync`` commands.

For example, for a recursive copy use:

.. code-block:: console 

   $ rsync -rv mydata panteater@hpc3.rcic.uci.edu:/dfsX/panteater_lab/panteater

