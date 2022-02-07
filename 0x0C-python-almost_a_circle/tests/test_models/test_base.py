#!/usr/bin/python3
""" Python Test File """
import unittest
from models.base import Base


class Test_Base_Model(unittest.TestCase):
    """ test class case models """

    def test_base_is_correct(self):
        """ test if base is corrcti """
        b = Base(20)
        self.assertEqual(b.id, 20)
        b = Base(100)
        self.assertEqual(b.id, 100)
        b = Base(60)
        self.assertEqual(b.id, 60)
        """ Negative base """
        b = Base(-20)
        self.assertEqual(b.id, -20)

    def test_id_manage(self):
        """ Manage Id to avoid duplicate """
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        b = Base(30)
        self.assertEqual(b.id, 30)
        b = Base()
        self.assertEqual(b.id, 4)
        b = Base(34)
        self.assertEqual(b.id, 34)
        b = Base(6)
        self.assertEqual(b.id, 6)
        b = Base()
        self.assertEqual(b.id, 5)
        b = Base()
        self.assertEqual(b.id, 6)

    def test_arg(self):
        """ Test If more than 1 arg """
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_tuples(self):
        """ Comments test for checker """
        b = Base((1, 3))
        self.assertEqual(b.id, (1, 3))

    def test_lists(self):
        """ Comments test or checkcer """
        b = Base([3])
        self.assertEqual(b.id, [3])
        b = Base([2, 3, 4, "Test String"])
        self.assertEqual(b.id, [2, 3, 4, "Test String"])
        b = Base([])
        self.assertEqual(b.id, [])

    def test_string_id(self):
        """ Comments test or checkcer """
        b = Base("String Test")
        self.assertEqual(b.id, "String Test")

    def test_true_false_as_id(self):
        """ Comments test or checkcer """
        b = Base(True)
        self.assertEqual(b.id, True)
        b = Base(False)
        self.assertEqual(b.id, False)
