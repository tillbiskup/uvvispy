import unittest

import aspecd.metadata

import uvvispy.metadata


class TestExperimentalDatasetMetadata(unittest.TestCase):

    def setUp(self):
        self.metadata = uvvispy.metadata.ExperimentalDatasetMetadata()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata,
                                   aspecd.metadata.ExperimentalDatasetMetadata))

    def test_has_attributes(self):
        attributes = [
            'measurement', 'sample', 'temperature_control',
            'cell', 'experiment', 'spectrometer',
            ]
        for attr in attributes:
            self.assertTrue(hasattr(self.metadata, attr))

    def test_attribute_sample_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata.sample,
                                   uvvispy.metadata.Sample))

    def test_attribute_temperature_control_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata.temperature_control,
                                   uvvispy.metadata.TemperatureControl))

    def test_attribute_cell_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata.cell,
                                   uvvispy.metadata.Cell))

    def test_attribute_experiment_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata.experiment,
                                   uvvispy.metadata.Experiment))

    def test_attribute_spectrometer_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata.spectrometer,
                                   uvvispy.metadata.Spectrometer))


class TestSample(unittest.TestCase):

    def setUp(self):
        self.metadata = uvvispy.metadata.Sample()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata, aspecd.metadata.Sample))

    def test_has_attributes(self):
        attributes = [
            'name', 'id', 'loi',
            'solvent', 'concentration', 'preparation',
            ]
        for attr in attributes:
            self.assertTrue(hasattr(self.metadata, attr))

    def test_concentration_is_physical_quantity(self):
        self.assertTrue(isinstance(self.metadata.concentration,
                                   aspecd.metadata.PhysicalQuantity))


class TestTemperatureControl(unittest.TestCase):

    def setUp(self):
        self.metadata = uvvispy.metadata.TemperatureControl()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata,
                                   aspecd.metadata.TemperatureControl))

    def test_has_attributes(self):
        attributes = [
            'temperature', 'controller',
            'cryostat', 'cryogen',
            ]
        for attr in attributes:
            self.assertTrue(hasattr(self.metadata, attr))


class TestCell(unittest.TestCase):

    def setUp(self):
        self.metadata = uvvispy.metadata.Cell()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata, aspecd.metadata.Metadata))

    def test_has_attributes(self):
        attributes = [
            'manufacturer', 'type', 'pathlength',
            ]
        for attr in attributes:
            self.assertTrue(hasattr(self.metadata, attr))

    def test_pathlength_is_physical_quantity(self):
        self.assertTrue(isinstance(self.metadata.pathlength,
                                   aspecd.metadata.PhysicalQuantity))


class TestExperiment(unittest.TestCase):

    def setUp(self):
        self.metadata = uvvispy.metadata.Experiment()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata, aspecd.metadata.Metadata))

    def test_has_attributes(self):
        attributes = [
            'type', 'measurement_mode',
            ]
        for attr in attributes:
            self.assertTrue(hasattr(self.metadata, attr))


class TestSpectrometer(unittest.TestCase):

    def setUp(self):
        self.metadata = uvvispy.metadata.Spectrometer()

    def test_instantiate_class(self):
        pass

    def test_is_correct_type(self):
        self.assertTrue(isinstance(self.metadata, aspecd.metadata.Metadata))

    def test_has_attributes(self):
        attributes = [
            'manufacturer', 'model', 'software',
            ]
        for attr in attributes:
            self.assertTrue(hasattr(self.metadata, attr))
