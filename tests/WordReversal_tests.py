from nose.tools import assert_equal
from Tabl_homework.WordReversal import *

def test_is_letter():
    #Test character
    assert_equal(is_letter('t'), True)
    
    #Test delimiter
    assert_equal(is_letter('?'), False)
    
    #Test number
    assert_equal(is_letter('3'), False)
    
    #Test empty string
    assert_equal(is_letter(''), False)
    
    #Test word, not a single character
    assert_equal(is_letter('word'), False)


def test_word_reverse():
    #Tests standard sentence
    assert_equal(word_reverse('I am   a sentence!!!'), 'sentence a   am I!!!')
    
    #Tests empty string
    assert_equal(word_reverse(''), '')
    
    #Tests sentence with only one word
    assert_equal(word_reverse('word'), 'word')
    
    #Tests sentence starting and ending with a delimiter
    assert_equal(word_reverse('!Ay caramba!'), '!caramba Ay!')
    
    #Tests sentence starting and ending with a word/character
    assert_equal(word_reverse('and/or'), 'or/and')

