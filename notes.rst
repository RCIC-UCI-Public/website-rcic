
Notes
=====

Notes about specific files or settings

Editing
-------

Simply edit needed rst files and while in *website-rcic/docs/* run

.. code-block:: console

   make html

This will recreate only html files for changed rst files.
Reload needed html in the local browser for verification of changes.

Any errors resulting from running ``make html`` need to be fixed before
committing changes to git, otherwise errors will be picked by the build
process after checking out the repo on the web server.

When editing the following (top level *website-rcic/docs/source/*):

* index.rst
* conf.py
* _static/js/*js
* _static/css/*css
* roles.txt

need to run

.. code-block:: console

   make clean
   make html

The changes to the above files are used by all html files
and doing *clean* ensures building all anew.


Images
------

1. images/rcic-logo.png

   - get an account for https://uci.widencollective.com/login/sam
   - once approved login with uci credentials, get to the approved logos page
     download UCI_MB_PI_WM_White.png
   - In power point create an empty slide, add a color background
   - insert UCI image on top of it.
   - add text for RCIC, use white for letters and set background to transparent.
     scale text to the logo image.
   - remove color background, select 2 elements on a slide, right-click on them
     and choose Save as Picture and choose PNG format

   Resulting image is a combination of the original UCI logo plus text,
   with transparent background.


Enable table sorting
--------------------

Original recipe https://stackoverflow.com/questions/64443832/sorting-table-with-rst-and-python-sphinx-in-html-output
did not work.  Modifications below.

1. Download jquery.dataTables related css, js and images as:

   .. code-block:: bash

      wget https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css
      wget https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js
      wget https://cdn.datatables.net/1.10.23/css/../images/sort_asc.png
      wget https://cdn.datatables.net/1.10.23/css/../images/sort_asc_disabled.png
      wget https://cdn.datatables.net/1.10.23/css/../images/sort_both.png
      wget https://cdn.datatables.net/1.10.23/css/../images/sort_desc.png
      wget https://cdn.datatables.net/1.10.23/css/../images/sort_desc_disabled.png

   | Move jquery.dataTables.min.css in _static/css/
   | Move jquery.dataTables.min.js to _static/js/
   | Move all images to _static/images/

2. Edit jquery.dataTables.min.css and change  *float* value to *none*

   .. code-block:: text

      .dataTables_filter{float:right;text-align:right}
      to
      .dataTables_filter{float:none;text-align:right}

   Otherwise table and above table show and search entries become misaligned.

3. Create _static/js/main.js

   .. code-block:: js

   $(document).ready( function () {
       $('table.sortable').DataTable();
   } );

   Note, *sortable* is a table class. Use it when need table sorting in any
   rst files as

   .. code-block:: rst

      .. table::
         :class: sortable

4. In conf.py add

   .. code-block:: text

      # custom css file
      html_css_files = [ 'css/rcic.css','css/jquery.dataTables.min.css']

      # custom js files
      html_js_files = ['js/jquery.dataTables.min.js', 'js/main.js',]

