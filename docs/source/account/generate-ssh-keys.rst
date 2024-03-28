:orphan:

.. _generate ssh keys:

Generate SSH keys
=================

We provide info here how to generate SSH keys on different laptops

.. contents::
   :local:

.. _generate-ssh-keys-linux:

Generate SSH keys on Linux
--------------------------

Follow the of the steps for :ref:`generating ssh keys on MacOS <generate-ssh-keys-mac>`
except in the first step use any terminal application that is available on your laptop.

.. _generate-ssh-keys-mac:

Generate SSH keys on MacOS
--------------------------

Here we assume your ``ssh`` is from OpenSSH, for other ssh versions please
use your specific software instructions.

To generate ssh keys on your laptop and to copy a public key to your account on the HPC3 cluster
do the following:

1. Open your :tt:`Terminal` application

.. image:: images/macos-terminal.png
   :align: center
   :alt: macos Terminal App


2. In the Terminal window check your ssh software is OpenSSH

   .. parsed-literal::

      :blue:`ssh -V`
      OpenSSH_8.6p1, LibreSSL 3.3.6
   
   The output shows **OpenSSH**, your version may differ depending on your
   installed ssh.

3. Create ssh keys 

   To create the keys, one needs to choose:

   - **name** for ssh keys files; this needs to be a single word with no spaces
   - **comment**  to add to the key; use your UCINetID
   - **very strong passphrase** must be used for protecting your SSH key;
     it can contain spaces, numbers and special characters and must be at least 10
     characters long. :red:`WARNING: Do not use empty passphrase!`

   In the following example we use the following choices:

   :name: key-to-hpc3
   :comment:  "panteater\@uci.edu (MacBook Air)"
   :passphrase:  you need to type it twice when prompted

   Execute the ``ssh-keygen`` command to create ssh keys:

   .. parsed-literal::

      :blue:`ssh-keygen -t rsa -f  ~/.ssh/key-to-hpc3 -C "panteater@uci.edu (MacBook Air)"`
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

   The above command will add a `:tt:`.ssh` folder in your $HOME and 
   generate two files there: a private key :tt:`key-to-hpc3`
   and a public key :tt:`key-to-hpc3.pub`. They are always
   generated and work as a pair. 

   .. attention:: | Private key should NEVER be shared. It remains on your laptop
                  | Use a non-empty passphrase for your key and remember it!

   Check your ssh keys:

   .. parsed-literal::

      :blue:`ls .ssh`
      key-to-hpc3     key-to-hpc3.pub
      :blue:`cat .ssh/key-to-hpc3.pub`
      ssh-rsa AAAA1yc2Ew...characters deleted...97VU0yRlaTxEX= panteater\@uci.edu (MacBook Air)


3. Transfer your public ssh key to HPC3

   Use ``ssh-copy-id`` command to copy your public key
   from your laptop to your account on HPC3.

   You will be prompted for the standard password and DUO authentication
   by this command. Use your UCINetID, here is an example session for user panteater:

   .. parsed-literal::

      :blue:`ssh-copy-id -i ~/.ssh/key-to-hpc3 panteater@hpc3.rcic.uci.edu`
      The authenticity of host 'hpc3.rcic.uci.edu (128.200.221.16)' can't be established.
      ED25519 key fingerprint is SHA256:KLY8s4Aq1JBrD8pCitYkn7MbZjUu6FOyUzgyuOevSuk.
      This key is not known by any other names
      Are you sure you want to continue connecting (yes/no/[fingerprint])?  :blue:`yes`
      /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
      /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
      (panteater\@hpc3.rcic.uci.edu) Password:  :red:`type your UCInetID password here`
      (panteater\@hpc3.rcic.uci.edu) Duo two-factor login for panteater

      Enter a passcode or select one of the following options:

       1. Duo Push to XXX-XXX-1234

      Passcode or option (1-1): 1

      Number of key(s) added:        1

      Now try logging into the machine, with:   "ssh panteater\@hpc3.rcic.uci.edu"
      and check to make sure that only the key(s) you wanted were added.

   The key will be placed into your HPC3 account in
   :tt:`$HOME/.ssh/authorized_keys` file.

.. _generate-ssh-keys-windows:

Generate SSH keys on Windows
----------------------------

Please use one of 

- `PuTTY/Pageant <https://winscp.net/eng/docs/ui_pageant>`_
- `Powershell <https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement>`_

Additional tutorials
--------------------

See :ref:`tutorials` for additional SSH-related reading. 
