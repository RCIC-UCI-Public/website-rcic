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

**This could be caused by one or more reasons:**

1. Disconnect from share after computer came back from sleep, or hibernation mode

   Resolution: reconnect your share. 

2. Not connected via UCI VPN
   
   Resolution: You must either be on the campus network or connected to the
   `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ 
3. Network connectivity is poor or network is down

   Resolution: Ensure your system is connected to UCINET or home internet. Restart system if necessary,
   to restore internet connectivity.  

If the above does not solve your issue, try deleting the *share bookmark*
from *CRSP Desktop*, and recreate it anew.  Follow configuring share
instructions for your laptop type in :ref:`crsp clients` guide.

.. _problem login:

Unable to login
---------------

**This could be caused by one or more reasons:**

1. You don't have an account created for CRSP.

   Resolution: Please note that HPC3 and CRSP accounts are separate,
   You may have an HPC3 account and may not have CRSP account.  See :ref:`getting crsp account`

2. Your UCINetID password is incorrect

   Resolution: Make sure your password is correct. Note, we do not manage passwords. 

3. Your CRSP home directory is over quota

   Resolution: Check your :ref:`crsp quotas`.

4. Not connected via UCI VPN
   
   Resolution: You must either be on the campus network or connected to the
   `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ 

5. There might be a technical issue with CRSP infrastructure.

   Resolution: Please submit a ticket. 

.. _problem sshfs:

Unable to access via SSHFS
--------------------------------

This may be caused by network issues: slow network connection, unstable network connections
or CRSP share is unavailable.

Resolution: unmount and then remount the share.

  .. code-block:: console

     $ fusermount -u ~/your-mount-point
     $ sshfs ucinetid@crspssh.crsp.uci.edu:/mmfs1/home/ucinetid ~/your-mount-point

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
