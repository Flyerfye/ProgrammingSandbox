from BinarySearch import binary_search, sort_list
from WordReversal import word_reverse

def val_in_list(input_list, input_val):
    val_index = binary_search(input_list, input_val)
    
    if(val_index != -1):
        print str(input_val) + " found at index " + str(val_index) + "!"
        return True
    else:
        print str(input_val) + " not found in input list"
        return False
    
example_list = [5, 6, 12, 2, 1, 11, 4, 3, 7]
example_string = "I am   a sentence!!!"

#makes sure the input list is sorted
sort_list(example_list)

print example_list
val_in_list(example_list, 5)
val_in_list(example_list, 8)

print "\n"
print example_string
reversed_string = word_reverse(example_string)
print reversed_string