from Animals.pet_animals.cat import *
import unittest


class test_Cat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        self.pet1 = Cat("Garfield", "orange")
        self.pet2 = Cat("Colonel Meow", "black")
        print("setUp")

    def test_sound(self):
        self.assertEqual(self.pet1.sound(), "Meow meow prrrrrr")
        self.assertEqual(self.pet2.sound(), "Meow meow prrrrrr")
        print("test_sound")

    def test_describe(self):
        self.assertEqual(self.pet1.describe("lazy"), "Garfield, the lazy, orange cat")
        self.assertEqual(self.pet2.describe("majestic"), "Colonel Meow, the majestic, black cat")
        print("test_describe")

    def test_feed(self):
        self.pet1.feed(30),
        self.assertEqual(self.pet1.weight, 6.0+30*0.1)
        self.pet2.feed(61)
        self.assertEqual(self.pet2.weight, 6.0+61*0.1)
        print("test_feed")

    def test_setWeight(self):
        self.pet1.setWeight(6)
        self.pet2.setWeight(3)
        self.assertEqual(self.pet1.weight, 6)
        self.assertEqual(self.pet2.weight, 3)

    def test_getWeight(self):
        self.assertEqual(self.pet1.getWeight(), "Garfield weights 6.0 kg.")
        self.assertEqual(self.pet2.getWeight(), "Colonel Meow weights 6.0 kg.")

    def test_on_a_diet(self):
        self.pet1.on_a_diet(2)
        self.assertEqual(self.pet1.weight, 4)

        self.pet2.on_a_diet(3)
        self.assertEqual(self.pet2.weight, 3)
        print("test_feed")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
