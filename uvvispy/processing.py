"""Processing steps of the UVVisPy package.

.. sidebar::
    processing *vs.* analysis

    For more details on the difference between processing and analysis,
    see the `ASpecD documentation <https://docs.aspecd.de/>`_.


A processing step always operates on a dataset and usually modifies the
numerical data contained therein. The result of a processing step is in any
case again a dataset, in contrast to analysis steps where this is not
necessarily the case. Typical routine processing steps are normalisation (to
area, amplitude, maximum, minimum), and for UVVis spectroscopy such things as
baseline correction.


Processing steps implemented
============================

The processing steps implemented in this module can be separated into those
specific for UVVis data and those that are generally applicable and were
inherited from the ASpecD framework.


Specific processing steps for UVVis data
----------------------------------------

Currently, there are no specific processing steps implemented.


General processing steps inherited from the ASpecD framework
------------------------------------------------------------

A number of further processing steps that are generally applicable to
spectroscopic data have been inherited from the underlying ASpecD framework:

* :class:`BaselineCorrection`

  Correct baseline of dataset.

* :class:`Normalisation`

  Normalise data to minimum, maximum, amplitude, area.

* :class:`ScalarAlgebra`

  Perform scalar algebraic operation on one dataset.

  Operations available: add, subtract, multiply, divide (by given scalar)

* :class:`ScalarAxisAlgebra`

  Perform scalar algebraic operation on axis values of a dataset.

  Operations available: add, subtract, multiply, divide, power (by given scalar)

* :class:`DatasetAlgebra`

  Perform scalar algebraic operation on two datasets.

  Operations available: add, subtract

* :class:`RangeExtraction`

  Extract range of data from a dataset.

* :class:`CommonRangeExtraction`

  Extract the common range of data for multiple datasets using interpolation.

  Useful (and often necessary) for performing algebraic operations on datasets.

* :class:`Interpolation`

  Interpolate data.

* :class:`Filtering`

  Filter data


Further processing steps implemented in the ASpecD framework can be used as
well, by importing the respective modules. In case of recipe-driven data
analysis, simply prefix the kind with ``aspecd``:

.. code-block:: yaml

    - kind: aspecd.processing
      type: <ClassNameOfProcessingStep>


Module documentation
====================

What  follows is the API documentation of each class implemented in this module.

"""

import aspecd.processing


class BaselineCorrection(aspecd.processing.BaselineCorrection):
    """Subtract baseline from dataset.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.BaselineCorrection`
    class for details.

    .. note::
        There is only one difference to the ASpecD class: The area used for
        fitting is by default only the ten percent from the right,
        as optical spectra tend to have features towards the high-energy
        short-wavelength end.


    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    In the simplest case, just invoke the baseline correction with default
    values:

    .. code-block:: yaml

        - kind: processing
          type: BaselineCorrection

    In this case, a zeroth-order polynomial baseline will be subtracted from
    your dataset using ten percent to the right, and in case of a
    2D dataset, the baseline correction will be performed along the first
    axis (index zero) for all indices of the second axis (index 1).

    Of course, often you want to control a little bit more how the baseline
    will be corrected. This can be done by explicitly setting some parameters.

    Suppose you want to perform a baseline correction with a polynomial of
    first order:

    .. code-block:: yaml

       - kind: processing
         type: BaselineCorrection
         properties:
           parameters:
             order: 1

    """

    def __init__(self):
        super().__init__()
        self.parameters["fit_area"] = [0, 10]


class Normalisation(aspecd.processing.Normalisation):
    """Normalise data.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.Normalisation`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.


    In the simplest case, just invoke the normalisation with default values:

    .. code-block:: yaml

       - kind: processing
         type: Normalisation

    This will normalise your data to their maximum.

    Sometimes, normalising to maximum is not what you need, hence you can
    control in more detail the criterion using the appropriate parameter:

    .. code-block:: yaml

       - kind: processing
         type: Normalisation
         properties:
           parameters:
             kind: amplitude

    In this case, you would normalise to the amplitude, meaning setting the
    difference between minimum and maximum to one. For other kinds, see above.

    If you want to normalise not over the entire range of the dataset,
    but only over a dedicated range, simply provide the necessary parameters:

    .. code-block:: yaml

       - kind: processing
         type: Normalisation
         properties:
           parameters:
             range: [50, 150]

    In this case, we assume a 1D dataset and use indices, requiring the data
    to span at least over 150 points. Of course, it is often more convenient
    to provide axis units. Here you go:

    .. code-block:: yaml

       - kind: processing
         type: Normalisation
         properties:
           parameters:
             range: [340, 350]
             range_unit: axis

    """


class ScalarAlgebra(aspecd.processing.ScalarAlgebra):
    """Perform scalar algebraic operation on one dataset.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.ScalarAlgebra`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    In case you would like to add a fixed value of 42 to your dataset:

    .. code-block:: yaml

       - kind: processing
         type: ScalarAlgebra
         properties:
           parameters:
             kind: add
             value: 42

    Similarly, you could use "minus", "times", "by", "add", "subtract",
    "multiply", or "divide" as kind - resulting in the given algebraic
    operation.

    """


class ScalarAxisAlgebra(aspecd.processing.ScalarAxisAlgebra):
    """Perform scalar algebraic operation on the axis of a dataset.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.ScalarAxisAlgebra`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    In case you would like to add a fixed value of 42 to the first axis
    (index 0) your dataset:

    .. code-block:: yaml

       - kind: processing
         type: ScalarAxisAlgebra
         properties:
           parameters:
             kind: plus
             axis: 0
             value: 42

    Similarly, you could use "minus", "times", "by", "add", "subtract",
    "multiply", "divide", and "power" as kind - resulting in the given
    algebraic operation.

    """


class DatasetAlgebra(aspecd.processing.DatasetAlgebra):
    """Perform scalar algebraic operation on two datasets.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.DatasetAlgebra`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    In case you would like to add the data of the dataset referred to by its
    label ``label_to_other_dataset`` to your dataset:

    .. code-block:: yaml

       - kind: processing
         type: DatasetAlgebra
         properties:
           parameters:
             kind: plus
             dataset: label_to_other_dataset

    Similarly, you could use "minus", "add", "subtract" as kind - resulting
    in the given algebraic operation.

    As mentioned already, the data of both datasets need to have identical
    shape, and comparison is only meaningful if the axes are compatible as
    well. Hence, you will usually want to perform a CommonRangeExtraction
    processing step before doing algebra with two datasets:

    .. code-block:: yaml

       - kind: multiprocessing
         type: CommonRangeExtraction
         results:
           - label_to_dataset
           - label_to_other_dataset

       - kind: processing
         type: DatasetAlgebra
         properties:
           parameters:
             kind: plus
             dataset: label_to_other_dataset
         apply_to:
           - label_to_dataset

    """


class RangeExtraction(aspecd.processing.RangeExtraction):
    """Extract range of data from dataset.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.RangeExtraction`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    In the simplest case, just invoke the range extraction with one range
    only, assuming a 1D dataset:

    .. code-block:: yaml

       - kind: processing
         type: RangeExtraction
         properties:
           parameters:
             range: [5, 10]

    This will extract the range ``data[5:10]`` from your data (and adjust
    the axis accordingly). In case of 2D data, it would be fairly similar,
    except of now providing two ranges:

    .. code-block:: yaml

       - kind: processing
         type: RangeExtraction
         properties:
           parameters:
             range:
              - [5, 10]
              - [3, 6]

    Additionally, you can provide step sizes, just as you can do when
    slicing in Python:

    .. code-block:: yaml

       - kind: processing
         type: RangeExtraction
         properties:
           parameters:
             range: [5, 10, 2]

    This is equivalent to ``data[5:10:2]`` or ``data[(slice(5, 10, 2))]``,
    accordingly.

    Sometimes, it is more convenient to give ranges in axis values rather
    than indices. This can be achieved by setting the parameter ``unit`` to
    "axis":

    .. code-block:: yaml

       - kind: processing
         type: RangeExtraction
         properties:
           parameters:
             range: [5, 10]
             unit: axis

    Note that in this case, setting a step is meaningless and will be
    silently ignored. Furthermore, the nearest axis values will be used for
    the range.

    In some cases you may want to extract a range by providing percentages
    instead of indices or axis values. Even this can be done:

    .. code-block:: yaml

       - kind: processing
         type: RangeExtraction
         properties:
           parameters:
             range: [0, 10]
             unit: percentage

    Here, the first ten percent of the data of the 1D dataset will be
    extracted, or more exactly the indices falling within the first ten
    percent. Note that in this case, setting a step is meaningless and will be
    silently ignored. Furthermore, the nearest axis values will be used for
    the range.

    """


class CommonRangeExtraction(aspecd.processing.CommonRangeExtraction):
    """
    Extract the common range of data for multiple datasets using interpolation.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the
    :class:`aspecd.processing.CommonRangeExtraction` class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    In case you would like to bring all datasets currently loaded into your
    recipe to a common range (use with caution, however), things can be as
    simple as:

    .. code-block:: yaml

       - kind: multiprocessing
         type: CommonRangeExtraction

    Note that this will operate on *all* datasets currently available in
    your recipe, including results from other processing steps. Therefore,
    it is usually better to be explicit, using ``apply_to``. Otherwise,
    you can use this processing step early on in your recipe.

    Usually, however, you will want to restrict this to a subset using
    ``apply_to`` and provide labels for the results:

    .. code-block:: yaml

       - kind: multiprocessing
         type: CommonRangeExtraction
         results:
           - dataset1_cut
           - dataset2_cut
         apply_tp:
           - dataset1
           - dataset2

    If you want to perform algebraic operations on datasets, the data of both
    datasets need to have identical shape, and comparison is only meaningful
    if the axes are compatible as well. Hence, you will usually want to
    perform a CommonRangeExtraction processing step before doing algebra
    with two datasets:

    .. code-block:: yaml

       - kind: multiprocessing
         type: CommonRangeExtraction
         results:
           - label_to_dataset
           - label_to_other_dataset

       - kind: processing
         type: DatasetAlgebra
         properties:
           parameters:
             kind: plus
             dataset: label_to_other_dataset
         apply_to:
           - label_to_dataset

    For details of the algebraic operations on datasets,
    see :class:`DatasetAlgebra`.

    """


class Interpolation(aspecd.processing.Interpolation):
    """Interpolate data.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.Interpolation`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    Generally, interpolating requires to provide both, a range and a number
    of points:

    .. code-block:: yaml

       - kind: processing
         type: Interpolation
         properties:
           parameters:
             range: [10, 100]
             npoints: 901

    This would interpolate your data between their indices 10 and 100 using
    901 points. As it is sometimes (often) more convenient to work with
    axis units, you can tell the processing step to use axis values instead
    of indices:

    .. code-block:: yaml

       - kind: processing
         type: Interpolation
         properties:
           parameters:
             range: [400, 700]
             npoints: 1201
             unit: axis

    This would interpolate your (1D) data between the axis values 400 and
    700 using 1201 points.

    """


class Filtering(aspecd.processing.Filtering):
    """Filter data.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.processing.Filtering`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    Generally, filtering requires to provide both, a type of filter and a
    window length. Therefore, for uniform and Gaussian filters, this would be:

    .. code-block:: yaml

       - kind: processing
         type: Filtering
         properties:
           parameters:
             type: uniform
             window_length: 10

    Of course, at least uniform filtering (also known as boxcar or moving
    average) is strongly discouraged due to the artifacts introduced.
    Probably the best bet for applying a filter to smooth your data is the
    Savitzky-Golay filter:

    .. code-block:: yaml

       - kind: processing
         type: Filtering
         properties:
           parameters:
             type: savitzky-golay
             window_length: 10
             order: 3

    Note that for this filter, you need to provide the polynomial order as
    well. To get best results, you will need to experiment with the
    parameters a bit.

    """
