UVVisPy documentation
=====================

Welcome! This is the documentation for UVVisPy. For general information see its `homepage <https://www.uvvispy.de/>`_.

UVVisPy is a Python package based on the `ASpecD framework <https://www.aspecd.de/>`_ for processing and analysing optical spectra obtained using UVVis spectroscopy. It emphasises reproducibility and good scientific practice.


Features
--------

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


Installation
------------

Install the package by running::

  pip install uvvispy

This will install the version from the `Python Package Index (PyPI) <https://pypi.org/>`_. To get the latest development version, clone the repository from `GitHub <https://github.com/tillbiskup/uvvispy>`_ and install it locally. In any case, it is highly recommended to use virtual environments to separate dependencies.



Where to start
--------------

Users new to UVVisPy should probably start :doc:`at the beginning <audience>`, those familiar with its :doc:`underlying concepts <concepts>` an planning to help in further developing may jump straight to the section explaining how to :doc:`contribute to the development of UVVisPy <developers>`.

The :doc:`API documentation <api/index>` is the definite source of information for developers, besides having a look at the source code.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   audience
   concepts
   developers
   api/index



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


A note on the logo
------------------

The snake (a python) forms a prism that diffracts the incoming light. The copyright of the logo belongs to J. Popp.
