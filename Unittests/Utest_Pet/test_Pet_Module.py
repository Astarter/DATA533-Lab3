from Animals.pet_animals.pet import *
import unittest
from unittest import mock
import io


class test_Pet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Beginning of test class")

    def setUp(self):
        self.pet1 = Pet("Garfield")
        self.pet2 = Pet("Colonel Meow")

    def tearDown(self):
        print("End of test case")

    @classmethod
    def tearDownClass(cls):
        print("End of test class")

    def test_intro(self):
        self.assertEqual(self.pet1.intro(), None)
        self.assertEqual(self.pet2.intro(), None)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.pet1.intro()
            self.pet2.intro()
        assert fake_stdout.getvalue() == "Hello, my name is Garfield, I'm your pet\n" \
                                         "Hello, my name is Colonel Meow, I'm your pet\n"

    def test_display(self):
        self.assertEqual(self.pet1.display(), None)
        self.assertEqual(self.pet2.display(), None)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.pet1.display()
            self.pet2.display()
        assert fake_stdout.getvalue() == "Pet's name: Garfield\n" \
                                         "Pet's name: Colonel Meow\n"
