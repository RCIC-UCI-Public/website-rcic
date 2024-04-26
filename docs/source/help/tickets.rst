
.. _tickets:

Support tickets
===============

The resources at RCIC are here to help the UCI research community.
There are literally 1000's of accounts on our resources, representing
disciplines from every corner of UCI. 

We handle a lot of help requests and the time to understand your problem is at a premium.
The better you construct our request the faster we can get to solving it.
Requests don’t need to be elaborate, but using good descriptions
and relevant information :underline:`really` helps us hone in on the root cause.

A pretty good perspective on `How to report bugs effectively
<http://www.chiark.greenend.org.uk/~sgtatham/bugs.html>`_
illustrates some of the reasons for the detail. High-end computing is a team sport!

**Please follow the guidelines below when submitting help requests.**

.. contents::
   :local:


.. _submit ticket:

:bluelight:`How to submit`
--------------------------

Send email to hpc-support@uci.edu describing your problem.
Sending email will automatically generate a ticket in our tracking system.

After you submit a ticket there is an automated email response that it was
registered in our system. This will be followed by a `real` response from one of our team
members who is handling the ticket.

| We try to respond by the next business day, but we do not work 24x7.
| Only emergency tickets are answered on weekends or during the holidays.

.. note::

   | How you submit your ticket and what information you include can
     greatly speed up resolution and save time for you and for us.
     **If we cannot reproduce your problem, we cannot fix it!**
   | Please follow good ticket practices and what to
     include for specific issues outlined below.

.. _good ticket:

:bluelight:`Good ticket practices`
-----------------------------------

:underline:`Before submitting a ticket`
  Help yourself first. Try your best to see if the problem is a simple one.

  1. **Assume you did something wrong**. Verify your commands and scripts and try to reproduce the error.
     Sometimes simple typos or wrong parameters are a cause of a problem.
  2. **Examine the contents of output/error files** (if your programs have any) before you call for help.
     Often these files have additional information and even potential solutions.
  3. **Read our :ref:`faq`**. Your question may have already been answered.
  4. **Read our user guides**. They explain a few guidelines that are specific for our systems.
     When users follow our guidelines many of the problems are easily avoided, such as:

     * file permissions
     * quota problems
     * Slurm jobs submission errors and OOM killed errors

  5. **Do a Google search** with your error message. Others may have had the same
     problem  and found a successful solution. Note, you need to understand
     what in your error is general (applicable to other similar
     installations) and what is specific to the resources we provide.

:underline:`When submitting a ticket`

:DO:
  * Please try to submit using your @uci.edu email address.
  * Have a descriptive subject line.
  * :red:`For any problem always provide your UCINetID`.
    Remember, not everyone uses `UCINetID@uci.edu`
  * Be specific and provide only relevant essential factual information
    about a problem (see following sections for details).
  * Be reasonable and polite. We know when something goes wrong, it's very stressful. It's stressful for us, too.

:DO NOT:
  * :red:`Do not be vague`. Statements like *it's slow*, *I cant login*, or *my code doesn't work* give us nothing concrete.
  * :red:`Do not send screenshots` unless you are working with a GUI application.
    From screenshots, we can't cut and paste commands or other info, which
    slows down our resolution of your problem. Simple text-based cut and paste
    directly into your email is the best info we can use.
  * :red:`Do not attach multiple files` to your ticket. This can overload mail attachment limit
    in ticketing system. It is much easier to see all files if you simply provide full path to them
    in your storage area.
  * :red:`Do not send multiple ticket requests` for the same problem. Simply reply to
    our response to you, this will keep all email conversation on the same ticket.

:underline:`After receiving a response from us`
  1. Sometimes our response is "no, this cant be done" or similar.
     This is a specific resolution of a specific ticket.
     There is always a :underline:`reasonable cause` for this and we explain it in our response.
  2. When we ask for additional information in our response provide exactly what we ask.
  3. Once your problem is resolved, acknowledge this so we can close the ticket.

.. _login tickets:

:bluelight:`Login problems`
---------------------------

When reporting login problems please include the following:

* Where from are you trying to log in, from campus or over the VPN ?
* What kind of computer and Operating System are you connecting from (Windows, macOS, Linux) ?
* What software and what version are you using to connect ?
* Copy and paste into your email what **exact commands** you typed and what **exact errors** you saw.
  Usually there are just a few lines.

.. _cluster tickets:

:bluelight:`Cluster Problems`
-----------------------------

When reporting errors related to Slurm, allocation quotas,
software errors, please include the following:

* Slurm job ID.
* Node  where you see the issue (for interactive jobs it is output of ``hostname`` command).
* Your working directory  (output of ``pwd`` command).
* Full path to the files that you reference (Slurm submit script,
  output/input/error files, your own scripts, etc).
  :red:`Do not attach multiple files to your ticket`. Providing a path
  gives us much better access to the files.
* If you loaded software modules, what were they (output of ``module list`` command)?
* Copy and paste **exact command** you used, :red:`do not send us a screenshotd` of the commands unless
  you're using a graphics program and the problem can not be described without a screenshot.
* Break very long commands into readable length with the use of the
  back slash continuation character :tt:`\\`.

  For example, this long line is difficult to read:

  .. code-block:: bash

                  make_2d_plots.py -i wetdry_cr/beta_diveuclidean/beta_div_euclideancoords.txt -m wetdry_cr/mapping_files/merged_mapping_data.txt -b 'Elevation' -o wetdry_cr/2dplots/elevation

  Same line with added :tt:`\\` is much easier to read and to understand:

  .. code-block:: bash

                  make_2d_plots.py \
                    -i wetdry_cr/beta_diveuclidean/beta_div_euclideancoords.txt \
                    -m wetdry_cr/mapping_files/merged_mapping_data.txt \
                    -b 'Elevation' \
                    -o wetdry_cr/2dplots/elevation

* Copy and paste **exact output** and **exact error** that the command caused.
  If the error and output are more than a few lines long, save in separate files and provide 
  full paths to them.

.. _storage tickets:

:bluelight:`Storage Problems`
------------------------------------

When reporting problems related to DFS or CRSP storage
please include the following:

* DFS or CRSP path and group ID you are trying to access. Many groups have
  multiple paths, we cant guess from your name which one you need.
* How do you access: on HPC3, via web browser, Desktop, etc.
* Copy and paste into your email what **exact commands** you typed and what **exact errors** you saw.
* If you are asking to be added to PI's DFS or CRSP group:

  * your PI UCInetID
  * cc your request to your PI so the PI can confirm the access
    on the same ticket. **We cant grant any access without PI's confirmation.**

.. _software tickets:

:bluelight:`Requesting New software`
------------------------------------

Because this is a research environment, we are often asked to add new software.

RCIC builds and maintains an extensive collection of domain-specific software.  Some software is
very straightforward to build and deploy to the cluster, other software can be extremely challenging
and time consuming.  We do our best to balance stability with the availability
of "latest and greatest".

Given realities of time, we have to prioritize software that affects more than a single
researcher or group.

:red:`We certainly are not here to install software that`
  * You might use.
  * You just want to play with or evaluate.
  * Is the latest available version. Just because it is the latest is not a good reason.
  * Is too old. Anything that is 5  or more years old  is not a good candidate.
  * Is no longer supported by developers (Python 2 is an example).

Even with those constraints, we are not shy about taking on complicated,
time-consuming installs with many dependencies.  Part of our value add to UCI is to handle as much of this as
possible.  We strive to say "yes" to software requests, but sometimes do have to say "no."

:underline:`Before asking us to install`:

  * Check if the software is already installed on the cluster.
    See :ref:`list modules <list modules>` for details.
  * Install it yourself. We encourage users first to build/install the applications
    in their user area.

    The most common request is for conda-based  install or for some specific Python, R, or Perl package.
    These very often can be installed on a per-user basis. Please see the following guides  that
    explain how to install software in user area:

    ====================== =========================== ================ 
    :ref:`install conda`   :ref:`install python`       :ref:`install r`
    :ref:`install perl`    :ref:`install singularity`  :ref:`compile`
    :ref:`install jupyter`
    ====================== =========================== ================

    .. attention:: When you attempt to install yourself, please note HPC3 is
                   CentOS-based system. If you run across instructions that say :tt:`Ubuntu`
                   or :tt:`apt get` or similar, those are for a different Linux-based OS
                   and won't work on HPC3.

    .. attention:: | :red:`For security reasons the following is not allowed:`
                   |   - :red:`sudo  or su access`
                   |   - :red:`Docker`
                   | However, many docker containers can be reused as singularity containers.
                   | Please see :ref:`install singularity`


:underline:`Submit a Software Ticket`

  You might not be able to install/compile the software yourself without some additional
  system-installed software and that's a good reason to ask us.
  In the end, it's a partnership to get new software added to HPC3. We need good
  information from you and a willingness to validate the installed software.

  If you want to request new software or updated versions of software that are
  already installed please submit a ticket with the following information:

  * Software name and version.
  * A brief statement about which lab(s)/domain(s) the software will impact
    and why this specific version is needed.
    Don't write *many labs will use it*, we need factual usefulness info.
  * How have you tried to install it yourself, and what were **exact commands** and **exact errors**.
  * URL for download/install instructions.
  * If applicable, any special configuration options/capabilities that should be enabled (or disabled).
  * A brief statement about a "test" input and expected output so that we can do an initial validation.

