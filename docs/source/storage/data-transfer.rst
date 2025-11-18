
.. _data transfer:

Data transfer
=============

.. contents::
   :local:

If you need to bring some data from your laptop or another host to the
cluster you will mainly want to use ``scp`` (there is an equivalent for
Windows)  or ``rsync`` commands. 

.. important:: You will have to use correct command-line parameters to ensure that
   the data transfer program you use will respect the sticky bit and not cause quota issues.

.. _scp data:

Using scp
---------

The ``scp`` is a secure file transfer protocol. It allows one to connect to a remote server
and transmit desired files via the connection. 

.. danger:: When files are transferred the destination sticky bits on directories are not inherited.

           - This is not a problem if the users are copying files to :tt:`/pub/UCInetID`
           - This is a problem when copying to :tt:`/dfsX/group-lab-path` area and it usually
             results in :red:`quota exceeded errors`.

There are 2 ways to deal with this.

:bluelight:`Scenario 1`
   Transfer needed files (using recursive directives if needed).
   For example, a user has an access to a group allocation :tt:`/dfsX/panteater_lab/user1`
   and want to transfer data there.

   On your laptop or other server run ``scp`` command:

   .. code-block:: console

      $ scp -r mydata panteater@hpc3.rcic.uci.edu:/dfsX/panteater_lab/user1

   On HPC3 check the permissions on the transferred directory:

   .. code-block:: console

      $ ls -l /dfsX/panteater_lab/user1
      total 138
      drwxr-xr-x 6 user1 panteater_lab     18 Feb 18 13:10 mydata

   Note, the permissions :tt:`drwxr-xr-x` are missing *s* (sticky bit is not set)
   and this means all subdirectories under *mydata* are also missing it.
   Will need to fix the permissions on *mydata*:

   .. code-block:: console

      $ chmod g+s /dfsX/panteater_lab/user1/mydata*

   Similarly, repeat ``chmod`` on all subdirectories under it.

:bluelight:`Scenario 2`
   This requires less work and is more accurate.

   On your laptop (or remote server) create a compressed tar file of the
   files you want to transfer and then scp this compressed file:

   .. code-block:: console
  
      $ tar czvf mydata.tar.gz mydata
      $ scp -r mydata.tar.gz panteater@hpc3.rcic.uci.edu:/dfsX/panteater_lab/user1

   On the cluster, uncompress transferred file and check permissions:

   .. code-block:: console
  
      $ cd /dfsX/panteater_lab/user1
      $ tar xzf mydata.tar.gz
      $ ls -l
      total 138
      drwxr-sr-x 6 user1 panteater_lab     18 Feb 18 13:12 mydata

      $ ls -l mydata
      total 124
      -rw-r--r--  1 user1 panteater_lab 17075 Jul 21  2020 desc.cvs
      -rwxr-xr-x  1 user1 panteater_lab  7542 Jul 21  2020 README
      drwxr-sr-x  2 user1 panteater_lab     4 Feb 18 12:03 common
      drwxr-sr-x  2 user1 panteater_lab     3 Feb 18 12:03 images
   
   Note, the permissions :tt:`drwxr-sr-x` on **mydata** include :tt:`s` and all directories
   under **mydata** inherited it.  Delete transferred **mydata.tar.gz** after verification.

.. _rsync data:

Using rsync
-----------

The ``rsync``  is a program that allows to greatly speed up file transfers.
See ``man rsync`` for more information and options to use.

There are two options in ``rsync`` command that will overwrite the destination
permissions and it is a common issue that the users encounter when transferring data:

  | ``-p, --perms`` preserve permissions
  | ``-a, --archive`` archive mode; same as ``-rlptgoD``, implies ``-p``

  .. important:: When ``-p`` option is used, ``rsync`` preserves the permissions of the source and
                 this is not correct for the destination server where  files and directories need
                 to have very specific **user:group** permissions.

                 Avoid using ``-p`` and ``-a`` options when running ``rsync`` commands.

For example, for a recursive copy  of a local directory and to show a verbose output one can use:

  .. code-block:: console 

     $ rsync -rv mydata panteater@hpc3.rcic.uci.edu:/dfsX/panteater_lab/user1

.. _aspera data:

Using Aspera
------------

There is no installation of Aspera cluster-wide as the Aspera client needs to
be installed by the user in a user-writable area.

1. **Download**

   You  will need to download and install Aspera Connect software from: https://www.ibm.com/aspera/connect/.
   Copy the URL for :blue:`Linux` on the download page and paste into ``wget`` command to download:

   .. code-block:: console

      $ wget https://d3gcli72yxqn2z.cloudfront.net/downloads/connect/latest/bin/ibm-aspera-connect_4.2.8.540_linux_x86_64.tar.gz

   Per above, a file is saved as :tt:`ibm-aspera-connect_4.2.8.540_linux_x86_64.tar.gz`.
   Note, available version for this example is :tt:`4.2.8.540`, and it will change when a new version becomes available.

2. **Install**

   Use the correct version number from your download in the following commands:

   .. code-block:: console

      $ tar -zxvf ibm-aspera-connect-VERSION_linux_x86_64.tar.gz
      $ ./ibm-aspera-connect-VERSION_linux_x86_64.sh

   This will result in creating :tt:`$HOME/.aspera/connect` directory which will have all
   needed components of the Aspera Connect client as far as compiled binary, certificates, etc.

3. **Use**

   Sites that require using Aspera Client for upload/download usually provide
   specific instructions how to connect to their Aspera servers.

   The following example shows a download of a *fastq* file from a remote server
   to a local directory :tt:`dir1`.  Command is broken with :tt:`\\` into multiple lines for readability:

   .. code-block:: console

      $ $HOME/.aspera/connect/bin/ascp  \
         -v \
         -P33001 \
         -i $HOME/.aspera/connect/etc/asperaweb_id_dsa.openssh \
         era-fasp@fasp.sra.ebi.ac.uk:vol1/fastq/SRR179/003/SRR1798143/SRR1798143.fastq.gz dir1/

   - ``-v``  use verbose mode
   - ``-P33001`` is the initial TCP connect port. Your server may need
     other port identified.  We have network settings to allow such high numbered ports to be opened for the transfer.
   - ``-i`` is the private key file created during the install.

   Any other flags will depend on the Aspera server setup.
   For additional help on usage:

   .. code-block:: console

      $ $HOME/.aspera/connect/bin/ascp -h

.. _globus data:

Using Globus
------------

If you need to transfer a large dataset (order of Tbs) we allow users to setup
**Globus Personal Connect** endpoints on one of our DTN nodes and transfer the
data using Globus. 
There are two DTN nodes that can be used:

  - dtn-1 
  - dtn-2


1. Login on the cluster as usual, then use ssh to login on one of the DTN nodes:

   .. code-block:: console

      [user@login-x:~]$ ssh dtn-1

2. Follow the instructions https://docs.globus.org/globus-connect-personal/install/linux/
   to set up personal Globus endpoint 

   Note, the prerequisites are already installed, you need to follow
   instructions for Gloubs Connect Personal download/install/configuration.
