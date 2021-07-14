"""
Metadata: crucial information about the numerical data.

Metadata
========

In this module, the individual metadata classes are defined which contain the
individual information about the experiment:

  * :class:`uvvispy.metadata.ExperimentalDatasetMetadata`

What may sound like a minor detail is one key aspect of the UVVisPy package:
The metadata and their structure provide a unified interface for all
functionality operating on datasets. Furthermore, the metadata contained
particularly in the :class:`uvvispy.metadata.ExperimentalDatasetMetadata` class
are the result of several years of practical experience. Reproducible research
is only possible if all information necessary is always recorded, and this
starts with all the metadata accompanying a measurement. Defining what kind
of metadata is important and needs to be recorded, together with metadata
formats easily writable by the experimenters *during* recording the data
requires a thorough understanding of both, the method and the setup(s) used.
For an overview of the structures of the dataset classes and their
corresponding metadata, see the :doc:`dataset structure </dataset-structure>`
section.


Module documentation
====================

"""

import aspecd.metadata


class ExperimentalDatasetMetadata(aspecd.metadata.ExperimentalDatasetMetadata):
    """Set of all metadata for a dataset object.

    Metadata as a unified structure of information coupled to the dataset are
    necessary for the understanding, analysis and processing of data,
    especially in UVVisPy. Too many parameters have an direct influence to the
    spectral shape of the spectrum that anything other than saving them in an
    appropriate place and accessing them automatised in the respective tasks
    is no option. Some parameters are written automatically by the
    spectrometer's software, others, depending also on the actual setup (that
    may change over time!) are omitted and it is highly recommended those
    should be noted by hand, for example in an *.info-file.*

    Attributes
    ----------
    cell: :class:`uvvispy.metadata.Measurement`
        Metadata corresponding to the cell used for the experiment.

    experiment: :class:`uvvispy.metadata.Experiment`
        Metadata corresponding to the actual experiment.

    spectrometer: :class:`uvvispy.metadata.Spectrometer`
        Metadata corresponding to the spectrometer used for the experiment.

    """

    def __init__(self):
        super().__init__()
        self.sample = Sample()
        self.temperature_control = TemperatureControl()
        self.cell = Cell()
        self.experiment = Experiment()
        self.spectrometer = Spectrometer()


class Sample(aspecd.metadata.Sample):
    """Metadata corresponding to the sample measured.

    Attributes
    ----------
    solvent : :class:`str`
        Solvent used.

    concentration : :class:`aspecd.metadata.PhysicalQuantity`
        Type of the cell as given by the manufacturer.

    preparation : :class:`str`
        Details on the preparation of the sample (concise!)

    """

    def __init__(self):
        super().__init__()
        self.solvent = ''
        self.concentration = aspecd.metadata.PhysicalQuantity()
        self.preparation = ''


class TemperatureControl(aspecd.metadata.TemperatureControl):
    """Metadata corresponding to the temperature control.

    Attributes
    ----------
    cryostat : :class:`str`
        Type of the cryostat used (as given by the manufacturer).

    cryogen : :class:`str`
        Type of cryogen.

        Typical values are "LN2", "LHe"

    """

    def __init__(self):
        super().__init__()
        self.cryostat = ''
        self.cryogen = ''


class Cell(aspecd.metadata.Metadata):
    """Metadata corresponding to the cell used for the experiment.

    Attributes
    ----------
    manufacturer : :class:`str`
        Manufacturer of the optical cell.

    type : :class:`str`
        Type of the cell as given by the manufacturer.

    pathlength : :class:`aspecd.metadata.PhysicalQuantity`
        Optical pathlength of the cell, usually 1 cm.

    """

    def __init__(self):
        super().__init__()
        self.manufacturer = ''
        self.type = ''
        self.pathlength = aspecd.metadata.PhysicalQuantity()


class Experiment(aspecd.metadata.Metadata):
    """Metadata corresponding to the actual experiment.

    Attributes
    ----------
    type : :class:`str`
        Type of experiment, such as "spectrum" or "kinetics"

    measurement_mode : :class:`str`
        Measurement mode of the experiment.

        Typical values are "absorption", "transmission"

    """

    def __init__(self):
        super().__init__()
        self.type = ''
        self.measurement_mode = ''


class Spectrometer(aspecd.metadata.Metadata):
    """Metadata corresponding to the spectrometer used for the experiment.

    Attributes
    ----------
    manufacturer : :class:`str`
        Name of the manufacturer

    model : :class:`str`
        Model as provided by the manufacturer, usually a short string

    software : :class:`str`
        Name and version of the software used to record the data

    """

    def __init__(self):
        super().__init__()
        self.manufacturer = ''
        self.model = ''
        self.software = ''
