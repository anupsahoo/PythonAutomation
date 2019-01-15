import unittest

class Example2(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("I will run for every class example 2 ")

    def setUp(self):
        print("I will run every tests method example 2")

    def test_methodA(self):
        print("Method A")
        a = True
        self.assertTrue(a, "a is not true ")
        self.assertFalse(a, "a is True")
        # assert a is not True


    def test_methodB(self):
        print("Method B example 2")

    def tearDown(self):
        print("I will run after every method example 2")
    @classmethod
    def tearDownClass(cls):
        print("I will run after every class example 2")


if __name__ == "__main__":
    unittest.main(verbosity=2)