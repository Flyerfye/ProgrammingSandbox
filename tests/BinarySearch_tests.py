from nose.tools import assert_equal
from Tabl_homework.BinarySearch import sort_list

def test_list_sorting():
    input_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]
    sort_list(input_list)
    assert_equal(input_list, [1, 2, 3, 4, 5, 6, 7, 11, 12])