#!/usr/bin/python3
""" Python test file """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """ Test Cases for Rectangle """
    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(3, 6)
        cls.r2 = Rectangle(5, 9)
        cls.r3 = Rectangle(5, 3, 6, 7, 9)
        cls.r4 = Rectangle(4, 5, 7, 4, 10)
    def test_width(self):
        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r4.width, 4)

    def test_height(self):
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r2.height, 9)
        self.assertEqual(self.r3.height, 3)
        self.assertEqual(self.r4.height, 5)

    def test_x(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 6)
        self.assertEqual(self.r4.x, 7)

    def test_y(self):
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 7)
        self.assertEqual(self.r4.y, 4)

    def test_no_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_no_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3)
    
    def test_width_no_int(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("Hi", 4)
        
    def test_height_no_int(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, "Howyou")

    def test_x_no_int(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(6, 4, "Holberton")
    
    def test_y_no_int(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(3, 5, 3, "School")
