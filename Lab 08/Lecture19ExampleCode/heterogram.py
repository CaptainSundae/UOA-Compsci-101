

def heterogram(sentence):
    """Returns True if sentence is a heterogram and False otherwise
    Arguments:
        sentence - a string to test if it is a heterogram
    Returns:
        True or False
    >>> heterogram("otto")
    False
    >>> heterogram("fact")
    True
    >>> heterogram("i am")
    True
    >>> heterogram("i am a boy")
    False
    >>> heterogram("")
    True
    >>> heterogram(3)
    sentence is not a string
    False
    """
    if not isinstance(sentence,str):
        print("sentence is not a string")
        return False
    found_letters = []
    for letter in sentence:
        if letter in found_letters:
            return False
        found_letters += letter
    return True


import doctest
doctest.testmod() 
