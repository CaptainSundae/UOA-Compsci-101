   


def palindrome(word):
    """Returns True if word is a palindrome and False otherwise
    Arguments:
        word - the word to check if it is a palindrome
    Returns:
        True or False
    >>> palindrome("otto")
    True
    >>> palindrome("fact")
    False
    >>> palindrome("Otto")
    False
    >>> palindrome("")
    True
    >>> palindrome(3)
    word is not a string
    False
    """ 
    if isinstance(word,str) == False:
        print("word is not a string")
        return False
    for index in range(len(word)//2):
        if word[index] != word[-index]:
            return False
    return True


import doctest
doctest.testmod() 
