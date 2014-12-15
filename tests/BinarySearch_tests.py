from nose.tools import assert_equal
from Tabl_homework.BinarySearch import *

def test_list_sorting():
    #test to make sure the quick-sort algorithm works properly
    input_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]
    sort_list(input_list)
    assert_equal(input_list, [1, 2, 3, 4, 5, 6, 7, 11, 12])
    
def test_binary_search_num_in_middle():
    #test when element is present 
    input_list = [1, 2, 3, 4, 5, 6, 7, 11, 12]
    assert_equal(binary_search(input_list, 6), 5)
    
def test_binary_search_num_at_start():
    #test when element is present at start of list
    input_list = [1, 2, 3, 4, 5, 6, 7, 11, 12]
    assert_equal(binary_search(input_list, 1), 0)
    

def test_binary_search_num_at_end():
    #test when element is present at end of list
    input_list = [1, 2, 3, 4, 5, 6, 7, 11, 12]
    assert_equal(binary_search(input_list, 12), 8)  
    

def test_binary_search_not_in_list():
    #test when element is not present
    input_list = [1, 2, 3, 4, 5, 6, 7, 11, 12]
    assert_equal(binary_search(input_list, 8), -1)
    
def test_quick_sort():
    #test to ensure the index of the initial pivot is returned to quick_sort correctly 
    input_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]
    assert_equal(quick_sort(input_list, 0, len(input_list)-1), 6)
    
def test_partition():
    #test to ensures the index of the initial pivot is selected properly
    input_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]
    assert_equal(partition(input_list, 0, len(input_list)-1), 6)
    
    