:orphan:

.. _generate ssh keys:

Generate SSH keys
=================

In the information provided here shows you how to generate SSH keys on different laptops
and then copy a public key to your account on the HPC3 cluster. If you have reached this
guide wanting to use :ref:`CRSP <crsp>`, many of the steps are identical. The main difference
is in the step of *copying public keys*.  CRSP uses :ref:`this procedure <manage crsp keys>` for that step.


.. attention::

   In the guides below  ``key-to-hpc3`` is used as a key name. This is only an *example* key name. You can use whatever
   you want that makes sense to you.  For example, you could use ``key-to-crsp`` if creating a key pair to use with
   :ref:`CRSP <crsp>`
   

**FAQS for Key Generation**

What is being created?
    You are generating an ssh *key pair*.  The pair is two parts: a private key, and a public key.
    The private part remains on your laptop. The public key is copied to the remote system.

Where is the key pair stored?
     The key pair is really two text files. These files are usually stored in the ``.ssh`` subdirectory for your
     $HOME directory on *your* laptop or desktop

What's the difference between a passphrase and a password?
     A passphrase is used to unlock the *private part* of a key pair.  Choose a phrase that is unique (i.e., don't
     use your UCINetID password).  A password is interepreted by the remote system and must therefore be sent
     over the network to be verified. The passphrase is local and is never
     transmitted over the network.

What do I do if I lose/forget my passphrase?
     Follow the procedure below to generate a *new* key pair and upload the *public* part of the new key. Finally,
     destroy the old private key.

Do I share the private part of my key?
     No. Never. The private part ( a file on your local system) should never leave your laptop. It doesn't need to be
     backed up.  If it is lost, you can always generate a new pair.

How does the remote system accept my key?
     Short answer:  Public key cryptography with challenge/response.   A little more information: Using Password+DUO,
     you have placed the public key on the remote server in an ``authorized_keys`` file.  When you log in,
     your client presents the *public key* to the server.  The server then *challenges* your client to prove that you
     have the private key.  It does this by encrypting a message that can only be decrypted using the private key.  If
     you can respond with contents of that challenge, then the server accepts your identification.

What if somebody gets a copy of my public key?
     Nothing to worry about. Public key cryptography means that security is not compromised if the public key were
     exposed. 

Can I use the same key pair to authenticate to both HPC3 and CRSP?
    Technically, yes. But it is recommended that you create a unique key pair for each remote system. 
    Each key pair should have its own unique password.

Can I omit the passphrase when creating my key pair?
    This is a violation of UCI password security rules.  While you can create a passwordless key, you never should.

CONTENTS
========

.. contents::
   :local:

.. _generate-ssh-keys-mac:

Generate SSH keys on macOS
--------------------------

We assume your ``ssh`` is from OpenSSH, for other ssh distributions please
use your specific software instructions.

1. Open your :tt:`Terminal` application

   .. figure:: images/macos-terminal.png
      :align: center
      :alt: macOS Terminal App

      Open macOS Terminal App

#. In the Terminal window check your ssh software is OpenSSH

   .. parsed-literal::

      :blue:`ssh -V`
      OpenSSH_8.6p1, LibreSSL 3.3.6
   
   The output shows *OpenSSH*, your version may differ depending on your
   installed ssh.

#. Create ssh keys 

   To create the keys, one needs to choose:

   - **name** for ssh keys files; this needs to be a single word with no spaces
   - **comment**  to add to the key; use your UCINetID
   - **very strong passphrase** must be used for protecting your SSH key.
     It can contain spaces, numbers and special characters and must be at least 10
     characters long. :red:`WARNING: Do not use empty passphrase!`

   In the following example we use the following choices:

   :name: key-to-hpc3
   :comment:  "panteater\@uci.edu (MacBook Air)"
   :passphrase:  you need to type it twice when prompted

   Execute the ``ssh-keygen`` command to create **RSA type** ssh keys.
   Use your UCINETID in place of *panteater*:

   .. parsed-literal::

      :blue:`cd ~/.ssh`
      :blue:`ssh-keygen -t rsa -f  key-to-hpc3 -C "panteater@uci.edu (MacBook Air)"`
      Generating public/private rsa key pair.
      Created directory '/Users/panteater/.ssh'.
      Enter passphrase (empty for no passphrase):
      Enter same passphrase again:
      Your identification has been saved in /Users/panteater/.ssh/key-to-hpc3
      Your public key has been saved in /Users/panteater/.ssh/key-to-hpc3.pub
      The key fingerprint is:
      SHA256:KLY8s4Aq1JBrD8pCitYkn7MbZjUu6FOyUzgyuOevSuk panteater@uci.edu (MacBook Air)
      The key's randomart image is:
      +---[RSA 3072]----+
      \|*=T=.            |
      \|*.o*.            |
      \|=.1.  o          |
      \|== o + .         |
      \|B.X * o S        |
      \|=E B o o o       |
      \|=.  o . .        |
      \|.+oo             |
      \|==. .            |
      +----[SHA256]-----+

   The above command will add a :tt:`.ssh` directory (directory is another name for folder)
   in your :tt:`$HOME` directory and generate two files there: a private key :tt:`key-to-hpc3`
   and a public key :tt:`key-to-hpc3.pub`. They are always generated and work as a pair. 

   .. _generate PEM-formatted keys:

   .. attention::
      | If you are creating ssh key pair for CRSP desktop client use the modified command
      | ``ssh-keygen`` shown below to create **PEM-formatted keys**.

      | PEM-formatted keys are the most reliable format for the :ref:`CRSP Desktop Client <crsp clients>`. 
      | The command is essentially identical to the one above but adds an explicit format and the :tt:`.pem` file extension. 

      | replace:
      | :blue:`ssh-keygen -t rsa -f  key-to-hpc3 -C "panteater@uci.edu (MacBook Air)"`
      | with:
      | :blue:`ssh-keygen -t rsa -f  key-to-hpc3.pem -m PEM -C "panteater@uci.edu (MacBook Air)"`

      This will create files :tt:`key-to-hpc3.pem` (private key) and :tt:`key-to-hpc3.pem.pub` (public key)

#. Check your ssh keys. The first command simply lists the contents of your
   :tt:`.ssh/` directory, and the second prints  the contents of your public
   RSA type ssh key:

   .. parsed-literal::

      :blue:`ls ~/.ssh`
      key-to-hpc3     key-to-hpc3.pub

      :blue:`cat ~/.ssh/key-to-hpc3.pub`
      ssh-rsa AAAA1yc2Ew...characters deleted...97VU0yRlaTxEX= panteater\@uci.edu (MacBook Air)

   .. important:: | Private key should NEVER be shared. It remains on your laptop.
                  | Alwyas use a non-empty passphrase for your key and remember it!

#. Transfer your public ssh key

   Once your keys are generated you will need to copy the contents of your public
   key to the desired server. See :ref:`copy-ssh-keys-macos`.


.. _generate-ssh-keys-linux:

Generate SSH keys on Linux
--------------------------

Follow the of the steps for :ref:`generating ssh keys on macOS <generate-ssh-keys-mac>`
except in the first step use any terminal application that is available on your laptop.
Once your keys are generated you will need to copy the contents of your public
key to the desired server. See :ref:`copy-ssh-keys-macos`.

.. _generate-ssh-keys-windows-powershell:

Generate SSH keys on Windows in Powershell
------------------------------------------

Follow the of the steps for :ref:`generating ssh keys on macOS <generate-ssh-keys-mac>`
except in the first step use Powershell that is available on your laptop.
Once the keys are generated you will need to copy to the contents of your
public key to the desired server.  See :ref:`copy-ssh-keys-windows` below.

.. _generate-ssh-keys-windows-putty:

Generate SSH keys on Windows with PuttyGen
------------------------------------------

`PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_ is a very common terminal program used on 
Windows laptops and desktops.  Other software that can use key-based authentication can also use keys generated by 
PuTTYgen.   This tutorial assumes that you have downloaded and installed PuTTY, Pageant, PuTTYgen (using their MSI-based
installer is the simplest method)

1. Open PuTTYgen from the Windows Start Button to see the following screen and
   press the :guilabel:`Generate` button

   .. figure:: images/puttygen-initial.png
      :align: center
      :width: 90%
      :alt: PuTTYgen start screen
      :class: addpadding

      PuTTYgen start screen

#. Assign a passphrase and save both the public and private key.   

   .. figure:: images/puttygen-passphrase.png
      :align: center
      :width: 90%
      :alt: PuTTYgen assign passphrase and save
      :class: addpadding

      PuTTYgen assign passphrase and save

   .. note::

      A reasonable pattern for your private key name :tt:`ucinetid-to-hpc3` and :tt:`ucinetid-to-hpc3.pub` for the public key. 
      replace *ucinetid* with your specific id, e.g., *panteater*.

   The private key file is of type *ppk* for PuTTY Private Key.
   The private key should remain on your laptop. 
   You will need to copy to the contents of your *public* key to the server. 
   See section :ref:`copy-ssh-keys-windows` below.

.. _copy-ssh-keys-macos:

Copy SSH public keys from macOS
-------------------------------

.. warning::

   If you need to transfer ssh keys to CRSP, follow the
   guide for :ref:`Managing Keys on CRSP <manage crsp keys>` 

To transfer the keys to HPC3:

1. Use ``ssh-copy-id`` command to copy your public key
   from your laptop to your account on HPC3.

   You will be prompted for the standard password and DUO authentication
   by this command.  Here is an example session for user panteater, **use
   your UCINETID** in its place:

   .. parsed-literal::

      :blue:`ssh-copy-id -i ~/.ssh/key-to-hpc3 panteater@hpc3.rcic.uci.edu`
      The authenticity of host 'hpc3.rcic.uci.edu (128.200.221.16)' can't be established.
      ED25519 key fingerprint is SHA256:KLY8s4Aq1JBrD8pCitYkn7MbZjUu6FOyUzgyuOevSuk.
      This key is not known by any other names
      Are you sure you want to continue connecting (yes/no/[fingerprint])?  :blue:`yes`
      /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
      /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
      (panteater\@hpc3.rcic.uci.edu) Password:  :red:`type your UCInetID password`
      (panteater\@hpc3.rcic.uci.edu) Duo two-factor login for panteater

      Enter a passcode or select one of the following options:

       1. Duo Push to XXX-XXX-1234

         Passcode or option (1-1): :blue:`1`

       Number of key(s) added:        1

       Now try logging into the machine, with  :blue:`ssh panteater@hpc3.rcic.uci.edu`
       and check to make sure that only the key(s) you wanted were added.

   The content of your public key will be added to :tt:`$HOME/.ssh/authorized_keys` file
   in your HPC3 account.

#. Create key mapping 

   This task is done on your laptop once for generated ssh keys pair.

   Your ssh keys are stored in the default directory but they have
   non-default names. We need to add newly generated key's name to the ssh
   configuration file to let the ssh commands know what keys to use when
   connecting to HPC3 cluster.

   Create :tt:`~/.ssh/config` file with your choice of editor and add the following:

   .. parsed-literal::

      Host hpc3.rcic.uci.edu 
        IdentityFile ~/.ssh/key-to-hpc3

   The :tt:`~/ssh/config` is a user's ssh configuiration file that is used  by ssh commands.
   The added content tells ssh to use this specific ssh key when connecting to HPC3.

.. _copy-ssh-keys-windows:

Copy SSH Public Key From Windows
--------------------------------

.. warning::

   If you need to transfer ssh keys to CRSP, follow the
   guide for :ref:`Managing Keys on CRSP <manage crsp keys>`.

To transfer the keys to HPC3:

Since Windows does not have the convenience of ``ssh-copy-id``, one has to type a bit more.  The following can be run 
from either a *Command window* or a *Powershell window* to place the key :tt:`panteater-to-hpc3.pub` in the appropriate place.

.. parsed-literal::

   C:\> :blue:`type .\\panteater-to-hpc.pub | ssh panteater@hpc3.rcic.uci.edu "cat >> .ssh/authorized_keys"`
   (panteater\@hpc3.rcic.uci.edu) Password: :red:`type your UCInetID password`
   (panteater\@hpc3.rcic.uci.edu) Duo two-factor login for panteater

   Enter a passcode or select one of the following options:
   
   1. Duo Push to XXX-XXX-1234
   
   Passcode or option (1-1): :blue:`1`

   C:\>

The content of your public key will be added to :tt:`$HOME/.ssh/authorized_keys` file
in your HPC3 account.


.. _additional tutorials:

Additional tutorials
--------------------

See :ref:`tutorials` for additional SSH-related reading. 
