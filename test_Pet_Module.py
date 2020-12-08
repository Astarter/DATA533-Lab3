from Animals.pet_animals.pet import *
import unittest


class test_Pet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        self.pet1 = Pet("Garfield")
        self.pet2 = Pet("Colonel Meow")
        print("setUp")

    def test_intro(self):
        self.assertEqual(self.pet1.intro(), "Hello, my name is Garfield, I'm your pet")
        self.assertEqual(self.pet2.intro(), "Hello, my name is Colonel Meow, I'm your pet")
        print("test_intro")

    def test_display(self):
        self.assertEqual(self.pet1.display(), "Pet's name: Garfield")
        self.assertEqual(self.pet2.display(), "Pet's name: Colonel Meow")
        print("test_display")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
