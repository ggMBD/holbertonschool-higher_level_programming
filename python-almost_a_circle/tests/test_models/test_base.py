#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_instance(self):
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)

    def test_base_id(self):
        base_instance_1 = Base()
        base_instance_2 = Base()
        self.assertEqual(base_instance_1.id, 1)
        self.assertEqual(base_instance_2.id, 2)

    def test_base_custom_id(self):
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)

    def test_to_json_string(self):
        base_instance = Base()
        json_str = Base.to_json_string([base_instance.to_dictionary()])
        self.assertTrue(isinstance(json_str, str))
        self.assertEqual(json_str, '[{"id": 1}]')

    def test_from_json_string(self):
        json_str = '[{"id": 1}]'
        json_list = Base.from_json_string(json_str)
        self.assertTrue(isinstance(json_list, list))
        self.assertEqual(json_list, [{"id": 1}])

    def test_save_to_file(self):
        base_instance = Base()
        Base.save_to_file([base_instance])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}]')

    def test_create(self):
        dictionary = {"id": 5}
        base_instance = Base.create(**dictionary)
        self.assertTrue(isinstance(base_instance, Base))
        self.assertEqual(base_instance.id, 5)

if __name__ == "__main__":
    unittest.main()
