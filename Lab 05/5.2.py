def print_short(string_list):
    """ Prints the string from a list of strings that is less than four characters long

    >>> print(['Welcome', 'to', 'COMPSCI101'])
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
