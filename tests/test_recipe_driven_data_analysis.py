import os
import unittest

import aspecd.tasks
import aspecd.utils


class TestRecipeDrivenDataAnalysis(unittest.TestCase):

    def setUp(self):
        self.recipe_file = 'recipe.yaml'
        self.history_filename = ''

    def tearDown(self):
        if os.path.exists(self.recipe_file):
            os.remove(self.recipe_file)
        if self.history_filename and os.path.exists(self.history_filename):
            os.remove(self.history_filename)

    def _write_recipe_file(self, recipe_dict=None):
        yaml = aspecd.utils.Yaml()
        yaml.dict = recipe_dict
        yaml.write_to(self.recipe_file)

    def _cook_recipe(self):
        chef_de_service = aspecd.tasks.ChefDeService()
        chef_de_service.recipe_filename = self.recipe_file
        self.history_filename = chef_de_service.serve()

    def test_recipe_with_import_only(self):
        recipe_dict = {
            "default_package": 'uvvispy',
            "datasets": ['./testdata/sa281-02-280K.txt'],
        }
        self._write_recipe_file(recipe_dict=recipe_dict)
        self._cook_recipe()
