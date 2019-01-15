import unittest

class Example(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("I will run for every class ")

    def setUp(self):
        print("I will run every tests method")

    def test_methodA(self):
        print("Method A")
        a = True
        self.assertTrue(a, "a is not true ")
        self.assertFalse(a, "a is True")
        # assert a is not True


    def test_methodB(self):
        print("Method B")

    def tearDown(self):
        print("I will run after every method")
    @classmethod
    def tearDownClass(cls):
        print("I will run after every class")


if __name__ == "__main__":
    unittest.main(verbosity=2)