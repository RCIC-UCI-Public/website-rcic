.. _crsp clients:

CRSP clients
============

.. contents::
   :local:

Depending on your laptop there are a few clients that can be installed.

Please note that RCIC does not provide Windows OS or macOS support for the campus.
If there is an operating system related issue, RCIC will refer you to you get support
to address your systems issue first before installing CRSP Desktop.

.. crsp access methods:

**Supported Protocols for Accessing CRSP**

  The following underlying data transfer protocols are supported for clients accessing CRSP:

  .. table::
     :class: noscroll-table

     +-----------+--------------------------------------------------------------------------------------------------------------+
     | **SFTP**  | `The secure shell file transfer protocol <https://www.ssh.com/academy/ssh/sftp-ssh-file-transfer-protocol>`_,|
     |           | it is the *only* protocol available to desktop clients.                                                      |
     +-----------+--------------------------------------------------------------------------------------------------------------+
     | **NFSv4** | Network File System. This is only supported on :ref:`HPC3 <hpc3>` through the path :tt:`/share/crsp`.        |
     +-----------+--------------------------------------------------------------------------------------------------------------+
     | **HTTPS** | It provides very simple, browser-based access to CRSP.  This is a *fallback* access method.                  |
     +-----------+--------------------------------------------------------------------------------------------------------------+

| For issues with clients please see :ref:`crsp troubleshoot`
| Please see the :ref:`Unsupported CRSP Clients Guide <unsupported clients guide>` for some pointers on
  unsupported clients.

.. _duo crsp:

Client Authentication
---------------------

In July 2024, `Campus DUO multifactor authentication <https://www.oit.uci.edu/services/accounts-passwords/duo/>`_
became **mandatory** for all CRSP desktop clients. The push response of DUO can become very tiresome.
On some clients, DUO can make CRSP unusable because *every* file transfer requires another
DUO push.  RCIC cannot "turn off DUO".

However, **ssh keys** with **strong passwords** is a *secure* method to to provide a different
second factor of authentication. SSH keys managed properly do not require DUO after initial setup but still maintain
strong security.

.. _crsp quick start:

**Quick Start**
  #. You should follow the guide to :ref:`generate ssh keys` for different platforms.
     Remember:

     * :red:`Never copy an ssh private key file!`
     * *All ssh keys* that you generate *MUST have a strong password*.
       **Passwordless keys are a security violation**.
     * **DO NOT COPY** ssh keys from one laptop to another. Every different physical
       device should have a different *ssh key pair*.
     * We **highly recommend** that your private key file is in
       *PEM* format *and* has a :tt:`.pem` file extension.
       The CRSP desktop clients recognize :ref:`PEM-formatted keys <generate PEM-formatted keys>` more reliably.

  #. Make sure you uploaded your public keys to CRSP per :ref:`manage crsp keys`.
  #. Learn how to use `SSH Agent <https://www.ssh.com/academy/ssh/agent>`_ on your desktop/laptop. On Windows,
     you can also use `Putty's pageant <https://winscp.net/eng/docs/ui_pageant>`_.
     SSH agents securely store a private key *in memory* so that you only have to type the key's passphrase once.


.. _client desktop mac:

macOS CRSP Desktop App
----------------------

The CRSP Desktop for macOS is a licensed and branded version of the generic |mduck|_ product.
It allows you to map one or more CRSP *drives* or *file paths* to a folder on your Mac.

.. centered::  **System Requirements**

.. table::
   :align: center
   :class: noscroll-table

   +------------------------------+---------------------------------------+
   | Supported Operating System   | Minimum Hardware Requirements         |
   +==============================+=======================================+
   | Monterey / Mojave /          | Intel or ARM (Apple Silicon) Processor|
   |                              |                                       |
   | Catalina / Big Sur / Ventura | 8 GB of memory                        |
   |                              |                                       |
   |                              | 1 GB of disk space                    |
   +------------------------------+---------------------------------------+

The following sections explain how to install and use CRSP Desktop app on macOS:
  | `macOS Download Desktop App`_
  | `macOS Install Desktop App`_
  | `macOS Configure Lab Share`_
  | `macOS Connect to Lab Share`_
  | `macOS Password+DUO vs. Passphrase`_
  | `macOS Add New Shares`_

.. _macOS Download Desktop App:

:section:`macOS Download Desktop App`
  .. important:: * You must either be on the campus network or connected to the
                   `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ to download the installers.
                 * UCI pays a per-seat license for CRSP Desktop.
                   Please do not share your downloaded copy of CRSP Desktop Installer with anyone.
                 * If you have a different (previous or newer) version of the
                   CRSP Desktop (or Mountain Duck), you need to uninstall it.

  **Download Step 1:**
    Using your choice of the web browser open URL `CRSP File Browser <https://access.crsp.uci.edu/myfiles/>`_
    and login using your UCInetID and password (left image below). Once you
    see a request for a Duo push (right image below) respond to it with your phone's Duo app.

    .. table::
       :align: center
       :class: noscroll-table

       +------------------------------------------+--------------------------------------+
       | .. figure:: images/crsp/authenticate.png | .. figure:: images/crsp/duo-push.png |
       |    :align: center                        |    :align: center                    |
       |                                          |    :width: 95%                       |
       |                                          |                                      |
       |    Login using your UCI credentials      |    Request for a DUO push            |
       +------------------------------------------+--------------------------------------+

  **Download Step 2:**
    | After a successful authentication the window will look similar to the one shown below.
    | Click on the :guilabel:`CRSP-Desktop-Downloads` tab, then click on the :guilabel:`CONNECT`:

    .. figure:: images/crsp/crsp-browser-top-level.png
       :align: center
       :width: 80%
       :alt: crsp top level

       CRSP web browser top level

  **Download Step 3:**
    You should see three items on screen: a :guilabel:`.pkg` file for Mac clients, a :guilabel:`.exe` file for Windows,
    and :guilabel:`older-versions` folder.  To toggle the between list and icon view  click on the Layout
    icon :green:`outlined in green`.

    For the Mac, simply click on the file with :guilabel:`.pkg` ending:

    .. figure:: images/mac/mac-download.png
       :align: center
       :width: 80%
       :alt: select file to download

       Select file to download

    You should then see a screen with a download button on it and the full name of the file that will be downloaded
    to your local computer. Click :guilabel:`Download`:

    .. figure:: images/mac/mac-download-2.png
       :align: center
       :width: 80%
       :alt: Download

       Download

    You may see a popup window asking  if you want to allow downloads from this
    site, click on :guilabel:`Allow` button and save the file to your local computer:

    .. figure:: images/mac/mac-download-allow.png
       :align: center
       :width: 50%
       :alt: Download

       Confirm download

.. _macOS Install Desktop App:

:section:`macOS: Install Desktop App`
  **Install Step 1:**
    Find the downloaded file, depending on your Mac configuration, the file is in your
    :tt:`Downloads` folder or in your :tt:`Desktop`:

    .. figure:: images/mac/mac-desktop-app.png
       :align: center
       :width: 80%
       :alt: downloaded crsp desktop app

       Downloaded CRSP Desktop app


  **Install Step 2:**
    Double-click on the downloaded file name to launch the installation.
    You will see a confirmation window, click :guilabel:`Open`:

    .. figure:: images/mac/mac-desktop-open-confirm.png
       :align: center
       :width: 80%
       :alt: confirm opening download app

       Confirm opening of CRSP Desktop app

    Congratulations! CRSP Desktop is now installed in your system!

.. _macOS Configure Lab Share:

:section:`macOS: Configure Lab Share`
  This will configure *Map CRSP Lab Share* as a folder on your laptop.

  **Configure Step 1**
    Once the CRSP Desktop application is opened, there will be a small icon in the top toolbar:

    .. figure:: images/mac/mac-top-toolbar.png
       :align: center
       :width: 80%
       :alt: crsp desktop app in the top toolbar

       CRSP Desktop app in the top toolbar

    First time the application is started, it will automatically open a template
    window where you can configure your connection. The template bookmark is labeled :tt:`panteater`.
    You will edit this bookmark with your specific information.

  **Configure Step 2**
    The most common share to access is a lab share, owned by a UCI's PI.

    Information needed to connect to CRSP:

        a. Your UCInetID
        #. | The UCInetID of the CRSP lab owner:
           | It is our UCInetID if you own CRSP Lab
           | It is the UCInetID of your PI, If you are a graduate student/post-doctoral researcher.

    In the following  example configuration, we are going to use the
    information for user *npw* to access the *ppapadop* lab:

        a. UCInetID - npw
        #. UCInetID of the CRSP lab owner - ppapadop

    You will edit 5 fields in the default bookmark (left image below):

      1. :guilabel:`Nickname` - we recommend to change it to something like: **CRSP LAb - <pi> lab**
      #. :guilabel:`Username` - your UCInetID
      #. :guilabel:`SSH Private Key` - use an SSH key name that you generated when following the
         :ref:`Quick Start <crsp quick start>` procedure for working effectively with DUO.
         The corresponding public key should have also been :ref:`copied to CRSP <manage crsp keys>`
         into  :tt:`~/.ssh/authorized_keys` file.
      #. :guilabel:`Path` - only the last part (highlighted below) that represents **CRSP Lab Owner's UCINetID**
         should be edited. The :tt:`/mmfs1/crsp/lab` must remain unchanged.
      #. :guilabel:`Connect Mode` - change to **Online**. This keeps all files on CRSP
         and reduces local cache space. If you use CRSP from multiple clients, this the *most reliable*
         mechanism for keeping all data in sync.

         The **URL** is created automatically from the information you type in other fields,
         you don't directly change it. This URL is for  using the SFTP protocol to access
         CRSP and is an end-to-end encrypted connection.

    After editing the bookmark, your screen should look similar to the one below (right image) but with your
    specific information in place.  Click :guilabel:`Connect` to save the updated bookmark and to connect to the share.

    .. table::
       :align: center
       :class: noscroll-table

       +-------------------------------------------------+----------------------------------------------+
       | .. figure:: images/mac/mac-bookmark-default.png | .. figure:: images/mac/mac-bookmark-edit.png |
       |    :align: center                               |    :align: center                            |
       |    :width: 90%                                  |    :width: 90%                               |
       |    :alt:  edit default bookmark                 |    :alt:  edit default bookmark              |
       |                                                 |                                              |
       |    Default template bookmark                    |    Edited bookmark                           |
       +-------------------------------------------------+----------------------------------------------+

.. _macOS Connect to Lab Share:

:section:`macOS: Connect to Lab Share`

  After editing, if you click on the CRSP Desktop Notification Icon (top bar),
  you should see your bookmarks. Click on the bookmark of your choice (there
  may be one or a few), then click on :guilabel:`Connect`:

    .. figure:: images/mac/mac-connect-to-lab.png
       :align: center
       :width: 70%
       :alt: connect to lab share

       Connect to Lab Share

  At this point, your lab share is connected and you can use it just like a folder or network drive
  on your laptop:

    .. figure:: images/mac/mac-crsp-filebrowser.png
       :align: center
       :width: 80%
       :alt: lab share in file browser

       Lab Share in file browser

    The snapshots folder is *hidden*.  To view hidden files/folders in Finder window
    press :guilabel:`Command + Shift + .` (period) to make the hidden files appear
    (they will have a slightly translucent in appearance).

.. _macOS Password+DUO vs. Passphrase:

:section:`macOS: Password+DUO vs. Passphrase`

  You have two authentication options when connecting to CRSP:

  :bluelight:`Option 1: SSH Key with Passphrase`
     We highly recommend that you use ssh keys with a passphrase as described in the
     :ref:`Quick Start <crsp quick start>` guide. Assuming you did that,
     when you click :guilabel:`connect` in the `macOS Connect to Lab Share`_ section, you should see a pop-up
     window similar to the following (with your ssh key info):

     .. figure:: images/mac/mac-crsp-passphrase.png
        :align: center
        :width: 50%
        :alt: enter ssh key passphrase share

        Enter the ssh key passphrase

     Notice that a *passphrase* for the ssh private key (a local file :tt:`~/.ssh/crsp-npw`)
     is requested.  You can optionally save the passphrase in your :guilabel:`Keychain Access` app.

     Assuming that the *public* key for the private key has been properly installed on CRSP, you should be connected
     *without a DUO prompt*.

  :bluelight:`Option 2: UCInetID + password + DUO Push`
     If you do not install an ssh key, you will be prompted for your UCInetID password and a DUO push. Even if you have
     the CRSP Desktop remember your password, the DUO Push will be **required each and every time the desktop
     reconnects to CRSP**.

     :bluelight:`Step 1` Enter your password, similar to the following:

     .. figure:: images/mac/mac-crsp-username-pw.png
        :align: center
        :width: 60%
        :alt: enter user password

        Enter the password associated with YOUR UCInetID


     :bluelight:`Step 2` Respond to the DUO push

     .. figure:: images/mac/mac-crsp-duo.png
        :align: center
        :width: 50%
        :alt: Respond to DUO

        Respond to DUO

     Usually, you would enter 1 in the box, click on :guilabel:`Continue` and you will receive a DUO push on your phone.
     If your phone isn’t available, then you can enter one of your DUO backup codes that
     you set up when you enrolled in DUO through the UCI Office of Information Technology.

.. _macOS Add New Shares:

:section:`macOS: Add New Shares`
  You are not limited to just a single, mapped, space. To create a new share,
  click :guilabel:`Open Connection` to create a new template and edit it
  per the directions in `macOS Configure Lab Share`_.

  The following figure shows 3 configured shares:

  .. figure:: images/mac/mac-bookmark-add.png
     :align: center
     :width: 70%
     :alt:  multiple shares

     Multiple Shares configured

.. _client desktop windows:

Windows CRSP Desktop App
------------------------

The CRSP Desktop for Windows is a licensed and branded version of the generic |mduck|_ product.
It allows you to map one or more CRSP *drives* or *file paths* to a folder on your PC.

.. table:: **System Requirements**
   :align: center
   :class: noscroll-table

   +------------------------------+---------------------------------------+
   | Supported Operating System   | Minimum Hardware Requirements         |
   +==============================+=======================================+
   |                              | Pentium Class Processor               |
   | Windows 10 /                 |                                       |
   | Windows 11                   | 4 GB of memory (8 GB recommended)     |
   |                              |                                       |
   |                              | 1 GB of disk space                    |
   +------------------------------+---------------------------------------+

The following sections explain how to install and use CRSP Desktop app on macOS:
  | `win Download Desktop App`_
  | `win Install Desktop App`_
  | `win Configure Lab Share`_
  | `win Connect to Lab Share`_
  | `win Password+DUO vs. Passphrase`_
  | `win Add New Shares`_

.. _win Download Desktop App:

:section:`Windows: Download Desktop App`
  .. important:: * You must either be on the campus network or connected to the
                   `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_ to download the installers.
                 * UCI pays a per-seat license for CRSP Desktop.
                   Please do not share your downloaded copy of CRSP Desktop Installer with anyone.
                 * If you have a different (previous or newer) version of the
                   CRSP Desktop (or Mountain Duck), you need to uninstall it.

  **Download Step 1:**
      Using your choice of the web browser open URL `CRSP File Browser <https://access.crsp.uci.edu/myfiles/>`_
      and login using your UCInetID and password (left image below). Once you
      see a request for a Duo push (right image below) respond to it with your phone's Duo app.

      .. table::
         :align: center
         :class: noscroll-table

         +------------------------------------------+--------------------------------------+
         | .. figure:: images/crsp/authenticate.png | .. figure:: images/crsp/duo-push.png |
         |    :align: center                        |    :align: center                    |
         |                                          |    :width: 95%                       |
         |                                          |                                      |
         |    Login using your UCI credentials      |    Request for a DUO push            |
         +------------------------------------------+--------------------------------------+

  **Download Step 2:**
    | After a successful authentication the window will look similar to the one shown below.
    | Click on the :guilabel:`CRSP-Desktop-Downloads` tab, then click on the :guilabel:`CONNECT`:

    .. figure:: images/crsp/crsp-browser-top-level.png
       :align: center
       :width: 80%
       :alt: crsp top level

       CRSP web browser top level

  **Download Step 3:**
    You should see three items on screen: a :guilabel:`.pkg` file for Mac clients, a :guilabel:`.exe` file for Windows,
    and :guilabel:`older-versions` folder.  To toggle the between list and icon view click on the Layout
    icon :green:`outlined in green`.

    For the Windows, simply click on the file with :guilabel:`.exe` ending.

    .. figure:: images/win/win-download-crsp-desktop.png
       :align: center
       :width: 80%
       :alt: select file to download

       Select file to download

    You should then see a screen with a download button on it and the full name of the file that will be downloaded
    to your local computer. Click :guilabel:`Download` and save the file to your local computer:

    .. figure:: images/win/win-download-crsp-desktop-2.png
       :align: center
       :width: 80%
       :alt: Download

       Download

.. _win Install Desktop App:

:section:`Windows: Install Desktop App`

  **Install Step 1**
    By default, the file is downloaded in your :guilabel:`Downloads` folder. Find the downloaded file,
    double-click on it to launch the installation of the licensed version of CRSP Desktop.

  **Install Step 2**
    In the opened window click :guilabel:`Install` to Install the CRSP Desktop on your laptop.

    .. figure:: images/win/win-install-crsp-desktop.png
       :align: center
       :width: 60%
       :alt: install downloaded app

       Install the CRSP Desktop.

  **Install Step 3**
    After a successful installation, follow the instructions and
    click :guilabel:`Restart` to restart your computer:

    .. figure:: images/win/win-restart-computer.png
       :align: center
       :width: 60%
       :alt: restart computer

       Restart your computer

    Congratulations!  CRSP Desktop is now installed in your system!

.. _win Configure Lab Share:

:section:`Windows: Configure Lab Share`
  This will *Map CRSP Lab Share* as a folder on your laptop.

  .. attention:: If Accessing :ref:`crsp annex`, then this step requires modification and is similar to
                 `win Add New Shares`_

  **Configure Step 1**
    CRSP Desktop shows in the Windows
    `Notification Area <https://support.microsoft.com/en-us/windows/customize-the-taskbar-notification-area-e159e8d2-9ac5-b2bd-61c5-bb63c1d437c3>`_
    (also known as *system  tray*). You can left-click or right-click on the :guilabel:`CRSP Desktop` icon to open it (left image).
    Once opened in a set of *bookmarks*  choose a template bookmark labeled :guilabel:`panteater` (right image):

    .. table::
       :align: center
       :class: noscroll-table

       +----------------------------------------------------+----------------------------------------------+
       | .. figure:: images/win/win-access-crsp-desktop.png | .. figure:: images/win/win-edit-bookmark.png |
       |    :width: 100%                                    |    :width: 80%                               |
       |    :alt: start desktop app                         |    :alt: choose template bookmark            |
       |                                                    |                                              |
       |    Start CRSP Desktop App                          |    Choose the template bookmark              |
       +----------------------------------------------------+----------------------------------------------+

  **Configure Step 2**
    The most common share to access is a lab share, owned by a UCI's PI.

    Information needed to connect to CRSP:

        a. Your UCInetID
        #. | The UCInetID of the CRSP lab owner:
           | It is our UCInetID if you own CRSP Lab
           | It is the UCInetID of your PI, If you are a graduate student/post-doctoral researcher.

    In the following  example configuration, we are going to use the
    information for user *nppapadop* to access the *npw* lab:

        a. UCInetID - ppapadop
        #. UCInetID of the CRSP lab owner - npw

    You will edit 5 fields in the default bookmark (left image below):

      1. :guilabel:`Nickname` - we recommend to change it to something like: **CRSP LAb - <pi> lab**
      #. :guilabel:`Username` - your UCInetID
      #. :guilabel:`SSH Private Key` - use an SSH key name that you generated when following the
         :ref:`Quick Start <crsp quick start>` procedure for working effectively with DUO.
         The corresponding public key should have also been :ref:`copied to CRSP <manage crsp keys>`
         into  :tt:`~/.ssh/authorized_keys` file.
      #. :guilabel:`Path` - only the last part (highlighted below) that represents **CRSP Lab Owner's UCINetID**
         should be edited. The :tt:`/mmfs1/crsp/lab` must remain unchanged.
      #. :guilabel:`Connect Mode` - change to **Online**. This keeps all files on CRSP
         and reduces local cache space. If you use CRSP from multiple clients, this the *most reliable*
         mechanism for keeping all data in sync.

         The **URL** is created automatically from the information you type in other fields,

    After editing the bookmark, your screen should look similar to the one below (right image) but with your
    specific information in place.  Click :guilabel:`OK` to save the updated bookmark.

    .. table::
       :align: center
       :class: noscroll-table

       +--------------------------------------------------+------------------------------------------------+
       | .. figure:: images/win/win-panteater-default.png | .. figure:: images/win/win-edited-bookmark.png |
       |    :width: 100%                                  |    :width: 100%                                |
       |    :alt: default template bookmark               |    :alt: edited bookmark                       |
       |                                                  |                                                |
       |    Default template bookmark                     |    Edited bookmark                             |
       +--------------------------------------------------+------------------------------------------------+

.. _win Connect to Lab Share:

:section:`Windows: Connect to Lab Share`
  After editing, if you click on the :guilabel:`CRSP Desktop` notification icon,
  you should see your edited bookmark.  For our example, it looks like the following:

  .. figure:: images/win/win-connect-to-lab.png
     :align: center
     :width: 60%
     :alt: connect to lab share

     Connect to Lab Share

  Click :guilabel:`connect` to open your share.

  If you are not running ssh-agent or CRSP desktop has not remembered your password, you should be asked for the
  *passphrase* to your ssh private key file that you specified.

  At this point, your lab share is connected and you can use it just like a folder or network drive.

.. _win Password+DUO vs. Passphrase:

:section:`Windows: Password + DUO vs. Passphrase`

  You have two authentication options when connecting to CRSP:

  :bluelight:`Option 1: SSH Key with Passphrase`
    We highly recommend that you use ssh keys with a passphrase as described in the
    :ref:`Quick Start <crsp quick start>` guide.
    When you click :guilabel:`Connect` in the previous step `win Connect to Lab Share`_, you should see a pop-up
    window similar to the following:

    .. figure:: images/win/crsp-passphrase.png
       :align: center
       :width: 60%
       :alt: enter ssh key passphrase share

       Enter the ssh key passphrase

    Notice that a *passphrase* is requested for a local file (ssh private key).
    You can optionally save the passphrase.  Assuming that the *public* key for
    the private key has been properly installed on CRSP, you should be connected
    *without a DUO prompt*.

  :bluelight:`Option 2: UCInetID + password + DUO Push`
    If you do NOT install an ssh key, you will be prompted for your UCInetID password and a DUO push. Even if you have
    the CRSP Desktop remember your password, the DUO Push will be **required each and every time** the desktop
    reconnects to CRSP.

    :bluelight:`Step 1` Enter your password, similar to the following:

      .. figure:: images/win/crsp-username-pw.png
         :align: center
         :width: 60%
         :alt: enter user password

         Enter the password associated with YOUR UCInetID

    :bluelight:`Step 2` Respond to the DUO push

      Usually, you would enter :tt:`1` in the box, and you will receive a DUO push on your phone. If your phone isn't
      available, then you can enter one of your DUO backup codes that you set up when you `enrolled in
      DUO <https://www.oit.uci.edu/services/accounts-passwords/duo/>`_ through the UCI Office of Information Technology

      .. figure:: images/win/crsp-duo.png
         :align: center
         :width: 60%
         :alt: Respond to DUO

         Respond to DUO

.. _win Add New Shares:

:section:`Windows: Add New Shares`
  You are not limited to just a single, mapped, space. To create a new share,
  click :guilabel:`Open Connection` to create a new template and edit it
  following the directions above in `win Configure Lab Share`_.

  Here is an example with multiple connections configured and active:

  .. figure:: images/win/win-multiple-connections.png
     :align: center
     :width: 50%
     :alt: multiple lab shares

     Multiple Lab Shares

.. _client web browser:

Web based File Browser
----------------------

A simple, easy to use *File Browser* is platform independent and is compatible
with most web browsers.

.. important:: * **File Browser is suitable only for lightweight use**.
               * Use :ref:`client desktop mac` and :ref:`client desktop windows` for moderate/heavy use.
               * Your system must be updated with the latest version of Google Chrome, or Firefox or Safari
               * You must be registered and setup with `UCI DUO <https://www.oit.uci.edu/services/accounts-passwords/duo/>`_

The following sections explain how to install and use CRSP Desktop app on macOS:
  | `Web Browser Login`_
  | `Web Browser Connect to Shares`_
  | `Web Browser Navigation`_

.. _Web Browser Login:

:section:`Web Browser Login`
    Using your choice of the web browser open URL `CRSP File Browser <https://access.crsp.uci.edu/myfiles/>`_
    and login using your UCInetID and password (left image below). Once you
    see a request for a Duo push (right image below) respond to it with your phone's Duo app.

    .. table::
       :align: center
       :class: noscroll-table

       +------------------------------------------+--------------------------------------+
       | .. figure:: images/crsp/authenticate.png | .. figure:: images/crsp/duo-push.png |
       |    :align: center                        |    :align: center                    |
       |                                          |    :width: 95%                       |
       |                                          |                                      |
       |    Login using your UCI credentials      |    Request for a DUO push            |
       +------------------------------------------+--------------------------------------+

.. _Web Browser Connect to Shares:

:section:`Web Browser Connect to Shares`
  Once logged in, you will be presented with the CRSP top level screen. You can
  follow the tab :guilabel:`My-labs`  to your Lab shared areas or the tab :guilabel:`My-Home`
  to your HOME private area.

  .. figure:: images/web/browser-lab-connect.png
     :align: center
     :width: 70%
     :alt: web browser top level

     Top level File Browser

  .. important::
     * Nothing can be stored in HOME area, it is used for for files associated with the account
       and for storing quota info file.  It is a completely private area, only you have access.
     * All work on CRSP must be done in your lab area.
       Lab areas are flexible for sharing. You can be granted access to multiple Lab areas.

  To see your labs, Click on :guilabel:`My-Labs`, then click on :guilabel:`CONNECT`.
  You will see a screen similar to the image below. In this example a user *npw*
  has an access to 4 labs:

  .. figure:: images/web/browser-user-labs.png
     :align: center
     :width: 80%
     :alt: web browser labs

     File browser labs for user *npw*

.. _Web Browser Navigation:

:section:`Web Browser Navigation`
  The File Browser is fairly easy to navigate, with some very basic sets of functions.

  #. **Create folders (directories)**

     Click on desired folders to navigate to a location where you want to create a
     new folder. Click on :guilabel:`NEW FOLDER` and on a newly opened line type
     desired folder name:

     .. figure:: images/web/browser-create-folder.png
        :align: center
        :width: 80%
        :alt:  Create a new folder

        Create a new folder

  #. **Create files**

     Click on desired folders to navigate to a location where you want to create a
     file then click on :guilabel:`NEW FILE`  and on a newly opened line type
     desired file name:

     .. figure:: images/web/browser-create-file.png
        :align: center
        :width: 80%
        :alt:  Create a new file

        Create a new file

  #. **Download files**

     Select a file or multiple files to download, click on :guilabel:`Download`:

     .. figure:: images/web/browser-file-download.png
        :align: center
        :width: 80%
        :alt: File download

        File download

     * a single file will be downloaded as a file with the same name
     * multiple files will be downloaded as :tt:`download.zip`  file
       which will need to be unzipped to access the contents.

  #. **Upload files**

     Navigate to a folder where you want to upload files to and click on
     the upload button at the bottom-right of the screen:

     .. figure:: images/web/browser-upload-file.png
        :align: center
        :width: 80%
        :alt: File upload

        File upload

     Then follow your local laptop file finder application that will let you
     choose file or multiple files for upload.
     Once uploaded the CRSP browser will show a confirmation similar to
     the one below showing your uploaded file name:

     .. figure:: images/web/browser-upload-file-confirm.png
        :align: center
        :width: 80%
        :alt: File upload

        File upload confirmation

  #. **Delete files or directories**

     Navigate to a folder or directory you want to remove and click on
     the icon before its name to choose it, then click on :guilabel:`REMOVE`:

     .. figure:: images/web/browser-rm-file.png
        :align: center
        :width: 80%
        :alt: delete file or folder

        Delete file or folder

     You will see a popup window asking to type item name,
     in this example it is :tt:`test-file`:

     .. figure:: images/web/browser-rm-file-confirm.png
        :align: center
        :width: 60%
        :alt: confirm delete

        Confirm deletion via typing file or folder name

  #. **Logout from CRSP FIle Browser**

     To logout from the CRSP browser click on the power icon
     in the top right corner:

      .. figure:: images/web/browser-logout.png
         :align: center
         :width: 80%
         :alt: CRSP File Browser logout

         CRSP File Browser logout

      You should see a confirmation:

      .. figure:: images/web/browser-logout-confirm.png
         :align: center
         :width: 80%
         :alt: CRSP File Browser logout confirmation

         CRSP File Browser logout  confirmation

.. _client sshfs:

Linux SSHFS
-----------

The following sections explain how to install and use SSHFS on Linux laptop for accessing CRSP:

  | :ref:`Install SSHFS <install sshfs>`
  | :ref:`Mount CRSP shares <mount sshfs>`
  | :ref:`Unmount CRSP shares <unmount sshfs>`
  | :ref:`Using SSHFS <using sshfs>`

.. _install sshfs:

:section:`Install SSHFS`
  On your laptop you will need super user (sudo) rights to install SSHFS.

  For CentOS based laptop

    .. code-block:: console

       $ yum -y install sshfs

  For Ubuntu/Debian based systems

    .. code-block:: console

       $ apt-get -y install sshfs

.. _mount sshfs:

:section:`Mount CRSP shares`
  SSHFS will *Map CRSP Lab Share* as a folder on your laptop.

  .. important:: You must either be on the campus network or connected to the
                 `UCI campus VPN <https://www.oit.uci.edu/help/vpn>`_.

  Information needed to connect to CRSP:

      a. Your UCInetID
      #. | The UCInetID of the CRSP lab owner:
         | It is our UCInetID if you own CRSP Lab
         | It is the UCInetID of your PI, If you are a graduate student/post-doctoral researcher.

  From your desktop or laptop, execute the following command
  replacing :tt:`username`  and :tt:`labname` with the appropriate UCInetID(s):

  .. code-block:: console

     $ cd ~
     $ mkdir crsp_mount
     $ sshfs -o ssh_command='ssh -A -X -o StrictHostKeyChecking=no' \
             -o idmap=user username@access.crsp.uci.edu:/mmfs1/crsp/lab/labname \
             ~/crsp_mount

  As a result, ``sshfs`` mounts CRSP Lab share under :tt:`~/crsp_mount`
  directory. Use any name of your choice in place of :tt:`crsp_mount`.

  **Sshfs will not automatically map all your remote UID and GID** from all of your CRSP groups
  into your local Linux system, it  will only present your primary UID/GID.
  Note in the command above the use of :tt:`-o idmap=user` option.

  As the campus does not have a centralized directory service to manage every system, options
  to keep your local system and CRSP accounts synced are very limited.

.. _unmount sshfs:

:section:`Unmount CRSP shares`
  To unmount the share that was mounted in the above example:

  .. code-block:: console

     $ fusermount -u ~/crsp_mount

.. _using sshfs:

:section:`Using SSHFS`
  Copy a file from your local system to your SSHFS mounted drive

  .. code-block:: console

     $ cp ~/dir1/file.tar.gz ~/crsp_mount/share/

  Recursively copy a directory from local system to mounted CRSP share using ``rsync``

  .. code-block:: console

     $ rsync -rltv ~/dir1 ~/crsp_mount/share/


.. _client from hpc3:

Access from HPC3
-----------------

On HPC3, CRSP shares are mounted in */share/crsp*:

.. code-block:: console

   [user@login-x:~]$ ls /share/crsp
   home  lab

:home:
  HOME area for all users accounts. All HOME snapshots are in :tt:`/share/crsp/home/.snapshots`
  with read only access. Users can only access their own HOME area.
:lab:
  Lab area for all users accounts. Each LAB directory has snapshots in :tt:`.snapshots/`
  for read-only access by LAB members.

.. _hpc3 crsp home:

:section:`CRSP HOME`
  User CRSP HOME area is :tt:`/share/crsp/home/UCInetID`:

  * it is a placeholder for login related files.
  * it is different from your HPC3 account's :tt:`$HOME`
  * :red:`Do not store anything in your CRSP HOME`
  * file :tt:`quotas.txt` is placed automatically in your CRSP HOME area
    and provides information about quotas. Please see :ref:`crsp quotas` for details.

.. _hpc3 crsp lab:

:section:`CRSP LAB`

  LAB area is your primary storage area. It is :tt:`/share/crsp/lab/UCInetID`
  or any other LAB directories you have access for.

  *If you are a PI and it's your lab*

  .. table::
     :class: noscroll-table

     +----------+----------+----------------------------------+-----------------------------------------+
     | USERNAME | LABNAME  | Mounted location                 | Read/write access                       |
     +==========+==========+==================================+=========================================+
     | your     | your     | /share/crsp/lab/LABNAME          | you can create any directories and files|
     |          |          +----------------------------------+-----------------------------------------+
     | UCInetID | UCInetID | /share/crsp/lab/LABNAME/USERNAME | your personal space                     |
     +----------+----------+----------------------------------+-----------------------------------------+

  *If you are added to a PI lab* e.g., you are a student/postdoc in the lab

  .. table::
     :class: noscroll-table

     +----------+----------+----------------------------------+-----------------------------------------+
     | USERNAME | LABNAME  | Mounted location                 | Read/write access                       |
     +==========+==========+==================================+=========================================+
     | your     | your PI  | /share/crsp/lab/LABNAME/USERNAME | you and PI                              |
     |          |          +----------------------------------+-----------------------------------------+
     | UCInetID | UCInetID | /share/crsp/lab/LABNAME/share    | all lab members                         |
     +----------+----------+----------------------------------+-----------------------------------------+

  The following example shows the directory structure and permissions
  for a PI panteater who has a lab and added 2 students:

  .. code-block:: console

     [user@login-x:~]$ ls -ld /share/crsp/lab/panteater
     drwxr-x--T 3 panteater panteater_lab_share  512 Mar  6 15:58 /share/crsp/lab/panteater

     [user@login-x:~]$ ls -l /share/crsp/lab/panteater
     drwx--S--- 2 panteater panteater_lab      2048 Jul 12 10:22 panteater # PI access
     drwxrws--- 2 student1  panteater_lab       512 Apr 29 10:27 student1  # student1/PI access
     drwxrws--- 2 student2  panteater_lab       512 Apr 29 10:27 student2  # student2/PI access
     drwxrws--T 4 panteater panteater_lab_share 512 Nov  2  2020 share     # all in lab acces


.. _hpc3 crsp data:

:section:`Moving data to CRSP`
  Please see :ref:`data transfer` for in-depth  commands examples.

  Recursively copy your :tt:`mydir/` directory from DFS6 storage to your LAB share on CRSP:

  .. code-block:: console

     [user@login-x:~]$ rsync -rv /dfs6/pub/paneater/mydir /share/crsp/lab/panteater/

.. |mduck| replace:: Mountain Duck link:https://mountainduck.io/[Mountain Duck] product.
.. _`mduck`: https://mountainduck.io
