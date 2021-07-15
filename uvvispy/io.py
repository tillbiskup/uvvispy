"""
General facilities for input (and output).

In order to work with UVVis data, these data need to be imported into the
UVVisPy package. Therefore, the module provides importers for specific file
formats.

Another class implemented in this module is the
:class:`uvvispy.io.DatasetImporterFactory`, a prerequisite for recipe-driven
data analysis. This factory returns the correct dataset importer for a
specific dataset depending on the information provided (usually, a filename).

"""
import io
import os

import aspecd.annotation
import aspecd.io
import aspecd.metadata
import aspecd.utils
import numpy as np


class DatasetImporter(aspecd.io.DatasetImporter):
    """
    Base class for dataset importers of the UVVisPy package.

    This base class takes care of reading the metadata from the
    corresponding YAML file. There are two options for classes inheriting
    from this class: either a call to :meth:`super()._import` or a call to
    :meth:`_read_metadata`. As soon as either of these calls exists in the
    actual importers and a YAML file with the same base name as the source
    exists, the metadata will be read from this file and mapped to the dataset.

    Note that it is a good idea to first read the metadata from this file
    and afterwards import the raw data, as this way you can easily overwrite
    values in the metadata that may have gone wrong in the (manually
    written) metadata file. Usually, parameters provided in the raw data are
    more reliable, as they are automatically written by the spectrometer
    software.
    """

    def __init__(self, source=None):
        super().__init__(source=source)
        self._metadata = dict()

    def _import(self):
        self._read_metadata()

    def _read_metadata(self):
        metadata_filename = aspecd.utils.basename(self.source) + '.yaml'
        if os.path.exists(metadata_filename):
            self._import_metadata(metadata_filename)
            self._map_metadata()
            self._add_comment_as_annotation()
        self.dataset.metadata.from_dict(self._metadata)

    def _import_metadata(self, filename):
        yaml = aspecd.utils.Yaml()
        yaml.read_from(filename)
        self._metadata = yaml.dict

    def _map_metadata(self):
        mapper = aspecd.metadata.MetadataMapper()
        mapper.version = self._metadata["format"]["version"]
        mapper.metadata = self._metadata
        root_path = os.path.split(os.path.abspath(__file__))[0]
        mapper.recipe_filename = os.path.join(root_path,
                                              'metadata_mapper.yaml')
        mapper.map()
        self._metadata = mapper.metadata

    def _add_comment_as_annotation(self):
        if "comment" in self._metadata:
            annotation = aspecd.annotation.Comment()
            annotation.comment = self._metadata["comment"]
            self.dataset.annotate(annotation)


class ShimadzuASCIIImporter(DatasetImporter):
    # noinspection PyUnresolvedReferences
    """
    Importer for the Shimadzu UVProbe ASCII export file format.

    Note that the Shimadzu UV Probe software originally writes a proprietary
    binary file format that contains a lot of parameters. Unfortunately,
    there seems no specification of this format available, and asking the
    vendor for this was so far not successful. The ASCII export format,
    however, is rather sparse in terms of additional information, besides
    the numerical data. A typical file will start as follows:

    .. code-block::

        "<filename_without_extension> - RawData"
        "Wavelength nm."	"Abs."
        300,00	0,322
        301,00	0,310
        302,00	0,289


    The first two lines are obviously header lines, with the first line
    starting with the filename excluding its extension, here represented by
    ``<filename_without_extension>``. The second line contains sort of
    information for the two columns with data. In this particular case,
    the decimal separator is the *comma*, not the dot. Otherwise, it would
    be fairly easy to just use the :class:`aspecd.io.TxtImporter`.

    .. note::
        If an accompanying metadata file (with same basename and "yaml" as
        extension) is present, its contents will be read automatically and
        mapped to the dataset.

    Attributes
    ----------
    parameters : :class:`dict`
        Parameters controlling the import

        skiprows : :class:`int`
            Number of rows to skip in text file (*e.g.*, header lines)

    """

    def __init__(self, source=None):
        super().__init__(source=source)
        self.extension = '.txt'
        self.parameters["skiprows"] = 2

    def _import(self):
        self._read_metadata()
        self._read_data()
        self._set_axes_description()

    def _read_data(self):
        with open(self.source) as file:
            contents = file.read()
        # noinspection PyTypeChecker
        raw_data = \
            np.loadtxt(io.StringIO(contents.replace(',', '.')),
                       skiprows=self.parameters["skiprows"])
        self.dataset.data.axes[0].values = raw_data[:, 0]
        self.dataset.data.data = raw_data[:, 1]

    def _set_axes_description(self):
        self.dataset.data.axes[0].quantity = "wavelength"
        self.dataset.data.axes[0].unit = "nm"
        self.dataset.data.axes[1].quantity = "absorbance"
        self.dataset.data.axes[1].unit = ""


class DatasetImporterFactory(aspecd.io.DatasetImporterFactory):
    """Factory for creating importer objects based on the source provided.

    Often, data are available in different formats, and deciding which
    importer is appropriate for a given format can be quite involved. To
    free other classes from having to contain the relevant code, a factory
    can be used.

    Currently, the sole information provided to decide about the appropriate
    importer is the source (a string). A concrete importer object is
    returned by the method ``get_importer()``. If no source is provided,
    an exception will be raised.

    If the source string does not match any of the importers handled by this
    module, the standard importers from the ASpecD framework are checked.
    See the documentation of the :class:`aspecd.io.DatasetImporterFactory`
    base class for details.

    """

    def _get_importer(self):
        importer = DatasetImporter()
        if self.source.endswith(".txt"):
            importer = ShimadzuASCIIImporter(source=self.source)
        return importer
