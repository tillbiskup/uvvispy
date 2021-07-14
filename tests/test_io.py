import datetime
import os
import unittest

import aspecd.io
import aspecd.utils

import uvvispy.dataset
import uvvispy.io


class TestDatasetImporter(unittest.TestCase):

    def setUp(self):
        self.importer = uvvispy.io.DatasetImporter()
        self.dataset = uvvispy.dataset.ExperimentalDataset()
        self.metadata_file = 'foo.yaml'
        self.dataset_file = 'foo.txt'

    def tearDown(self):
        if os.path.exists(self.metadata_file):
            os.remove(self.metadata_file)

    def _write_metadata_file(self, metadata_dict=None):
        yaml = aspecd.utils.Yaml()
        yaml.dict = metadata_dict
        yaml.write_to(self.metadata_file)

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.importer,
                                   aspecd.io.DatasetImporter))

    def test_import_reads_metadata_if_present(self):
        metadata_dict = {
            'format': {'version': '0.1.4'},
            'experiment': {'type': 'spectrum'},
            'measurement': {'labbook': ''},
        }
        self._write_metadata_file(metadata_dict)
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual(metadata_dict["experiment"]["type"],
                         self.dataset.metadata.experiment.type)

    def test_import_reads_datetime_from_metadata(self):
        metadata_dict = {
            'format': {'version': '0.1.4'},
            'measurement': {'start': {'date': '2018-05-13',
                                      'time': '11:05:00'},
                            'labbook': ''}
        }
        self._write_metadata_file(metadata_dict)
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        # noinspection PyTypeChecker
        datetime_str = " ".join([metadata_dict["measurement"]["start"]["date"],
                                 metadata_dict["measurement"]["start"]["time"]])
        datetime_object = datetime.datetime.strptime(datetime_str,
                                                     "%Y-%m-%d %H:%M:%S")
        self.assertEqual(datetime_object,
                         self.dataset.metadata.measurement.start)

    def test_import_maps_metadata_from_old_format(self):
        metadata_dict = {
            'format': {'version': '0.1.3'},
            'general': {'operator': 'John Doe',
                        'labbook': ''}
        }
        self._write_metadata_file(metadata_dict)
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual(metadata_dict["general"]["operator"],
                         self.dataset.metadata.measurement.operator)

    def test_import_maps_labbook_entry(self):
        metadata_dict = {
            'format': {'version': '0.1.4'},
            'measurement': {'labbook': 'loi:42.1001/lb/tb/uvvis/yyyy-mm-dd_id'}
        }
        self._write_metadata_file(metadata_dict)
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual(metadata_dict["measurement"]["labbook"],
                         self.dataset.metadata.measurement.labbook_entry)

    def test_import_maps_labbook_entry_in_old_format(self):
        metadata_dict = {
            'format': {'version': '0.1.3'},
            'general': {'labbook': 'loi:42.1001/lb/tb/uvvis/yyyy-mm-dd_id'}
        }
        self._write_metadata_file(metadata_dict)
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual(metadata_dict["general"]["labbook"],
                         self.dataset.metadata.measurement.labbook_entry)


class TestShimadzuASCIIImporter(unittest.TestCase):

    def setUp(self):
        self.importer = uvvispy.io.ShimadzuASCIIImporter()
        self.dataset = uvvispy.dataset.ExperimentalDataset()
        self.dataset_file = 'foo.txt'
        self.metadata_file = 'foo.yaml'
        self.data = None

    def tearDown(self):
        if os.path.exists(self.dataset_file):
           os.remove(self.dataset_file)
        if os.path.exists(self.metadata_file):
           os.remove(self.metadata_file)

    def _write_dataset_file(self):
        with open(self.dataset_file, "w+") as f:
            for line in self.data:
                f.write(line + '\n')

    def _write_metadata_file(self, metadata_dict=None):
        yaml = aspecd.utils.Yaml()
        yaml.dict = metadata_dict
        yaml.write_to(self.metadata_file)

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.importer,
                                   uvvispy.io.DatasetImporter))

    def test_read_from_file_skips_header(self):
        self.data = [
            '"filename - RawData"',
            '"Wavelength nm."	"Abs."',
            '300,00	0,322',
            '301,00	0,310',
        ]
        self._write_dataset_file()
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual(300., self.dataset.data.axes[0].values[0])
        self.assertEqual(0.322, self.dataset.data.data[0])

    def test_import_reads_metadata_if_present(self):
        self.data = [
            '"filename - RawData"',
            '"Wavelength nm."	"Abs."',
            '300,00	0,322',
            '301,00	0,310',
        ]
        self._write_dataset_file()
        metadata_dict = {
            'format': {'version': '0.1.4'},
            'experiment': {'type': 'spectrum'},
            'measurement': {'labbook': ''},
        }
        self._write_metadata_file(metadata_dict)
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual(metadata_dict["experiment"]["type"],
                         self.dataset.metadata.experiment.type)

    def test_read_from_file_sets_first_axis_descriptions(self):
        self.data = [
            '"filename - RawData"',
            '"Wavelength nm."	"Abs."',
            '300,00	0,322',
            '301,00	0,310',
        ]
        self._write_dataset_file()
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual("wavelength", self.dataset.data.axes[0].quantity)
        self.assertEqual("nm", self.dataset.data.axes[0].unit)

    def test_read_from_file_sets_second_axis_descriptions(self):
        self.data = [
            '"filename - RawData"',
            '"Wavelength nm."	"Abs."',
            '300,00	0,322',
            '301,00	0,310',
        ]
        self._write_dataset_file()
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual("absorbance", self.dataset.data.axes[1].quantity)
        self.assertEqual("", self.dataset.data.axes[1].unit)


class TestDatasetImporterFactory(unittest.TestCase):

    def setUp(self):
        self.factory = uvvispy.io.DatasetImporterFactory()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.factory,
                                   aspecd.io.DatasetImporterFactory))

    def test_get_importer_returns_dataset_importer(self):
        source = 'foo'
        importer = self.factory.get_importer(source=source)
        self.assertTrue(isinstance(importer, uvvispy.io.DatasetImporter))

    def test_get_importer_with_shimadzu_ascii_returns_correct_importer(self):
        source = './testdata/sa281-02-280K.txt'
        importer = self.factory.get_importer(source=source)
        self.assertTrue(isinstance(importer, uvvispy.io.ShimadzuASCIIImporter))
