from Animals.pet_animals.cat import *
import unittest
from unittest import mock
import io


class test_Cat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Beginning of test class")

    def setUp(self):
        self.cat1 = Cat("Garfield", "orange")
        self.cat2 = Cat("Colonel Meow", "black")

    def tearDown(self):
        print("End of test case")

    @classmethod
    def tearDownClass(cls):
        print("End of test class")

    def test_sound(self):
        self.assertEqual(self.cat1.sound(), None)
        self.assertEqual(self.cat2.sound(), None)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.cat1.sound()
            self.cat2.sound()
        assert fake_stdout.getvalue() == "Meow meow prrrrrr\n" \
                                         "Meow meow prrrrrr\n"

    def test_describe(self):
        self.assertEqual(self.cat1.describe("lazy"), None)
        self.assertEqual(self.cat2.describe("majestic"), None)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.cat1.describe("lazy")
            self.cat2.describe("majestic")
        assert fake_stdout.getvalue() == "Garfield, the lazy, orange cat\n" \
                                         "Colonel Meow, the majestic, black cat\n"

    def test_feed(self):
        self.cat1.feed(30),
        self.assertEqual(self.cat1.weight, 6.0 + 30 * 0.1)
        self.cat2.feed(61)
        self.assertEqual(self.cat2.weight, 6.0 + 61 * 0.1)

    def test_setWeight(self):
        self.cat1.setWeight(6)
        self.cat2.setWeight(3)
        self.assertEqual(self.cat1.weight, 6)
        self.assertEqual(self.cat2.weight, 3)

    def test_getWeight(self):
        self.assertEqual(self.cat1.getWeight(), None)
        self.assertEqual(self.cat2.getWeight(), None)

        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.cat1.getWeight()
            self.cat2.getWeight()
        assert fake_stdout.getvalue() == "Garfield weights 6.0 kg.\n" \
                                         "Colonel Meow weights 6.0 kg.\n"

    def test_on_a_diet(self):
        self.cat1.on_a_diet(2)
        self.assertEqual(self.cat1.weight, 4)
        self.cat2.on_a_diet(3)
        self.assertEqual(self.cat2.weight, 3)
