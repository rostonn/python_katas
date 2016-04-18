# import unittest
#
# class FailureMessageTest(unittest.TestCase):
#
#     def test_fail(self):
#         self.assertTrue(False, 'failure message goes here')
#
# if __name__ == '__main__':
#     unittest.main()

# import unittest
#
# class TruthTest(unittest.TestCase):
#
#     def test_assert_true(self):
#         self.assertTrue(True)
#
#     def test_assert_false(self):
#         self.assertFalse(False)
#
# if __name__ == '__main__':
#     unittest.main()

import unittest

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.assertNotEqual(1, 3-3)

    def testNotEqual(self):
        self.assertEqual(2, 4-2)

if __name__ == '__main__':
    unittest.main()
