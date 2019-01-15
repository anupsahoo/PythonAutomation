import unittest
from unittests.test_example import Example

tc1 = unittest.TestLoader().loadTestsFromTestCase(Example)

smoke_tests = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smoke_tests)