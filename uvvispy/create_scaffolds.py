"""
Module for creating scaffolds of modules conforming to the ASpecD framework.

This module may form the basis of functionality of the ASpecD framework
greatly facilitating with creating packages derived from the ASpecD
framework, as it is intended to create modules and class stubs.
"""

import importlib
import os


class CreateProcessingStepClasses:

    def __init__(self):
        self.package = 'uvvispy'
        self.module = 'processing'
        self.classes = [
            'BaselineCorrection', 'Normalisation', 'ScalarAlgebra',
            'ScalarAxisAlgebra', 'DatasetAlgebra', 'RangeExtraction',
            'CommonRangeExtraction', 'Interpolation', 'Filtering', 'Noise',
            'ChangeAxesValues',
        ]

    def create_module(self):
        module_filename = self.module + '.py'
        if not os.path.exists(module_filename):
            self._module_head(module_filename)
        aspecd_module = importlib.import_module('aspecd.' + self.module)
        package_module = \
            importlib.import_module(self.package + '.' + self.module)
        with open(module_filename, 'a') as file:
            for class_name in self.classes:
                if hasattr(aspecd_module, class_name) \
                        and not hasattr(package_module, class_name):
                    self._class_stub(class_name, file)

    def _class_stub(self, class_name, file):
        print("Create scaffold for class '" + class_name + "'")
        file.write('\n\n' + 'class ' + class_name +
                   '(aspecd.processing.' + class_name + '):' + '\n')
        file.write('    """<one line of description>.' + '\n\n')
        file.write('    As the class is fully inherited from ASpecD ' +
                   'for simple usage, see the\n' +
                   '    ASpecD documentation for the :class:`aspecd.' +
                   self.module + '.' + class_name + '`\n' +
                   '    class for details.' +
                   '\n\n')
        file.write('    Examples\n' +
                   '    --------\n' +
                   '    For convenience, a series of examples in recipe ' +
                   'style (for details of\n' +
                   '    the recipe-driven data analysis, see ' +
                   ':mod:`aspecd.tasks`) is given below\n' +
                   '    for how to make use of this class. The examples ' +
                   'focus each on a single\n' +
                   '    aspecd.\n\n' +
                   '    Some description here...\n\n' +
                   '    .. code-block:: yaml\n\n' +
                   '        - kind: ' + self.module + '\n'
                   '          type: ' + class_name + '\n\n'
                   )
        file.write('    """' + '\n')

    def _module_head(self, module_filename):
        print("Create file")
        with open(module_filename, 'w+') as file:
            file.write('"""' + self.module.capitalize() + '.\n\n')
            file.write('And here some more documentation...\n')
            file.write('"""\n\n')
            file.write('import aspecd.' + self.module + '\n')
