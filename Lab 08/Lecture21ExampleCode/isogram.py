

def isogram(word):
    """Returns True if word is an isogram and False otherwise
    Arguments:
        word - word to test if it is an isogram
    Returns:
        True or False
    >>> isogram("subdermatoglyphic")
    True
    >>> isogram("deed")
    True
    >>> isogram("sara")
    False
    """
    letter = word[0]
    num = count(letter,word)
    for i in range(1,len(word)):
        if num != count(word[i],word):
            return False
    return True

def count(letter,word):
    """Returns the number of times letter appears in word
    Arguments:
        letter - letter to count number of appearances
        word - word in which to look for letter
    Returns:
        integer
    >>> count("s","subdermatoglyphic")
    1
    >>> count("e","deed")
    2
    >>> count("a","sara")
    2
    """
    count = 0
    for letter2 in word:
        if letter == letter2:
            count = count + 1
    return count


import doctest
doctest.testmod()

