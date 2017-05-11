"""
Name: Nicolas Siasoco
UPI: jsia894
ID: 8104859
"""
#6.5
def cumulative_sum(integer_list):
    """
    Takes a list and calculates the cumulative sum.

    Argument:
    integer list -- a list of integers

    Return:
    cumulative list -- the cumulative sum of the list

    Tests:

    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    
    """
    cumulative_list=[]
    cumulative_integer = 0

    for integer in integer_list:
        cumulative_integer = cumulative_integer + integer  
        cumulative_list.append(cumulative_integer)

    return cumulative_list

import doctest
doctest.testmod ()

#6.6

def unique_file(input_filename,output_filename):
    """
    Takes the contents of one file and creates a file of unique words
    Argument:
    input filename -- input name of file
    output filename -- output name of file

    """

    file=open(input_filename, 'r')
    contents=file.read()
    file.close()

    string_list=contents.split()
    output_file=open(output_filename,'w')
    for word in string_list:
        output_file.write(word)
        output_file.write('\n')
    output_file.close()




















    
