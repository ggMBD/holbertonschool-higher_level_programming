#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_instance(self):
        square_instance = Square(5)
        self.assertIsInstance(square_instance, Square)

    def test_square_size_property(self):
        square_instance = Square(5)
        self.assertEqual(square_instance.size, 5)

    def test_square_size_setter(self):
        square_instance = Square(5)
        square_instance.size = 10
        self.assertEqual(square_instance.size, 10)

    def test_square_area(self):
        square_instance = Square(5)
        self.assertEqual(square_instance.area(), 25)

    def test_square_str(self):
        square_instance = Square(5, 2, 3, 7)
        self.assertEqual(str(square_instance), "[Square] (7) 2/3 - 5")

    def test_square_update_args(self):
        square_instance = Square(5, 2, 3, 7)
        square_instance.update(1, 10, 20, 30)
        self.assertEqual(str(square_instance), "[Square] (1) 20/30 - 10")

    def test_square_update_kwargs(self):
        square_instance = Square(5, 2, 3, 7)
        square_instance.update(id=1, size=10, x=20, y=30)
        self.assertEqual(str(square_instance), "[Square] (1) 20/30 - 10")

    def test_square_to_dictionary(self):
        square_instance = Square(5, 2, 3, 7)
        dictionary = square_instance.to_dictionary()
        self.assertEqual(dictionary, {'id': 7, 'size': 5, 'x': 2, 'y': 3})

if __name__ == "__main__":
    unittest.main()
