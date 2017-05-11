

def semordnilap(word):
    """Returns True if word is a semordnilap and False otherwise
    Arguments:
        word - the word to test
    Returns:
        True or False
    >>> semordnilap("dog")
    True
    >>> semordnilap("dan")
    False
    """
    dictionary_file = open("unixdict.txt", "r")
    dictionary = dictionary_file.read()
    dictionary_list = dictionary.split()
    if word in dictionary_list and reverse(word) in dictionary_list:
        return True
    return False

def reverse(word):
    """Returns the string in word in reverse order
    Arguments:
        word - the word to reverse
    Returns:
        the string word in reverse order
    >>> reverse("dog")
    'god'
    >>> reverse("swamp")
    'pmaws'
    >>> reverse("")
    ''
    """
    new_word = ""
    for i in range(len(word)-1,-1,-1):
        new_word += word[i]
    return new_word

import doctest
doctest.testmod()
