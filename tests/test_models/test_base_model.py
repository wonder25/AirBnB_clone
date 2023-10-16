#!/usr/bin/python3
"""test base_model"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_new_instance(self):
        my_model = BaseModel()
        result = my_model
        self.assertIsInstance(result, BaseModel)

    def test_attributes_initialization(self):
        my_model = BaseModel()
        attributes = my_model.__dict__.keys()
        self.assertIn('id', attributes)
        self.assertIn('created_at', attributes)
        self.assertIn('updated_at', attributes)

    def test_str_method(self):
        my_model = BaseModel()
        exp_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        result_str = str(my_model)
        self.assertEqual(result_str, exp_str)

    def test_save_method(self):
        my_model = BaseModel()
        current_updated_at = my_model.updated_at

        my_model.save()
        new_updated_at = my_model.updated_at

        self.assertNotEqual(current_updated_at, new_updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()

        final_dict = my_model.to_dict()

        self.assertIsInstance(final_dict, dict)
        self.assertIn('id', final_dict)
        self.assertIn('__class__', final_dict)
        self.assertIn('created_at', final_dict)
        self.assertIn('updated_at', final_dict)



if __name__ == "__main__":
    unittest.main()
