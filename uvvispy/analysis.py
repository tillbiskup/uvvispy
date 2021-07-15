"""Data analysis functionality.

.. sidebar:: Processing vs. analysis steps

    The key difference between processing and analysis steps: While a
    processing step *modifies* the data of the dataset it operates on,
    an analysis step returns a result based on data of a dataset, but leaves
    the original dataset unchanged.


Key to reproducible science is automatic documentation of each analysis
step applied to the data of a dataset. Such an analysis step each is
self-contained, meaning it contains every necessary information to perform
the analysis task on a given dataset.

Analysis steps, in contrast to processing steps (see
:mod:`aspecd.processing` for details), operate on data of a
:class:`aspecd.dataset.Dataset`, but don't change its data. Rather,
some result is obtained that is stored separately, together with the
parameters of the analysis step, in the
:attr:`aspecd.dataset.Dataset.analyses` attribute of the dataset.


Analysis steps implemented
==========================

The analysis steps implemented in this module can be separated into those
specific for UVVis data and those that are generally applicable and were
inherited from the ASpecD framework.


Specific analysis steps for UVVis data
--------------------------------------

Currently, there are no specific analysis steps implemented.


General analysis steps inherited from the ASpecD framework
----------------------------------------------------------

A number of further analysis steps that are generally applicable to
spectroscopic data have been inherited from the underlying ASpecD framework:

* :class:`BasicCharacteristics`

  Extract basic characteristics of a dataset

* :class:`BasicStatistics`

  Extract basic statistical measures of a dataset

* :class:`BlindSNREstimation`

  Blind, *i.e.* parameter-free, estimation of the signal-to-noise ratio

* :class:`PeakFinding`

  Find peaks in 1D datasets


Module documentation
====================

"""

import aspecd.analysis


class BasicCharacteristics(aspecd.analysis.BasicCharacteristics):
    """Extract basic characteristics of a dataset.

    Extracting basic characteristics (minimum, maximum, area, amplitude) of
    a dataset is programmatically quite simple. This class provides a
    working solution from within the ASpecD framework.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.analysis.BasicCharacteristics`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    Extracting the characteristic of a dataset is quite simple:

    .. code-block:: yaml

       - kind: singleanalysis
         type: BasicCharacteristics
         properties:
           parameters:
             type: min
         result: min_of_dataset

    This would simply return the minimum (value) of a given dataset in the
    result assigned to the recipe-internal variable ``min_of_dataset``.
    Similarly, you can extract "max", "area", and "amplitude" from your
    dataset. In case you are interested in the axes values or indices,
    set the output parameter appropriately:

    .. code-block:: yaml

       - kind: singleanalysis
         type: BasicCharacteristics
         properties:
           parameters:
             type: min
             output: axes
         result: min_of_dataset

    In this particular case, this would return the axes values of the
    global minimum of your dataset in the result. Note that those other
    output types are only available for "min" and "max", as "area" and
    "amplitude" have no analogon on the axes.

    Sometimes, you are interested in getting the values of all
    characteristics at once in form of a dictionary:

    .. code-block:: yaml

       - kind: singleanalysis
         type: BasicCharacteristics
         properties:
           parameters:
             type: all
         result: characteristics_of_dataset

    Make sure to understand the different types the result has depending on
    the characteristic and output type chosen. For details, see the table
    above.

    """


class BasicStatistics(aspecd.analysis.BasicStatistics):
    """Extract basic statistical measures of a dataset.

    Extracting basic statistical measures (mean, median, std, var) of
    a dataset is programmatically quite simple. This class provides a
    working solution from within the ASpecD framework.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.analysis.BasicStatistics`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    Some description here...

    .. code-block:: yaml

        - kind: singleanalysis
          type: BasicStatistics

    """


class BlindSNREstimation(aspecd.analysis.BlindSNREstimation):
    """Blind, *i.e.* parameter-free, estimation of the signal-to-noise ratio.

    In spectroscopy, the signal-to-noise ratio (SNR) is usually defined as the
    ratio of mean (of the signal) to standard deviation (of the noise) of a
    signal or measurement.

    For accurate estimations, this requires to be able to separate noise and
    signal, hence to define a part of the overall measurement not including
    signal. As this is not always possible, there are different ways to make
    a blind estimate of the SNR, *i.e.* without additional parameters.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.analysis.BlindSNREstimation`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    Obtaining a blind estimate of the SNR of a dataset is quite simple:

    .. code-block:: yaml

       - kind: singleanalysis
         type: BlindSNREstimation
         result: SNR_of_dataset

    This would simply return the SNR of the data of a given dataset in the
    result assigned to the recipe-internal variable ``SNR_of_dataset``.

    To have more control over the method used to blindly estimate the SNR,
    explicitly provide a method:

    .. code-block:: yaml

       - kind: singleanalysis
         type: BlindSNREstimation
         properties:
           parameters:
             method: der_snr
         result: SNR_of_dataset

    This would use the DER_SNR method as described above.

    """


class PeakFinding(aspecd.analysis.PeakFinding):
    """Peak finding in one dimension.

    Finding peaks is a use case often encountered in analysing spectroscopic
    data, but it is far from trivial and usually requires careful choosing
    of parameters to yield sensible results.

    As the class is fully inherited from ASpecD for simple usage, see the
    ASpecD documentation for the :class:`aspecd.analysis.PeakFinding`
    class for details.

    Examples
    --------
    For convenience, a series of examples in recipe style (for details of
    the recipe-driven data analysis, see :mod:`aspecd.tasks`) is given below
    for how to make use of this class. The examples focus each on a single
    aspect.

    Finding the peak positions of a basically noise-free dataset is quite
    simple:

    .. code-block:: yaml

       - kind: singleanalysis
         type: PeakFinding
         result: peaks

    This would simply return the peak positions of the data of a given dataset
    in the result assigned to the recipe-internal variable ``peaks``.

    To have more control over the method used to find peaks, you can set a
    number of parameters. To get the negative peaks as well (normally,
    only positive peaks will be looked for):

    .. code-block:: yaml

       - kind: singleanalysis
         type: PeakFinding
         properties:
           parameters:
             negative_peaks: True
         result: peaks

    Sometimes it is convenient to have the peaks returned as a dataset,
    to plot the data and highlight the peaks found:

    .. code-block:: yaml

       - kind: singleanalysis
         type: PeakFinding
         properties:
           parameters:
             return_dataset: True
         result: peaks

    From the options that can be set for the function
    :func:`scipy.signal.find_peaks`, you can set "height", "threshold",
    "distance", "prominence", and "width". For details, see the SciPy
    documentation.

    For noisy data, "prominence" can be a good option to only find "true" peaks:

    .. code-block:: yaml

       - kind: singleanalysis
         type: PeakFinding
         properties:
           parameters:
             prominence: 0.2
         result: peaks

    If you supply one of these additional options, you might be interested
    not only in the peak positions, but in the properties of the peaks found
    as well.

    .. code-block:: yaml

       - kind: singleanalysis
         type: PeakFinding
         properties:
           parameters:
             prominence: 0.2
             return_properties: True
         result: peaks

    In this case, the result, here stored in the variable "peaks", will be a
    tuple with the peak positions as first element and a dictionary with
    properties as the second element. Note that if you ask for negative
    peaks as well, this option will silently be ignored and only the peak
    positions returned.

    """
