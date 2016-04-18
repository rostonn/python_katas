# import unittest
# from fibonacci import fib

# class FibonacciTest(unittest.TestCase):
#
#     def testCalculation(self):
#         self.assertEqual(fib(0),0)
#         self.assertEqual(fib(1),1)
#         self.assertEqual(fib(2),1)
#         self.assertEqual(fib(10),55)
#         self.assertEqual(fib(20),6765)
#
# if __name__ == "__main__":
#     unittest.main()
import unittest
from fibonacci import fib

class FibonacciTest(unittest.TestCase):

    def setUp(self):
        self.fib_elems = ( (0,0), (1,1), (2,1), (3,2), (4,3), (5,5) )
        print ("setUp executed!")

    def testCalculation(self):
        for (i,val) in self.fib_elems:
            self.assertEqual(fib(i), val)

    def tearDown(self):
        self.fib_elems = None
        print ("tearDown executed!")

if __name__ == "__main__":
    unittest.main()
