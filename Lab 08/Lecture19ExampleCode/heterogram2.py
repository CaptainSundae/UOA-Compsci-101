
def heterogram2(sentence):
    """Returns True if sentence is a heterogram and False otherwise
    Arguments:
        sentence - a string to test if it is a heterogram
    Returns:
    True or False
    >>> heterogram2("otto")
    False
    >>> heterogram2("fact")
    True
    >>> heterogram2("i am")
    True
    >>> heterogram2("i am a boy")
    False
    >>> heterogram2("i am boy")
    True
    >>> heterogram2("")
    True
    >>> heterogram2(3)
    sentence is not a string
    False
    """
    if isinstance(sentence,str) == False:
        print("sentence is not a string")
        return False
    found_letters = []
    punctuation = [" ", ",", ".", ";", ":", "?", "!"]
    for letter in sentence:
        if letter in found_letters:
            if letter not in punctuation:
                return False
        found_letters += letter
    return True


import doctest
doctest.testmod() 
