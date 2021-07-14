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

    def _write_metadata_file(self, metadata_dict=dict()):
        yaml = aspecd.utils.Yaml()
        yaml.dict = metadata_dict
        yaml.write_to(self.metadata_file)

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.importer,
                                   aspecd.io.DatasetImporter))

    def test_import_reads_metadata_if_present(self):
        metadata_dict = {'experiment': {'type': 'spectrum'}}
        self._write_metadata_file(metadata_dict)
        self.importer.source = self.dataset_file
        self.dataset.import_from(self.importer)
        self.assertEqual(metadata_dict["experiment"]["type"],
                         self.dataset.metadata.experiment.type)


class TestShimadzuASCIIImporter(unittest.TestCase):

    def setUp(self):
        self.importer = uvvispy.io.ShimadzuASCIIImporter()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.importer,
                                   uvvispy.io.DatasetImporter))


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
