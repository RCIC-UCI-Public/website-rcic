.. _acceptable use:
.. _conduct rules:

Acceptable use
==============

Cluster is a shared resource where at any given time there can be hundreds users
and thousands of jobs running. What you do can have dramatic effects on others.

Access to all RCIC managed resources is subject to our
`Acceptable Use Policy </_static/RCIC-Acceptable-Use-Policy.pdf>`_ (PDF).

.. important::

   Violations of this policy or any other applicable University policies may result
   in the temporary or permanent removal of accounts associated with research computing.
   To avoid problems, please read the policy and follow simple rules of conduct described below. 

.. centered:: Conduct Rules 

.. table:: 
   :class: noscroll-table

   +----------------+---------------------------------------------------------------------------------------------+
   | Node/Task      | Action                                                                                      |
   +================+=============================================================================================+
   | **Login**      | Allowed are light-weight processes such as:                                                 |
   | **nodes**      |    * Light editing                                                                          |
   |                |    * Very short compilation that are under a few minutes and use  1 CPU                     |
   |                |    * Submitting all interactive and batch jobs to Slurm Scheduler                           |
   |                |                                                                                             |
   |                | :darkred:`Not allowed:`                                                                     |
   |                |    * :darkred:`Any setup of jupyter or other servers on local ports`                        |
   |                |    * :darkred:`Any computational jobs`                                                      |
   |                |    * :darkred:`Any job that runs for more than 1hr or uses significant memory and CPU`      |
   |                |    * :darkred:`Any make/cmake compilation with multiple threads, for example` ``make -j 8`` |
   |                |    * :darkred:`Any R or conda/mamba installation of packages or environments`               |
   |                |    * :darkred:`Any downloads of packages, data, large files that exceed a few Gbs`          |
   |                |                                                                                             |
   |                |    The above and additional similar processes need to be submitted to the                   |
   |                |    Slurm scheduler as :ref:`interactive or batch jobs <jobs>`.                              |
   |                |                                                                                             |
   |                |    :darkred:`Long-running jobs will be removed from login nodes without notice.`            |
   +----------------+---------------------------------------------------------------------------------------------+
   | **Compute**    |  There is NO SSH access to the compute nodes to prevent users from starting                 |
   | **nodes**      |  jobs bypassing Slurm.  Use :ref:`attach to job`.                                           |
   +----------------+---------------------------------------------------------------------------------------------+
   | **Slurm jobs** | Do:                                                                                         |
   |                |   * All batch or interactive jobs must be submitted to Slurm                                |
   |                |   * Make sure to use your actual UCI-issued email address.                                  |
   |                |                                                                                             |
   |                | :darkred:`Do not:`                                                                          |
   |                |   * :darkred:`run Slurm jobs in your $HOME`.                                                |
   |                |     Instead, use your DFS storage :tt:`/pub/UCInetID`                                       |
   |                |   * :darkred:`use mail event type ALL,BEGIN`. The END is sufficient for all jobs.           |
   |                |   * :darkred:`enable email notification if you submit hundreds of jobs.                     |
   |                |     Sending an email for each job overloads Postfix server.`                                |
   +----------------+---------------------------------------------------------------------------------------------+
   | **Disk**       |  Check your disk quota frequently. See :ref:`home`, :ref:`dfs` and :ref:`crsp`              |
   | **quotas**     |  pages for information about quotas. File system limits are generally the first             |
   |                |  ones that will negatively affect your job.                                                 |
   +----------------+---------------------------------------------------------------------------------------------+

