"""
Lab 05
UPI:jsia894
"""
#exercise 5.1
def print_even (number_list):
    """ Prints all the even numbers in a parameter

    >>> print_even([4,1,3,2,7])
    4
    2

    """
    for numbers in number_list:
        if numbers % 2 == 0:
            print (numbers)
            
import doctest
doctest.testmod()

#exercise 5.2

def print_short(string_list):
    """ Prints the string from a list of strings that is less than four characters long

    >>> print_short(['Welcome', 'to', 'COMPSCI101'])
    to

    >>> print_short (['Monday', 'Mon', 'Sunday', 'Sun'])
    Mon
    Sun
    """
    for word in string_list:
        if len(word) < 4:
            print (word)

import doctest
doctest.testmod ()

#exercise 5.3

def count_names_in_file (filename):
    """Prints the number of names in a text file

    >>> count_names_in_file ("names.txt")
    6
    """
    file= open(filename, 'r')
    contents = file.read()
    file.close()

    word_list = contents.split(',')
    return (len(word_list))
import doctest
doctest.testmod ()

#exercise 5.4

def find_words(character, filename):
    """Prints all the words which contains the specified character

    >>> find_words("n", "names.txt")
    andrew
    ann
    angela

    >>> find_words ("e", "names.txt")
    andrew
    peter
    angela

    """

    file = open(filename, 'r')
    contents = file.read()
    file.close()

    string= contents.split(',')
    for name in string:
        if character in name:
            print (name)
       
import doctest
doctest.testmod ()












