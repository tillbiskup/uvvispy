
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4717937.svg
   :target: https://doi.org/10.5281/zenodo.4717937
   :align: right

=====================
UVVisPy documentation
=====================

Welcome! This is the documentation for UVVisPy, a Python package for **processing and analysis of UV-visible (UVVis) spectra** based on the `ASpecD framework <https://www.aspecd.de/>`_. For general information see its `Homepage <https://www.uvvispy.de/>`_. Due to the inheritance from the ASpecD framework, all data generated with the UVVisPy package are completely reproducible and have a complete history.

What is even better: Actual data processing and analysis **no longer requires programming skills**, but is as simple as writing a text file summarising all the steps you want to have been performed on your dataset(s) in an organised way. Curious? Have a look at the following example:


.. code-block:: yaml
    :linenos:

    default_package: uvvispy

    datasets:
      - /path/to/first/dataset
      - /path/to/second/dataset

    tasks:
      - kind: processing
        type: BaselineCorrection
        properties:
          parameters:
            order: 0
      - kind: singleplot
        type: SinglePlotter1D
        properties:
          filename:
            - first-dataset.pdf
            - second-dataset.pdf


Interested in more real-live examples? Check out the :doc:`use cases section <usecases>`.


Features
========

A list of features, not all implemented yet but aimed at for the first public release (uvvispy 0.1):

* fully reproducible processing of UVVis data

* customisable plots

* automatically generated reports

* recipe-driven data analysis


And to make it even more convenient for users and future-proof:

* Open source project written in Python (>= 3.5)

* Developed fully test-driven

* Extensive user and API documentation



.. warning::
  UVVisPy is currently under active development and still considered in Alpha development state. Therefore, expect frequent changes in features and public APIs that may break your own code. Nevertheless, feedback as well as feature requests are highly welcome.


.. _sec-how_to_cite:

How to cite
===========

UVVisPy is free software. However, if you use UVVisPy for your own research, please cite it appropriately:

Till Biskup. UVVisPy (2021). `doi:10.5281/zenodo.xxxxxxx <https://doi.org/10.5281/zenodo.xxxxxxx>`_

To make things easier, UVVisPy has a `DOI <https://doi.org/10.5281/zenodo.xxxxxxx>`_ provided by `Zenodo <https://zenodo.org/>`_, and you may click on the badge below to directly access the record associated with it. Note that this DOI refers to the package as such and always forwards to the most current version.

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg
   :target: https://doi.org/10.5281/zenodo.xxxxxxx


Where to start
==============

Users new to the UVVisPy package should probably start :doc:`at the beginning <audience>`, those familiar with its :doc:`underlying concepts <concepts>` may jump straight to the section explaining frequent :doc:`use cases <usecases>`.

The :doc:`API documentation <api/index>` is the definite source of information for developers, besides having a look at the source code.


Installation
============

To install the UVVisPy package on your computer (sensibly within a Python virtual environment), open a terminal (activate your virtual environment), and type in the following:

.. code-block:: bash

    pip install uvvispy

Have a look at the more detailed :doc:`installation instructions <installing>` as well.


Related projects
================

There is a number of related packages users of the UVVisPy package may well be interested in, as they have a similar scope, focussing on spectroscopy and reproducible research.

* `ASpecD <https://docs.aspecd.de/>`_

  A Python framework for the analysis of spectroscopic data focussing on reproducibility and good scientific practice. The framework the UVVisPy package is based on, developed by T. Biskup.

* `cwepr <https://docs.cwepr.de/>`_

  Package for processing and analysing continuous-wave electron paramagnetic resonance (cw-EPR) data, originally developed by P. Kirchner, currently developed and maintained by M. Schröder and T. Biskup.

* `trepr <https://docs.trepr.de/>`_

  Package for processing and analysing time-resolved electron paramagnetic resonance (TREPR) data, originally developed by J. Popp, currently developed and maintained by M. Schröder and T. Biskup.

You may as well be interested in the `LabInform project <https://www.labinform.de/>`_ focussing on the necessary more global infrastructure in a laboratory/scientific workgroup interested in more `reproducible research <https://www.reproducible-research.de/>`_. In short, LabInform is "The Open-Source Laboratory Information System".

Finally, don't forget to check out the website on `reproducible research <https://www.reproducible-research.de/>`_ covering in more general terms aspects of reproducible research and good scientific practice.


.. toctree::
   :maxdepth: 2
   :caption: User Manual:
   :hidden:

   audience
   concepts
   metadata
   usecases
   installing

.. toctree::
   :maxdepth: 2
   :caption: Developers:
   :hidden:

   people
   developers
   changelog
   roadmap
   dataset-structure
   api/index


License
=======

This program is free software: you can redistribute it and/or modify it under the terms of the **BSD License**. However, if you use the UVVisPy package for your own research, please cite it appropriately. See :ref:`How to cite <sec-how_to_cite>` for details.


A note on the logo
==================

The snake (a python) forms a prism that diffracts the incoming light. The copyright of the logo belongs to J. Popp.
