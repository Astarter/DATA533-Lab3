from Animals.livestocks.livestock import *
import unittest
from unittest import mock
import io


class test_livestock(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This test class starts")

    def setUp(self):
        print("A test case starts.")
        self.L1 = Livestock("Ben")
        self.L2 = Livestock("Bob")

    def tearDown(self):
        print("Tear down. This test case is completed.\n")

    @classmethod
    def tearDownClass(cls):
        print("This test class is completed.")

    def test_introduce(self):
        self.assertEqual(self.L1.intoduce(), None)
        self.assertEqual(self.L2.intoduce(), None)

        # Combined the last 2 assertions:
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.L1.intoduce()
            self.L2.intoduce()

        assert fake_stdout.getvalue() == "Hi, I am Ben's livestock\n" \
                                         "Hi, I am Bob's livestock\n"

    def test_display(self):
        self.assertEqual(self.L1.display(), None)
        self.assertEqual(self.L2.display(), None)

        # Combined the last 2 assertions:
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.L1.display()
            self.L2.display()

        assert fake_stdout.getvalue() == "Infor:\n" \
                                         "Owner: Ben\n" \
                                         "Infor:\n" \
                                         "Owner: Bob\n"

