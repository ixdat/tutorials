tutorials
#########
jupyter notebook tutorials for ``ixdat``
========================================
This is a collection of tutorials and worked examples for use of ``ixdat``,
the `In-situ Experimental Data Tool <https://ixdat.readthedocs.io>`_.

The tutorials here are intended to demonstrate general features of ``ixdat`` and
give a sense of the design of the package, as well as key features.

Links to specific examples of ixdat usage showing how to make published figures 
and derive published results can be found in article repositories. For a complete
list of tutorials and article repositories, see the ixdat documentation:

https://ixdat.readthedocs.io/en/latest/tutorials.html

Setup
=====

- Install python with, at a minimum: numpy, scipy, matplotlib, and Jupyter notebook.
  Anaconda python is recommended

- Install the latest version of ixdat with ``pip install --upgrade ixdat``

  This main version of the tutorials repository works with ixdat v0.2
  For a version compatible with ixdat v0.1.x, see the `ixdat_v0p1 branch <https://github.com/ixdat/tutorials/tree/ixdat_v0p1>`_

- Download or clone this repository or the tutorial you are interested in

- If necessary, download the example data it uses (it will be described below).

- Open the tutorial in Jupyter notebook and it should run!

- Help us with your feedback! If something was unclear in the tutorial, it's probably
  because we need to improve it.


The Tutorials
=============

Electrochemistry
----------------


Tutorial 1: Reading and Using Data
..................................

Location: `electrochemistry/01_reading_and_using_data.ipynb <https://github.com/ixdat/tutorials/blob/main//electrochemistry/01_reading_and_using_data.ipynb>`_

This tutorial shows with electrochemistry data how to load, append, and export data.
It shows, among other things, the **appending + operator** and how to use the **backend** (save() and get()).

It requires the data files `here <https://www.dropbox.com/sh/ag3pq7vqwuapd0o/AAB2Vqs6ZLZuFuMGp2ZeeWisa?dl=0>`_.


Tutorial 2: Comparing Cycles
............................

Location: `electrochemistry/02_comparing_cycles.ipynb <https://github.com/ixdat/tutorials/blob/main//electrochemistry/02_comparing_cycles.ipynb>`_

This tutorial, together with the previous one, shows the ``ixdat``'s API for electrochemistry data.
It demonstrates, with CO stripping as an example, the following features:

- Selecting cyclic voltammatry cycles

- Integrating current to get charge passed

- Lining seperate cycles up with respect to potential

It reads ixdat-exported data directly from github.
A worked example based on the methods in this tutorial


Spectroelectrochemistry
-----------------------



Location: `spectroelectrochemistry/spectroelectrochemistry_demo.ipynb <https://github.com/ixdat/tutorials/blob/main/spectroelectrochemistry/spectroelectrochemistry_demo.ipynb>`_

The sample data is not yet publically available.

EC-MS
----------------------
See these two examples, respectively, for making and using an ixdat EC-MS calibration:

- https://github.com/ScottSoren/pyCOox_public/blob/main/paper_I_fig_S1/paper_I_fig_S1.py

- https://github.com/ScottSoren/pyCOox_public/blob/main/paper_I_fig_2/paper_I_fig_2.py


For developers
==============
Add a pre-commit hook that clears all ipython notebook output, as described here:
https://medium.com/somosfit/version-control-on-jupyter-notebooks-6b67a0cf12a3
