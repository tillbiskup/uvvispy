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

import os

import aspecd.io
import aspecd.utils


class DatasetImporter(aspecd.io.DatasetImporter):
    """
    Base class for dataset importers of the UVVisPy package.

    This base class takes care of reading the metadata from the
    corresponding YAML file.
    """

    def _import(self):
        metadata_filename = aspecd.utils.basename(self.source) + '.yaml'
        if os.path.exists(metadata_filename):
            yaml = aspecd.utils.Yaml()
            yaml.read_from(metadata_filename)
            self.dataset.metadata.from_dict(yaml.dict)


class ShimadzuASCIIImporter(DatasetImporter):
    """
    Importer for the Shimadzu UVProbe ASCII export file format.

    Note that Shimadzu originally writes a proprietary binary file format
    that contains a lot of parameters. Unfortunately, there seems no
    specification of this format available, and asking the vendor for this
    was so far not successful.

    """


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
        return importer
