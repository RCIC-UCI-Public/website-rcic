
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
