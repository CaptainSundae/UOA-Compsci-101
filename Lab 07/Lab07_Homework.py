"""
UPI: jsia894
ID:
Name:
"""

#ex 7.4
def reverse_numbers(filename):
    """
    Takes the filename as a parameter and reads a list of integers and displays them in reverse

    Arguement:
    filename -- a filename
    
    """
    inputfile=open(filename, 'r')
    contents=inputfile.read()
    numbers =contents.split()
    inputfile.close()
    numbers.reverse()
 
    list=[]
    for index in numbers:
        print(index)
        


#ex 7.5

def print_doubles(integer_list):
    """
    Takes a list of integers as a parameter and prints all the integers in the list that are exactly double the previous integer in the list.

    Arguement:
    integer_list -- a list of integers

    >>> print_doubles([3, 5, 10])
    10

    >>> print_doubles([3, 6, 5, 10])
    6
    10

    >>> print_doubles([2, 3, 6, 8, 16, 20, 40, 80])
    6
    16
    40
    80
    
    """
    for i in range(len(integer_list)-1):
        if integer_list[i]*2==integer_list[i+1]:
            print(integer_list[i+1])

import doctest
doctest.testmod()
    
