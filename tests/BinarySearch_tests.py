from nose.tools import assert_equal
from Tabl_homework.BinarySearch import *

def test_list_sorting():
    input_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]
    sort_list(input_list)
    assert_equal(input_list, [1, 2, 3, 4, 5, 6, 7, 11, 12])
    
def test_binary_search():
    input_list = [1, 2, 3, 4, 5, 6, 7, 11, 12]
    #test when element is present 
    #in list
    assert_equal(binary_search(input_list, 6), 5)
    #at either end of list
    assert_equal(binary_search(input_list, 1), 0)
    assert_equal(binary_search(input_list, 12), 8)    
    
    #test when element is not present
    assert_equal(binary_search(input_list, 8), -1)
    
def test_quick_sort():
    #ensures the index of the initial pivot is returned to quick_sort correctly 
    input_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]

    assert_equal(quick_sort(input_list, 0, len(input_list)-1), 6)
    
def test_partition():
    #ensures the index of the initial pivot is unchanged 
    input_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]

    assert_equal(partition(input_list, 0, len(input_list)-1), 6)