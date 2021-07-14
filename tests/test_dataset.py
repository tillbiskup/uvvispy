import unittest

import aspecd.dataset
import aspecd.metadata

import uvvispy.dataset
import uvvispy.metadata


class TestExperimentalDataset(unittest.TestCase):

    def setUp(self):
        self.dataset = uvvispy.dataset.ExperimentalDataset()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.dataset,
                                   aspecd.dataset.ExperimentalDataset))

    def test_has_correct_metadata(self):
        self.assertTrue(
            isinstance(self.dataset.metadata,
                       uvvispy.metadata.ExperimentalDatasetMetadata))


class TestCalculatedDataset(unittest.TestCase):

    def setUp(self):
        self.dataset = uvvispy.dataset.CalculatedDataset()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.dataset,
                                   aspecd.dataset.CalculatedDataset))


class TestDatasetFactory(unittest.TestCase):

    def setUp(self):
        self.factory = uvvispy.dataset.DatasetFactory()
        self.dataset_filename = "testdata/sa281-02-280K.txt"

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.factory,
                                   aspecd.dataset.DatasetFactory))

    def test_get_dataset_returns_uvvis_dataset(self):
        dataset = self.factory.get_dataset(source=self.dataset_filename)
        self.assertTrue(isinstance(dataset,
                                   uvvispy.dataset.ExperimentalDataset))
