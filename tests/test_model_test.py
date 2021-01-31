import unittest
from src.models.model_test import ModelTest


class TestModel(unittest.TestCase):
    def test_model_test_create(self):
        model_test = ModelTest("elson", 35)
        self.assertEqual(model_test.name, "elson")
