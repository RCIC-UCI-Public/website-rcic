
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

PDF files
---------

1. **RCIC-description.pdf** generated  from docx file in RCIC-Internal/ on google drive.  
#. **RCIC-Acceptable-Use-Policy.pdf** generated from docx file in RCIC-Internal/ on google drive.
#. **software-latest.pdf** generated in admixbuilder repo (github.com:RCIC-UCI-Public/admixbuilder.git)
   via *dotpdf* target in Makefile.

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

Inline icons
------------

These inline icons are from the rst file for TOC in RTD documentation, see https://docs.readthedocs.io/en/stable/index.html

- ⏩️  use this in reference guide
- 🚀 Tutorials
- 💡 Explanation
- 🪄 How-to guides
- 📚 Reference
- 💓 Open source and user focused
- 🔄 Up to date documentation

|:card_index_dividers:| Documentation for every version


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

2. Edit jquery.dataTables.min.css and change  *float:right* value to *float:none*

   .. code-block:: text

      .dataTables_filter{float:right;text-align:right}
      to
      .dataTables_filter{float:none;text-align:right}

   Otherwise the table and the elements "Show" and "Search" above it become misaligned,
   and the table itself is reduced to 50% of the page width.

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

Accessibility
-------------

Changes were done via overwriting Sphinx read-the-docs original theme. The changes are via:

* files in **_templates/** overwrite original theme layouts in specific sections

  * **breadcrumbs.html** - overwrite original where each page has a home icon,
    link to the rst source and a repetitive title of the page. 
    **IMPORTANT: keep this file empty**, it is intended for the original header removal.
  * **footer.html** - overwrite the original footer. Adds links to accessibility
    and creates buttons (look the same) without a tag 'accesskey' which
    accessibility checkers flag as a warning.
  * **layout.html** - adds needed spaces for the main logo  and make all the
    necessary adjustments for the image and surrounding elements. Creates needed
    spaces for the links in the footer.

* overwrites in _static/css/rcic.css replace defaults or add new items
* conf.py has an overwrite for *mailto* directive.

Color verification was done using:

  * https://app.contrast-finder.org
  * https://accessibleweb.com/color-contrast-checker/

The accessibility checking is done via Web accessibility evaluation tool https://wave.webaim.org/aimscore
See about/accessibility.rst for details and more links.

**When changes or new additions to the pages are needed**:

  * use already existing styles
  * check existing pages for references and do the same.
    This will help to eliminate adding ad hoc changes that could minimize the accessibility. 
  * Verify ALL changes prior to pushing to git repo and build html pages locally.
    Make sure html pages look the same and don't introduce errors.
  * If changes were stylistic or if they use new elements re-check accessibility of
    the pages with the tool. This can only be done to published pages (on http://rcic.uci.edu) 
