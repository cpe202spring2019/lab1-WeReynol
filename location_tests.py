# Wesley Reynolds
# Paul Hatalsky
# CPE 202
# CPE 202 Lab 0

import unittest
from location import *

class TestLab1(unittest.TestCase):
    def test_repr(self):
        # Locations
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1

        # Test cases
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2),"Location('Paris', 48.9, 2.4)")
        self.assertEqual(repr(loc3),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc4),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        # Locations
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1

        # Test cases
        self.assertFalse(loc1 == loc2)
        self.assertTrue(loc1 == loc3)
        self.assertTrue(loc1 == loc4)
        self.assertFalse(loc2 == loc3)
        self.assertFalse(loc2 == loc4)
        self.assertTrue(loc3 == loc4)

if __name__ == "__main__":
        unittest.main()
