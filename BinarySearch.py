#searches for val in sorted input list
def binary_search(sorted_list, val):
    left = 0
    right = len(sorted_list) - 1
    mid = -1

    while(left < right):
        mid = int((left + right)/2)
        cur_val = sorted_list[mid]
        
        if(cur_val == val):
            return mid
        elif(val < cur_val):
            right = mid - 1
        else:
            left = mid + 1
    
    return -1
    
# calls quick sort function to sort the input list
# no return value because lists are mutable in Python
def sort_list(input_list):
    quick_sort(input_list, 0, len(input_list)-1)
    
def quick_sort(input_list, low, high):
    if low < high:
        # partition the array
        index = partition(input_list, low, high)
        
        # call quick sort on left and right side of partition
        quick_sort(input_list, low, index - 1)
        quick_sort(input_list, index + 1, high)
    
def partition(input_list, low, high):
    # set last element as partition
    pivot_val = input_list[high]
    
    swap_index = low
    
    for i in range(low, high):
        if input_list[i] < pivot_val:
            temp = input_list[i]
            input_list[i] = input_list[swap_index]
            input_list[swap_index] = temp
            swap_index += 1
            
    input_list[high] = input_list[swap_index]
    input_list[swap_index] = pivot_val
    
    return swap_index