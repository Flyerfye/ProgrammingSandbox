from nose.tools import assert_equal
from Tabl_homework.WordReversal import *

def test_is_letter_a_letter():
    #Test character
    assert_equal(is_letter('t'), True)
    
def test_is_delimeter_a_letter():
    #Test delimiter
    assert_equal(is_letter('?'), False)
    
def test_is_number_a_letter():
    #Test number
    assert_equal(is_letter('3'), False)
    
def test_is_empty_a_letter():
    #Test empty string
    assert_equal(is_letter(''), False)
    
def test_is_word_a_letter():
    #Test word, not a single character
    assert_equal(is_letter('word'), False)
    
def test_word_reverse_sentence():
    #Tests standard sentence
    assert_equal(word_reverse('I am   a sentence!!!'), 'sentence a   am I!!!')
    
def test_word_reverse_empty_string():
    #Tests empty string
    assert_equal(word_reverse(''), '')
    
def test_word_reverse_one_word():
    #Tests sentence with only one word
    assert_equal(word_reverse('word'), 'word')
    
def test_word_reverse_delimiter_start():
    #Tests sentence starting and ending with a delimiter
    assert_equal(word_reverse('!Ay caramba!'), '!caramba Ay!')
    
def test_word_reverse_word_end():
    #Tests sentence starting and ending with a word/character
    assert_equal(word_reverse('and/or'), 'or/and')
    
def test_word_reverse_numbers_and_words():
    #Tests sentence starting and ending with a word/character
    assert_equal(word_reverse('R2D2 and C3PO at your service!'), 'service2your2 at PO3C and D R!')
    
    
    
    
    

