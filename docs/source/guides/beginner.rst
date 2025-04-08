.. _beginner guide:

Beginner guide
===============

.. contents::
   :local:

This is a step by step beginner guide that explains how to get an account, to login,
and to do a few simple things on HPC3 cluster.

.. _your laptop:

Your Laptop
-----------

You will need to have a  few applications on your laptop, most are standard:

.. _laptop apps:

.. table:: Your laptop applications
   :class: noscroll-table

   +-----------------+-------------+-------------+---------------+--------------------------------+
   | **Application** |  Your laptop model                                                         |
   |                 +-------------+-------------+---------------+--------------------------------+ 
   | **Type**        | **Linux**   | **macOS**   | **Windows**   | **Windows 10**                 |
   +=================+=============+=============+===============+================================+
   |  VPN access     | Install client VPN software per the instructions |ucivpn|_                 |
   +-----------------+-------------+-------------+---------------+--------------------------------+
   |  Terminal       | use your    | Terminal or | |putty|_ or   | Windows Terminal, |mobaXterm|_ |
   |                 |             |             |               |                                |
   |                 | favorite    | |iTerm2|_   | |mobaXterm|_  | or |linsub|_                   |
   +-----------------+-------------+-------------+---------------+--------------------------------+
   |  Secure Connect | ssh         |  ssh        |               | ssh                            |
   +-----------------+-------------+-------------+---------------+--------------------------------+
   |  Secure Data    | scp         | scp         | Filezilla or  | scp  or rsync                  |
   |                 |             |             |               |                                |
   |  Transfer       | or rsync    | or rsync    | WinSCP        | (in |linsub|_)                 |
   +-----------------+-------------+-------------+---------------+--------------------------------+

.. attention::

   :red:`MobaXterm users DO NOT enable Remote monitoring!`
   See :ref:`MobaXterm <mobaxterm duo>` for more info.

Login
-----

| Before you login please make sure you have an account.  Please see :ref:`get account`.
| Once you have an account you can login to HPC3 cluster.
| HPC3 is a shared facility. Please read :ref:`acceptable use` guide.

The :tt:`HPC3` cluster name is :bluelight:`hpc3.rcic.uci.edu` and it should be used in all connections.

We require multi-factor authentication for all password-based logins.
Please make sure you have enabled your DUO device using `UCI’s Duo infrastructure
<https://www.oit.uci.edu/services/accounts-passwords/duo/>`_.

To directly login on :tt:`HPC3` cluster you must:

  * be connected to the UCI campus VPN (or be on the campus network)
  * use ``ssh`` command from your *Terminal* application
  * have a way to use DUO authentication

**Step 1**
  Connect to UCI campus VPN, see |ucivpn|_ instructions.

**Step 2**
  Open your Terminal application on your laptop and start ``ssh`` session
  to connect to the cluster login node.
  Use a cluster name and your your regular UCI credentials (UCInetID and
  password).  For example, a user with UCInetID *panteater* will use:

    .. code-block:: console

       $ ssh panteater@hpc3.rcic.uci.edu

    When prompted for a password enter your UCInetID password followed by :guilabel:`Return` key.
    Note, password will not be visible when typed:

    .. code-block:: console

	   Password:

**Step 3**
  After that, user will get a DUO prompt to enter a passcode 
  or request a push to the enrolled DUO-enabled device (user's phone).
  A prompt looks similar to:

    .. code-block:: text

       Duo two-factor login for panteater

       Enter a passcode or select one of the following options:

        1. Duo Push to XXX-XXX-1234

       Passcode or option (1-1):

  Type desired option (in this example *1*):

    .. code-block:: text

       Passcode or option (1-1): 1

  Now use the DUO app on your phone and respond to the received DUO
  notification by pressing :guilabel:`Approve` when prompted.
  If the DUO authentication is successful you will see in your laptop window:

    .. code-block:: text

       Success. Logging you in...

  And after a successful login you will see a screen similar to the following:

    .. code-block:: text
  
       +-----------------------------------------+
       |  _             _             _ _ ____   |
       | | | ___   __ _(_)_ __       (_) | ___|  |
       | | |/ _ \ / _` | | '_ \ _____| | |___ \  |
       | | | (_) | (_| | | | | |_____| | |___) | |
       | |_|\___/ \__, |_|_| |_|     |_|_|____/  |
       |          |___/                          |
       +-----------------------------------------+
        Distro:  Rocky 8.7 Green Obsidian
        Virtual: NO

        CPUs:    40
        RAM:     191.8GB
        BUILT:   2022-08-30 14:02

        ACCEPTABLE USE: https://rcic.uci.edu/documents/RCIC-Acceptable-Use-Policy.pdf

        [panteater@login-i15:~]$

    The above text output screen  is called :term:`motd`. It
    includes a general information about the cluster login node (we have a few) plus important
    messages about the cluster such as pending shutdowns or links to important online documents.

    The last line of the output is your *shell prompt* (yours may look slightly different),
    this is where you can type commands.

File editing
------------

Users will need to learn one of file editors: ``vim`` or ``emacs``.
Choose the editor that is more intuitive for you.
See the :ref:`editors` beginner tutorials, many more are available online.

.. important:: Please avoid using :ref:`special characters` in file and directory names.

Simple commands
---------------

Users who are unfamiliar with Linux environment will need to learn
the basics of *bash shell*, file editing, or using language such as R or Python.
Please see the :ref:`tutorials` page that lists links to various beginner guides.

The cluster shell :tt:`bash` is a command language interpreter that executes
commands that you type (the standard input). Bash shell automatically provides a prompt
which is a text similar to |prompt| and is usually the username followed by the hostname.
You don't need to type prompt.

Below is a small set of simple but very useful commands to try. What you type
is immediately after the prompt |prompt|.
Each command returns an output that will be displayed in your terminal window
and will be similar to the following:

Print name of current/working directory:

  .. code-block:: console

     [user@login-x:~]$ pwd
     /data/homezvol0/panteater

Print current date and time in default format:

  .. code-block:: console

     [user@login-x:~]$ date
     Mon May 19 12:43:42 PDT 2023

Print host name:

  The cluster has  a few login nodes and multiple working nodes, each has its own unique name.

  .. code-block:: console
  
    [user@login-x:~]$ hostname
    login-i15

List current directory contents:

  .. code-block:: console

     [user@login-x:~]$ ls
     local

Long list using :tt:`-l` option:

  Lists all directory contents including hidden files that start with dot :tt:`.`
  and info about each file.

  .. code-block:: console

     [user@login-x:~]$ ls -l
     drwx------   3 panteater panteater    9 Jul 13 00:02 .
     drwxr-xr-x 785 root      root       785 Jul 16 10:32 ..
     -rw-r--r--   1 panteater panteater  183 Jul 12 14:42 .bash_profile
     -rw-r--r--   1 panteater panteater  541 Jul 12 14:42 .bashrc
     -rw-r--r--   1 panteater panteater  500 Jul 12 14:42 .emacs
     -rw-r--r--   1 panteater panteater   17 Jul 12 14:42 .forward
     drwxrwxr-x   2 panteater panteater    2 Jun 15 09:48 local


By default, many commands need no arguments or additional flags.
Arguments given to the commands provide more
specific information in the output, as the last command ``ls -l`` did.

To learn about specific commands consult tutorials or use manual pages via
``man`` command. For example to learn more about ``ls`` command type:

  .. code-block:: console

     [user@login-x:~]$ man ls

  and use the :guilabel:`space` key to scroll through the output on the screen.

Running applications
--------------------

**Please follow** :ref:`conduct rules` **to avoid problems**.
Cluster is a shared resource, at any time there are many users logged in 
and hundreds of jobs are running. What you do can adversely affect others.

The cluster environment **is not well suited for GUI type of applications**.
Most of the commands users need to type in, there are no clickable icons and
no pop-up windows.

We use Slurm scheduler to run CPU-intensive or long running applications.
:ref:`Slurm guide <slurm manager>` provides extensive info about using the scheduler.
Here is a brief summary:

 *  Slurm is an open-source workload manager for Linux clusters that manages
    and schedules jobs on the cluster. 
 * HPC3 has different kinds of nodes (servers) that are separated into groups according to
   their resources (memory, CPU, etc).  Slurm uses the term :tt:`partition` to signify a group
   of such resources. All jobs are submitted to the nodes in :tt:`partitions`.

We have a few partitions, most users will need to use:

 * *free partition* is for jobs that can be preempted (killed) by standard
   jobs. There are no charges for using this partition.
 * *standard partition* is for jobs that should not be interrupted.
   Usage is charged against:

    * The user's Slurm bank account. Each user gets FREE one time allocation of 1000 core hours to run jobs here.
      **Users are NOT CHARGED FOR this allocation**, but it can not be extended or renewed.
    * If all allocation is used, users can run jobs in this partition only if they are associated with
      labs that have core hours in their Slurm lab banks. Usually, Slurm lab bank is a PI lab account.

Using  interactive job
^^^^^^^^^^^^^^^^^^^^^^^

``srun``

To request an interactive job, use the ``srun`` command.
Interactive does not mean *instantaneous*, the scheduler still needs to
check for available resources and balance users and jobs.

**To start an interactive session**

  You can use one of these example methods :

  1. Run job in standard partition, your default Slurm bank account will be charged.

     .. code-block:: console
  
        [user@login-x:~]$ srun --pty /bin/bash -i
        srun: job 37382052 queued and waiting for resources
        srun: job 37382052 has been allocated resources
        [user@hpc3-l18-04:~]$

  2. Run job in free partition, your default Slurm bank account will not be charged.

     .. code-block:: console
  
        [user@login-x:~]$ srun -p free --pty /bin/bash -i
        srun: job 37382053 queued and waiting for resources
        srun: job 37382053 has been allocated resources
        [user@hpc3-16-04:~]$

  3. Run job in standard partition using *panteater_lab account* (you must have an access to it).
     Your Slurm lab account will be charged.

     .. code-block:: console
  
        [user@login-x:~]$ srun -A panteater_lab --pty /bin/bash -i
        srun: job 37382054 queued and waiting for resources
        srun: job 37382054 has been allocated resources
        [user@hpc3-19-01:~]$

  After you execute the command, Slurm will put you on a compute node (when it is available)
  and you will see a new shell prompt in the terminal window.
  Now you can interactively run your applications and commands from the command line.

**To stop an interactive session**

  After you are done, logout from interactive node.
  This will end your Slurm interactive session and you will return to the
  terminal window on the login node:

  .. code-block:: console

     [user@hpc3-l18-04:~]$ logout
     [user@login-x:~]$ 


Using batch job
^^^^^^^^^^^^^^^

``sbatch``

A batch job is run by the scheduler at sometime in the future and the
scheduler picks an available time and node. Usually, it is within minutes,
or as soon as requested resources become available. Slurm balances resource usage among
many users and many jobs. If you are requesting resources that are not readily
available you may have to wait longer.

Slurm batch jobs can be submitted to the same partitions as interactive jobs.
A user needs to use:

  * ``sbatch`` command
  * *Slurm submit script* which is a text file that specifies:

    * the directives to Slurm what resources are needed for the job
    * commands that the jobs needs to execute

:bluelight:`Example sbatch job`
  In the steps below you will download an example Slurm submit script, Python example
  program, then submit a job to the scheduler and check its output.
  All commands are executed on the cluster after you login.

  **Step: download example files**
    Files are downloaded from our web server to your user area that is allocated to you on the cluster.
    The submit script and Python program don't need any editing after the download.
    Type all 4 commands exactly as they are shown (text after the prompt).

    1. Change directory to your DFS user area, here :tt:`$USER` is a shortcut for your UCInetID.

       .. code-block:: console

          [user@login-x:~]$ cd /pub/$USER

    2. Download Slurm submit script and save it as :tt:`firstjob.sub` file

       .. code-block:: console

          [user@login-x:~]$ wget https://rcic.uci.edu/_static/examples/firstjob.sub

    3. Download Python code and save it as :tt:`days.py` file. It is a
       simple Python program that prints today's date and a random day 1-365 days in the past.

       .. code-block:: console

          [user@login-x:~]$ wget https://rcic.uci.edu/_static/examples/days.py

    4. Show the content of the Slurm script in the Terminal window.

       .. code-block:: console

          [user@login-x:~]$ cat firstjob.sub


  **Step: submit job to Slurm scheduler**
    .. code-block:: console

       [user@login-x:~]$ sbatch firstjob.sub
       Submitted batch job 5776081

    The output shows that script was submitted as a job with ID 5776081.
    All job IDs are unique, yours will be different and the output file name of
    your job will reflect a different ID.

  **Step: Check the job status and output file**
    This test job will run very quickly (fraction of a second) because it
    executes a few very fast commands and has no computational component.

    Check the status of your job.

      .. code-block:: console

         [user@login-x:~]$ squeue -u $USER
         JOBID   PARTITION   NAME  USER  ACCOUNT ST   TIME  CPUS NODE NODELIST(REASON)

      When the output is a single line as shown, the job is finished, otherwise
      there would be info about your job in the output.

    List the files in the current directory.

      .. code-block:: console

         [user@login-x:~]$ ls
         firstjob.5776081.err  firstjob.5776081.out  firstjob.sub

      There are now error and output files produced by the Slurm job as was requested in the submit script.
      Your file names will reflect your Slurm job ID.


    Show the contents of the output file in the Terminal window.

      .. code-block:: console

         [user@login-x:~]$ cat firstjob.5776081.out
         Running job on host hpc3-l18-05
         Today is 2021-07-23 and 325 days ago it was 2020-09-01

    .. note:: Alwya check your slurm output and error files. They provide
	          information about your job.

Storage
-------

The filesystem storage is generally in 3 areas.
Please use the links below for detailed information about each filesystem.

.. important:: All filesystems have storage quotas.
               Check quotas on regular basis after adding or removing a lot of files,
               transferring data or running computational jobs that create a lot of files:

:ref:`home`
  | All users have 50GB quota :tt:`$HOME` area.
    The :tt:`$HOME` is in :tt:`/data/homezvolX/UCInetID`.
    Use it for storing important and rarely changed files.
  | :ref:`How to check $HOME quotas <home check quotas>`

:ref:`dfs`
  * All users have 1Tb quota :tt:`/pub/UCInetID` private area.
    Use it for storing data sets, documents, Slurm scripts and jobs input/output.
  * Depending on a lab affiliation, some users may have space in
    additional DFS areas (:tt:`/dfs7`, etc). This area is accessible by all
    members of the lab.

  :ref:`How to check DFS quotas <dfs check quotas>`
  
:ref:`crsp`
  | :red:`By default users don't have access to this area`.
    Depending on a lab affiliation, some users may have space in
    :tt:`/share/crsp/lab/labname/UCInetID`. Please see :ref:`getting crsp account` for details.
  | :ref:`How to check CRSP quotas <crsp check quotas>`

Transferring files
------------------

Often users need to brings data from other servers and laptops.
To transfer data one needs to use ``scp`` (secure copy) or ``rsync`` (file copying tool).
Please see detailed :ref:`data transfer` examples.

Alternatively, one can use graphical tools on their laptops (FileZilla, MountainDuck, or WinSCP)
to transfer files between a local laptop and the cluster.
Please follow  each program instructions how to do this.

In all of the transfer application you will need to use :bluelight:`hpc3.rcic.uci.edu`
as a remote server (where you want to transfer your files to/from) and use
your UCInetID credentials for your user name and password.

**Simple examples of file transfers with scp:**
  The ``scp`` command is used to transfer files and directories  between a local
  laptop and a remote server. The command has a simple structure:

  .. code-block::

     scp OPTIONS SOURCE DESTINATION

  | We omit OPTIONS for the simple cases.
  | The SOURCE and DESTINATION may be specified as a local file name, or
    a remote host with optional path in the form :proposed:`user`:red:`@server:`:blue:`path` where

    | :proposed:`user` is your account on a cluster
    | :red:`@server:` is the server name delimited with 2 special characters,
    |        :red:`@` separates user name from server name
    |        :red:`:` separates server name from path name
    | :blue:`path` is a file path name on the server, can be made explicit using absolute or relative names:
    |        **absolute** or full file name :tt:`/Users/someuser/project1/input/my.fasta` on your laptop
    |        **relative** file name is :tt:`my.fasta` when used from the directory where this file is located.

  1. Transfer a single file to HPC3

     Transfer file :tt:`myfile.txt` from a local laptop to HPC3 and put
     it in the directory :tt:`/pub/panteater`.
     On your laptop, use a *Terminal app* and descend into the directory where your file is
     located, then execute the ``scp`` command (use your UCInetID):
  
     .. code-block:: console
  
        scp myfile.txt panteater@hpc3.rcic.uci.edu:/pub/panteater
  
  2. Transfer a single file from HPC3 to a local laptop

     On your laptop, use a *Terminal app* and descend into the directory where you
     want to put the transferred file, then execute the ``scp`` command (use your UCInetID):
  
     .. code-block:: console
  
        scp panteater@hpc3.rcic.uci.edu:/pub/panteater/project1/j-123.fa j-123.fa
  
  3. Transfer multiple files from your laptop to HPC3:
  
     .. code-block:: console
  
        scp f1.py f2.py doc.txt panteater@hpc3.rcic.uci.edu:/pub/panteater
  
  4. Transfer a directory with all its content from HPC3 to a local laptop

     On your laptop, use a *Terminal app* and descend into the directory where you
     want to put the transferred directory and its content, then execute the ``scp`` command (use your UCInetID).
     Note, the single dot character at the end means *copy to this current directory*:
  
     .. code-block:: console
  
        scp -r panteater@hpc3.rcic.uci.edu:/pub/panteater/results .

Logout
------

You can run many commands and submit many jobs.
After you are done with your work you need to logout from the cluster
using ``logout`` or ``exit`` command, for example:

.. code-block:: console

   [user@login-x:~]$ logout


.. |iterm2| replace:: iTerm2
.. _`iTerm2`: http://www.iterm2.com

.. |putty| replace:: PuTTY
.. _`putty`: http://www.chiark.greenend.org.uk/~sgtatham/putty

.. |mobaXterm| replace:: MobaXterm
.. _`mobaXterm`: https://mobaxterm.mobatek.net

.. |linsub| replace:: Linux Subsystem for Windows
.. _`linsub`: https://docs.microsoft.com/en-us/windows/wsl/install-win10

.. |ucivpn| replace:: UCI campus VPN
.. _`ucivpn`: https://www.oit.uci.edu/help/vpn

.. |prompt| replace:: :navy:`[user@login-x:~]$`
