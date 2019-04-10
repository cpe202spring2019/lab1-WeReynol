# Wesley Reynolds
# Paul Hatalsky
# CPE 202
# CPE 202 Lab 0

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # If the input parameter of the function is None, check to see if the ValueError exception is raised.
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        # Test with integers
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([3, 2, 1]), 3)
        self.assertEqual(max_list_iter([1, 3, 2]), 3)
        
        # Test with strings
        self.assertEqual(max_list_iter([1, 2, "Hello"]), 2)
        self.assertEqual(max_list_iter([1, "Hello", 2]), 2)
        self.assertEqual(max_list_iter(["Hello",2, 1]), 2)

        # Test with no numbers
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter(["Hello", "Hi", "Hola"]), None)

    def test_reverse_rec(self):
        # If the input parameter of the function is None, check to see if the ValueError exception is raised.
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

        # Check with integers
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([3,3,3]),[3,3,3])
        self.assertEqual(reverse_rec([3,2,1]),[1,2,3])
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search(self):
        # If the input parameter of the function is None, check to see if the ValueError exception is raised.
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(tlist, tlist, tlist, tlist)

        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val) - 1

        list_val2 = [10]
        high2 = len(list_val2) - 1

        list_val3 = []
        high3 = len(list_val3) - 1

        self.assertEqual(bin_search(4, low, high, list_val), 4) # Test the 5th value in the list
        self.assertEqual(bin_search(0, low, high, list_val), 0) # Test the 1st value in the list
        self.assertEqual(bin_search(1, low, high, list_val), 1) # Test the 2nd value in the list
        self.assertEqual(bin_search(2, low, high, list_val), 2) # Test the 3rd value in the list
        self.assertEqual(bin_search(3, low, high, list_val), 3) # Test the 4th value in the list
        self.assertEqual(bin_search(7, low, high, list_val), 5) # Test the 6th value in the list
        self.assertEqual(bin_search(8, low, high, list_val), 6) # Test the 7th value in the list
        self.assertEqual(bin_search(9, low, high, list_val), 7) # Test the 8th value in the list
        self.assertEqual(bin_search(10, low, high, list_val), 8) # Test the 9th value in the list
        self.assertEqual(bin_search(5, low, high, list_val), None) # Test for a number that is not in the list
        self.assertEqual(bin_search(5, 1, 0, list_val), None) # Test with low > high
        self.assertEqual(bin_search(10, low, high2, list_val2), 0) # Test a list with one item (the target)
        self.assertEqual(bin_search(9, low, high2, list_val2), None) # Test a list with one item (not the target)
        self.assertEqual(bin_search(5, low, high3, list_val3), None) # Test an empty list

if __name__ == "__main__":
        unittest.main()

    
