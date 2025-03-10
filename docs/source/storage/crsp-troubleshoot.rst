.. _crsp troubleshoot:

CRSP Troubleshooting
====================

.. contents::
   :local:

Please note that RCIC does not provide Windows OS or macOS support for the campus.
If there is an operating system related issue, RCIC will refer you to you get support
to address your systems issue first before installing CRSP Desktop.

The following sections have information on how to solve most common problems.
If you continue having issues after reading the guide below please see :ref:`submit ticket` a ticket.

.. _problem install:

CRSP Desktop install problems
-----------------------------

.. _problem mac install:

On macOS
^^^^^^^^

If you are having issues installing *CRSP Desktop*, please check the following:

1. Make sure your system meets minimal requirements listed in the :ref:`client desktop mac`.
2. Make sure you have Admin rights in your system. If your system is managed by OIT,
   ask your support team to give you Admin rights.
3. In :guilabel:`Applications`, check for *CRSP Desktop* (*Mountain Duck*).
   If found, drag the App to trash, and retry installation using RCIC provided version.

.. _problem windows install:

On Windows 
^^^^^^^^^^

If you are having issues installing *CRSP Desktop*, please check the following:

1. Make sure your system meets minimal requirements listed in the :ref:`client desktop windows`.
2. In :guilabel:`Windows -> Add or Remove Programs`, check for *CRSP Desktop* (*Mountain Duck*).
   If found, uninstall any previous installations, reboot the system and retry
   installation using RCIC provided version :ref:`client desktop windows`.
3. Check for any obvious errors or warnings on your laptop.


.. _problem empty share:

Share is not visible or is empty
--------------------------------

This could be caused by one or more reasons:

1. Disconnect from share after computer came back from sleep, or hibernation mode.

   Resolution: reconnect your share.
#. Not connected via UCI VPN.

   Resolution: You must either be on the campus network or connected to the
   `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_
#. Network connectivity is poor or network is down.

   Resolution: Ensure your system is connected to UCINET or home internet. Restart system if necessary,
   to restore internet connectivity.

If the above does not solve your issue, try deleting the *share bookmark*
from *CRSP Desktop*, and recreate it anew.  Follow configuring share
instructions for your laptop type in :ref:`crsp clients` guide.

.. _problem login:

Unable to login
---------------

This could be caused by one or more reasons:

1. You don't have an account created for CRSP.

   Resolution: Please note that HPC3 and CRSP accounts are created separately.
   You may have an HPC3 account and may not have CRSP account. See :ref:`getting crsp account`

#. Not connected via UCI VPN

   Resolution: You must either be on the campus network or connected to the
   `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_

#. Your UCInetID password is incorrect.

   Resolution: Make sure your password is correct.
   Please see :ref:`password reset <reset password>`.

#. Your CRSP home directory is over quota

   Resolution: Check your :ref:`crsp quotas`.

#. There might be a technical issue with CRSP infrastructure.

   Resolution: Please submit a ticket. 

#. Authentication errors.

   When setting your CRSP desktop app you see a message similar to

   | :red:`Too many authentication errors. Please contact your web hosting`
   | :red:`service provider for assistance`

   This may happen when you used to have a password access  and have stored
   your password in the laptop credentials manager and then you switched to
   the ssh-keys based access.  It is a bug in CRSP app, the workaround is as
   follows.

   For Windows laptops:
     - Quit CRSP Desktop App.
     - | Open the :guilabel:`Windows Credentials Manager` and delete any references to CRSP.
       | It might be under *sftp* , it might be under *access.crsp*. Remove all such entries.
       | That should remove the remembered password for the CRSP desktop.
     - Start CRSP App which will ask for the passphrase for your locally-setup key.

   For macOS laptops:
     - Quit CRSP Desktop App.
     - Open :guilabel:`Applications -> Utilities -> Keychain Access` application (standard on Mac).

       - Choose a Default keychain **login**, then **Passwords**, and in the **Search** box type :bluelight:`crsp`.
       - Delete entries with **crsp** in their names that show up in the main window.
       - Do the same for Default keychain **iCloud** or any other keychain that you may have on your laptop.

       See for a reference:

       .. figure:: images/crsp/mac-keychain.png
          :align: center
          :alt: Keychain access app

          Keychain Access App

     - Quit Keychain Access app.

     - Start CRSP app, edit your lab bookmark.
       It should no longer have Password field filled or you should be able to remove what is there
       and  the password  should not appear again.
     - Try to connect to the lab share. you will be prompted for your passphrase  which is the what you used when you created your ssh keys.


.. _problem sshfs:

Unable to access via SSHFS
--------------------------------

This may be caused by network issues: slow network connection, unstable network connections
or CRSP share is unavailable.

Resolution: unmount and then remount the share.

  .. code-block:: console

     $ fusermount -u ~/your-mount-point
     $ sshfs UCInetID@crspssh.crsp.uci.edu:/mmfs1/home/UCInetID ~/your-mount-point

.. _problem file browser:

File Browser issues
-------------------

Please note that File Browser based access is for lightweight use cases.

The following are the known limitations of web based File Browser access:

* It will take longer to populate the file browser if there are lots of files in a directory.
  In our lab tests, we were able to load around 2000 files in the file browser.
* Uploading large size files with file browser can be a problem if you have slow internet connection
  or if your connection is interrupted. 
  If you have large data sets, use one of the following clients in place of File Browser:

  * :ref:`client sshfs`
  * :ref:`client desktop mac` 
  * :ref:`client desktop windows` 

* Running the File Browser in Firefox does not provide the best user experience.
  Chrome or Safari seems to work better.

* Since the File Browser works with campus shibboleth authentication, it will timeout and expire
  as soon as browser authentication expires. That means a re-authentication will be required.

* You must be registered and setup with `UCI DUO <https://www.oit.uci.edu/help/duo>`_
  in order to use File Browser.
