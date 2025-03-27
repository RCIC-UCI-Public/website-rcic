.. _unix primer:

UNIX primer
===========

.. contents::
   :local:

The information is intended for **new HPC3 users** and
for **users that are new to Linux/UNIX-like operating systems.**
Please consult the rest of the user guides for information that is not covered here.

This page contains info to provide some familiarity with Linux/UNIX
but it is not an exhaustive guide.

.. _bash init files:

Bash init files
---------------

A shell is a program that acts as an interface between the user and the operating system's kernel,
allowing users to type and execute commands and interact with the system.

On HPC3 the default shell is `bash` and it uses 2 initialization files.
Both files are located in your :tt:`$HOME` directory
and are provided with the default settings when your account is created.
Both files start with *dot* which makes them *invisible* to a regular ``ls`` command.

:bluelight:`.bash_profile`
  Is the initialization file executed only for login shells.
  Anything you want to run when you log in, you put in :tt:`.bash_profile`.
  A default one is sufficient for nearly all users and has the following content:

    .. code-block:: bash

       # .bash_profile
       # Get the aliases and functions
       if [ -f ~/.bashrc ]; then
             . ~/.bashrc
       fi

       # User specific environment and startup programs

       PATH=$PATH:$HOME/bin
       export PATH

  Best practices:
   * it should be a very small file, keep changes here to a bare minimum
   * It will source :tt:`.bashrc` by default so you don't have to duplicate any commands you want to run for every shell.

:bluelight:`.bashrc`
  Is the initialization file executed every time a user starts a new shell.
  It includes all customizing of your shell environment with aliases, functions, environment variables, etc.

  What to put in this file:
    * aliases - shortcuts to the commands
    * environment variables that affect your shells and applications
    * history configuration
    * terminal color scheme
    * prompt configuration

  :red:`Do not put in this file:`
    * module load/unload commands
    * conda init commands, see :ref:`install conda` section to learn how to use them

  Best practices:
   * Keep your file clean and concise
   * Consider using separate files for different types of customizing that can be sourced when needed.
   * Use a text editor ``vim`` or  ``nano`` to modify your :tt:`.bashrc` file.
   * Before editing make a copy of your current file so you can revert to it if your edits go wrong.
   * Reload your file after editing for the changes to take an affect:

     .. code-block:: console

	    [user@login-x:~]$ . ~/.bashrc

  Example file:
    .. code-block:: console

       # Source global definitions
       if [ -f /etc/bashrc ]; then
            . /etc/bashrc
       fi

       alias rm='rm -i'
       alias c='clear'
       alias h='history'
       alias la='ls -la'
       alias pub="cd /pub/$USER"
       alias crsplab="cd /share/crsp/lab/PI-LAB/share/"
       alias saccf="export SACCT_FORMAT='JobID%20,JobName,User,Partition,NodeList,Start,End,Elapsed,State,ExitCode,MaxRSS,AllocTRES%32'"

       # set prompt color
       host=`hostname -s`
       PS1="\[\033[01;36m\]\\h \!% \[\e[0m\] "

       export VISUAL=vi
       export EDITOR=emacs
       export CLICOLOR=true
       export MYPUB=/pub/$USER
       export biojhub4HOME="/pub/$USER/biojhub4_dir"

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

.. _symbolic links:

Symbolic Links
--------------

Symbolic links, also known as soft links or symlinks, are special types of files that point
to other files. The data in the target file does not appear in a symbolic link, instead, it
points to another file system entry.

While symbolic links can be  a practical choice, sometimes they can have a significant, adverse impact on performance

*Appropriate use:*
  * When making shortcuts for the names between the files on the same filesystem.

  * When making shortcuts from a local file system to a remote file (networked) file system,
    for example :tt:`/pub -> /dfs6/pub`

:red:`Should not be used:`
  * Symbolic links between any two **networked** file systems.

  As an example of inappropriate use suppose you define a *convenience* link
  from your home area :tt:`$HOME` to your PI's CRSP lab area as:

  .. code-block:: console

     $ ls -l crsplab
     crsplab -> /share/crsp/lab/pilab

  In this scenario,

  #. Every file operation that uses :tt:`$HOME/crsplab` as part of its path must first go to the NFS server
     that provides $HOME.
  #. The NFS home server then redirects to CRSP server and a **second** network transaction is made for the CRSP server.

  Essentially, this kind of *convenience* link forces the home
  area server to be in the middle, doing completely useless work that can have significant impact on the
  home area server *and* on your code running on a cluster node.

  **CRSP** and **DFS** servers are  designed to handle high-volumes of traffic, while the home area server is not.

  .. attention:: | :red:`Do not create symbolic links between $HOME and CRSP or DFS!`
                 | Use aliases or environment variables in place of symbolic links when
                 | you are making shortcuts for the file names in different filesystems.


**Use aliases or environment variables**

A shortcut  name can be accomplished via an alias or an environment variable.
For example, in your :tt:`.bashrc` add

.. code-block:: bash

   alias crsplab='cd /share/crsp/lab/pilab'
   export CRSPLAB=/share/crsp/lab/pilab

Then use either an alias or a variable depending on your task.
When need to change to your CRSP lab area can simply execute one of the
following commands (they are equivalent):

.. code-block:: bash

   $ crsplab
   $ cd $CRSPLAB

When need to list contents  of your CRSP lab area:

.. code-block:: bash

   $ ls $CRSPLAB

For using aliases and environment variables in your Slurm jobs please see
:ref:`using aliases`.

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

.. _ssh guide:

SSH keys
--------

You must either be on the campus network or connected to the
`UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ to access HPC3.

.. _keys concepts:

Keys Concepts
^^^^^^^^^^^^^

A high-level  understanding of how things work will enable you to better secure your own logins
SSH uses :tt:`Public Key Cryptography` and :tt:`challenge/response` to negotiate secured sessions.

What do these terms really mean?

* :tt:`Public Key Cryptography` - text or data can be encrypted using the public key of the recipient.  The recipient then
  uses the matching private key to decrypt the message.
* :tt:`Challenge/Response` - the ssh server (e.g., HPC3) encrypts a message using your public ssh key and **challenges** your
  client on your laptop to decrypt it and send back a **response** based on the contents. If you can successfully respond to the
  *]*challenge**, the ssh server considers you authenticated.
* :tt:`Passphrase` - a password associated with your ssh key pair


The figure below shows where your SSH private key and
public keys are located. The server encrypts the **challenge** with YOUR public key.
You type in your passphrase to your private key each time you login.


.. figure:: images/challenge-response-ssh.png
   :align: center
   :width: 60%
   :alt: ssh challenge response

   SSH Keys Challenge Response

**The Algorithm Steps**:

  1. User **requests to login**.
  2. Server creates a random code and *encrypts* the code with the user's
     *ssh public key* and sends it back to the user - **challenge**.
  3. User *decrypts* the *challenge* with the user's *private ssh key*. To do
     it, need to type in the passphrase to that key. The now-decrypted *challenge* is used
     to create a valid response message. That message is digitally signed with the *private key*  and
     is then sent back to the server -  **response to challenge**.
  4. The server uses the user's public key to verify the authenticity and content of the message.
     If the *response* matches the *challenge*, then **access is granted otherwise it is denied**.


**Takeaways**

* Your private SSH key should never leave your laptop
* You should always use a strong password (passphrase) on your private ssh key
* This password should be different than all of your other passwords
* You need to type in your password each time you login

.. _ssh agent:

Ssh-agent
^^^^^^^^^

If you have access to your private key and use it to *respond* to HPC3's *challenge*,
you need to type in the passphrase to that key for success.

**Ssh-agent enables you to load the key into the agent with a passphrase and have the agent
respond to login challenges for you.**

In essence, you type in private key passphrase once when loading your local agent
and then the agent responds for you.  In this scenario, you enter your the passphrase to your private key once.

.. figure:: images/challenge-response-ssh-agent.png
   :align: center
   :width: 60%
   :alt: ssh challenge response agent

   SSH Challenge Response with Agent

**The algorithmic steps**:

  1. User **starts an ssh agent** then enters once the password to ssh key to activate the agent
  2. User **requests to login**
  3. Server creates a random code and *encrypts* the code with the user's *ssh public key*
     and sends it back to the user - **challenge**
  4. Ssh agent *decrypts* the *challenge* with the user's *private ssh key*,
     uses *decrypted challenge* to create a valid response message, digitally signs it
     with the *private key* and sends it back to the server - **response**.
  5. The server uses the user's public key to verify the authenticity and content of the message.
     If the *response* matches the *challenge*, then **access is granted otherwise it is denied**


**Takeaways**

* Using ssh-agent reduces the number of times you enter a password from the keyboard
* When you reboot your laptop (or logout), the agent is wiped from memory


.. _ssh-sgent windows:

Ssh-agent & Windows
^^^^^^^^^^^^^^^^^^^

With the general background of how ssh-agent functions,
Microsoft **Windows 10/11** has two commonly-used ssh-agent mechanisms:

1. *Ssh-agent* running in Microsoft *Powershell*
2. *Putty ssh client* that uses *putty-gen* to create a public/private key
   pair and *pageant* as the ssh-agent.

Please see :ref:`ssh agents guides listing<ssh keys>`.


.. _ssh troubleshooting:

Troubleshooting
^^^^^^^^^^^^^^^

There are many online guides for ssh, please sea
:doc:`SSH</guides/tutorials>` links.
