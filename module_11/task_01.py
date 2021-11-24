import random
import unittest
from mergesort import *

test_list = [random.randint(1, 100) for x in range(1, 50)]
test_list_copy = test_list.copy()
test_list_copy.sort()
class TestMergeSort(unittest.TestCase):
    def test_sort(self):
        self.assertListEqual(merge_sort(test_list), test_list_copy)


if bool([]) is False:
    print('q')
unittest.main()


