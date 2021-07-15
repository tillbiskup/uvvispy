import importlib
import unittest

import aspecd.analysis

# import uvvispy.analysis


class TestProcessingStepsFromAspecd(unittest.TestCase):

    def setUp(self):
        self.classes = [
            'BasicCharacteristics', 'BasicStatistics', 'BlindSNREstimation',
            'PeakFinding',
        ]

    def test_classes_exist(self):
        module = importlib.import_module('uvvispy.analysis')
        for class_name in self.classes:
            with self.subTest(classname=class_name):
                if hasattr(aspecd.analysis, class_name):
                    getattr(module, class_name)

    def test_classes_have_correct_type(self):
        module = importlib.import_module('uvvispy.analysis')
        for class_name in self.classes:
            with self.subTest(classname=class_name):
                if hasattr(aspecd.analysis, class_name):
                    aspecd_type = getattr(aspecd.analysis, class_name)
                    obj = getattr(module, class_name)()
                    self.assertTrue(isinstance(obj, aspecd_type))
