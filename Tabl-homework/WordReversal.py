import re

def is_letter(input_char):
    if len(input_char) != 1:
        return False
    elif re.match('[A-z]', input_char) != None:
        return True
    else:
        return False
        

def word_reverse(input_string):
    curr_word = ""
    prev_type = ""
    reversed_string = ""
    
    type_list = []  #allow function to handle sentences that start with non-letters
    word_list = []
    delim_list = []
    
    for i in range(0, len(input_string)):
#         print input_string[i]
        if(prev_type == ""):
            prev_type = is_letter(input_string[i])
            curr_word = input_string[i]
        else:
            curr_type = is_letter(input_string[i])
            if(prev_type == curr_type):
                curr_word += str(input_string[i])
            else:
                if(prev_type == True):
                    word_list.append(curr_word)
                else:
                    delim_list.append(curr_word)
                    
                type_list.append(prev_type)
                prev_type = curr_type
                curr_word = input_string[i]
    
    #to add the last stored 'word' to the appropriate list 
    if(prev_type == True):
        word_list.append(curr_word)
    else:
        delim_list.append(curr_word)       
    
    type_list.append(prev_type)         
    
    #reverse the words in word_list into reversed_list
    word_list.reverse()
    
    word_i = 0
    delim_i = 0

    for t in type_list:
        if(t == True):
            reversed_string += word_list[word_i]
            word_i += 1
        else:
            reversed_string += str(delim_list[delim_i])
            delim_i += 1
            
    return reversed_string