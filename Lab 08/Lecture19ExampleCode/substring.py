   


def substring(my_word,my_string):
    """Returns True if my_word is a substring of my_string and False otherwise
    Arguments:
        my_word - a string we want to test to see if it exists within another string
        my_string - a string we want to see if our first string exists within
    Returns:
        True or False
    >>> substring("ab","ab fab")
    True
    >>> substring("Ab","ab fab")
    False
    >>> substring("ab","Fact")
    False
    >>> substring("","Fact")
    True
    >>> substring("","")
    True
    >>> substring(3,"fact")
    my_word is not a string
    False
    >>> substring("ab",3)
    my_string is not a string
    False
    """ 
    if isinstance(my_word,str) == False:
        print("my_word is not a string")
        return False
    if isinstance(my_string,str) == False:
        print("my_string is not a string")
        return False
    if my_word in my_string:
        return True
    return False





import doctest
doctest.testmod()        
