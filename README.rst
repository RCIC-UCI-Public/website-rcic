
RCIC website
============

This repo provides documentation created with Read The Docs.


Building HTML locally for testing
---------------------------------

1. Install prerequisites

   .. code-block:: console

      pip3 install sphinx
      pip3 install sphinx_rtd_theme

2. Check out repo and build

   .. code-block:: console

      git clone git@github.com:RCIC-UCI-Public/website-rcic.git
      cd website-rcic
      make default
      make deploy

   See ``make help`` for more options

3. Point your local browser to `build/html/index.html`.

Editing
-------

See *notes.rst*


Install on webserver host
-------------------------

Older python 3.6 8 while installed sphinx does not have a newer 
theme and results in a bit outdated look. 

**Remedy**

Copy CentOS 7.9 RPMS fro xcat and install as 

.. code-block:: console

   yum install rocks-devel-7.1-13.x86_64.rpm
   yum install rcic-module-support-1.2-1.x86_64.rpm
   yum install rcic-module-path-1.0-5.x86_64.rpm
   yum install python_3.8.0-3.8.0-5.x86_64.rpm
   yum install python_3.8.0-module
   yum install python_3.8.0-module-3.8.0-5.x86_64.rpm
   yum install python_3.8.0-pip-20.0.2-4.x86_64.rpm 
   yum install python_3.8.0-setuptools-46.0.0-4.x86_64.rpm
   yum install python_3.8.0-urllib3-1.25.8-4.x86_64.rpm
   
   pip install sphinx==6.2.0
   pip install sphinx_rtd_theme

Update cron script to reference new python when building



