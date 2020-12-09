from Animals.livestocks.cow import *
import unittest
from unittest import mock
import io


class test_cow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This test class starts.")

    def setUp(self):
        print("A test case starts.")
        self.C1 = Cow("Ben")
        self.C2 = Cow("Bob", 1500, 150)

    def tearDown(self):
        print("This test case is complete")

    @classmethod
    def tearDownClass(cls):
        print("This test class is completed")

    def test_makesound(self):
        self.assertEqual(self.C1.makeSound(), None)
        self.assertEqual(self.C2.makeSound(), None)

        # Combined the last 2 assertions:
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.C1.makeSound()
            self.C2.makeSound()

        assert fake_stdout.getvalue() == "Mooooooooooo!!!\n" \
                                         "Mooooooooooo!!!\n"

    def test_eat(self):
        self.C1.eat(-10)
        self.assertEqual(self.C1.weight, 100)  # Won't change

        self.C1.eat(0)
        self.assertEqual(self.C1.weight, 100)  # Won't change

        self.C1.eat(2000)
        self.assertEqual(self.C1.weight, 100 + (1000 / 100))

        self.C1.eat(120)
        self.assertEqual(self.C1.weight, 100 + (1000 / 100) + (120 / 100))

    def test_setPrice(self):
        self.C1.setPrice(0)
        self.assertEqual(self.C1.price, 0)

        self.C1.setPrice(100)
        self.assertEqual(self.C1.price, 100)

        self.C1.setPrice(1000000)
        self.assertEqual(self.C1.price, 1000000)

        self.C1.setPrice(-10)
        self.assertEqual(self.C1.price, -10)
