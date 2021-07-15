import importlib
import unittest

import aspecd.processing

import uvvispy.processing


class TestProcessingStepsFromAspecd(unittest.TestCase):

    def setUp(self):
        self.classes = [
            'BaselineCorrection', 'Normalisation', 'ScalarAlgebra',
            'ScalarAxisAlgebra', 'DatasetAlgebra', 'RangeExtraction',
            'CommonRangeExtraction', 'Interpolation', 'Filtering', 'Noise',
            'ChangeAxesValues',
        ]

    def test_classes_exist(self):
        module = importlib.import_module('uvvispy.processing')
        for class_name in self.classes:
            with self.subTest(classname=class_name):
                if hasattr(aspecd.processing, class_name):
                    getattr(module, class_name)

    def test_classes_have_correct_type(self):
        module = importlib.import_module('uvvispy.processing')
        for class_name in self.classes:
            with self.subTest(classname=class_name):
                if hasattr(aspecd.processing, class_name):
                    aspecd_type = getattr(aspecd.processing, class_name)
                    obj = getattr(module, class_name)()
                    self.assertTrue(isinstance(obj, aspecd_type))

    def test_baseline_correction_area_by_default_only_from_right(self):
        processing = uvvispy.processing.BaselineCorrection()
        self.assertEqual([0, 10], processing.parameters["fit_area"])
