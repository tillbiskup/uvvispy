import importlib
import unittest

import aspecd.plotting


class TestPlottersFromAspecd(unittest.TestCase):

    def setUp(self):
        self.classes = [
            'SinglePlotter1D', 'MultiPlotter1D', 'MultiPlotter1DStacked',
        ]

    def test_classes_exist(self):
        module = importlib.import_module('uvvispy.plotting')
        for class_name in self.classes:
            with self.subTest(classname=class_name):
                if hasattr(aspecd.plotting, class_name):
                    getattr(module, class_name)

    def test_classes_have_correct_type(self):
        module = importlib.import_module('uvvispy.plotting')
        for class_name in self.classes:
            with self.subTest(classname=class_name):
                if hasattr(aspecd.plotting, class_name):
                    aspecd_type = getattr(aspecd.plotting, class_name)
                    obj = getattr(module, class_name)()
                    self.assertTrue(isinstance(obj, aspecd_type))
