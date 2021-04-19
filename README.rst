tutorials
#########
jupyter notebook tutorials for ``ixdat``
========================================
This is a collection of tutorials and worked examples for use of ``ixdat``,
the `In-situ Experimental Data Tool <https://ixdat.readthedocs.io>`_.

The tutorials here are intended to demonstrate general features of ``ixdat`` and
give a sense of the design of the package, as well as key features.

Specific examples of ixdat usage showing how to make and derive certain published
figures and results can be found in article repositories including:

- https://github.com/ScottSoren/pyCOox_public

- https://github.com/kkrempl/Dynamic-Interfacial-Reaction-Rates

Setup
=====

- Install python with, at a minimum: numpy, scipy, matplotlib, and Jupyter notebook.
Anaconda python is recommended

- Install the latest version of ixdat with ``pip install --upgrade ixdat``

- Download or clone this repository or the tutorial you are interested in

- If necessary, download the example data it uses (it will be listed

- Open the tutorial in Jupyter notebook and it should run!

- Help us with your feedback! If something was unclear in the tutorial, it's probably
because we need to improve it.


The Tutorials
=============

Loading, selecting, calibrating, and exporting data
---------------------------------------------------

Location: `loading_appending_and_saving/export_demo_data_as_csv.ipynb <https://github.com/ixdat/tutorials/blob/main/loading_appending_and_saving/export_demo_data_as_csv.ipynb>`_

This tutorial shows with electrochemistry data how to load, append, and export data.
It shows, among other things, the **appending + operator** and how to use the **backend** (save() and get()).

It requires the data files `here <https://www.dropbox.com/sh/ag3pq7vqwuapd0o/AAB2Vqs6ZLZuFuMGp2ZeeWisa?dl=0>`_.


Comparing cycles of a cyclic voltammagram
-----------------------------------------

Location: `simple_ec_analysis/difference_between_two_cvs.ipynb <https://github.com/ixdat/tutorials/blob/main/simple_ec_analysis/difference_between_two_cvs.ipynb>`_

This tutorial, together with the previous one, shows the ``ixdat``'s API for electrochemistry data.
It demonstrates, with CO stripping as an example, the following features:

- Selecting cyclic voltammatry cycles

- Integrating current to get charge passed

- Lining seperate cycles up with respect to potential

It reads ixdat-exported data directly from github.
A worked example based on the methods in this tutorial


Calibrating EC-MS data
----------------------
See these two examples, respectively, for making and using an ixdat EC-MS calibration:

- https://github.com/ScottSoren/pyCOox_public/blob/main/paper_I_fig_S1/paper_I_fig_S1.py

- https://github.com/ScottSoren/pyCOox_public/blob/main/paper_I_fig_2/paper_I_fig_2.py


For developers
==============
Add a pre-commit hook that clears all ipython notebook output, as described here:
https://medium.com/somosfit/version-control-on-jupyter-notebooks-6b67a0cf12a3
