import importlib
import unittest

import uvvispy.processing


class TestProcessingStepsFromAspecd(unittest.TestCase):

    def setUp(self):
        self.classes = [
            'Normalisation', 'Integration', 'Differentiation',
            'ScalarAlgebra', 'Projection', 'SliceExtraction',
            'RangeExtraction', 'BaselineCorrection ', 'Averaging',
            'ScalarAxisAlgebra', 'DatasetAlgebra', 'Interpolation',
            'Filtering', 'CommonRangeExtraction', 'Noise',
            'ChangeAxesValues',
        ]

    def test_classes_exist(self):
        module = importlib.import_module('uvvispy.processing')
        for classname in self.classes:
            with self.subTest(classname=classname):
                getattr(module, classname)
