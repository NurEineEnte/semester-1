# Week 1.7, Session 1: Task 2 - unit test for process_data() 

from process_data import process_data
import unittest

class Test_process_data(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(process_data([]), None)
        assert process_data([]) == None
        
    def test_one_int_list(self):
        self.assertEqual(process_data([1]), 1)
        self.assertEqual(process_data([-1]), -1)

    def test_multiple_int_list(self):
        self.assertEqual(process_data([1,-3,2,4]), 4)
        self.assertEqual(process_data([1,5,7,2]), 15)
        self.assertEqual(process_data([-1,-4,-5]), -10)
        self.assertEqual(process_data([1,2,5,1,2,3,2,2,2,2,2,2,2,2,1,1,1,1,4,151,5,21,5,5125]), 5345)

if __name__ == "__main__":
    unittest.main()