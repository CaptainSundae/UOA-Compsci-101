"""
name: Juan Nicolas Sevilla Siasoco
UPI: jsia894
ID: 8104859
"""
#5.5
def unique_list(string_list):
    """
    Takes a list of strings and returns unique values.

    Arguement:
    string_list -- a list of strings (str)

    Returns:
    unique_strings_list -- a list containing unique strings. (str)

    Tests:

    >>> unique_list(['cat','dog','cat','bug','dog','ant','dog','bug'])
    ['cat', 'dog', 'bug', 'ant']

    >>> unique_list(['Welcome', 'to', 'COMPSCI101', 'To'])
    ['Welcome', 'to', 'COMPSCI101', 'To']
    """
    unique_strings_list=[]
    for word in string_list:
        if word not in unique_strings_list:
            unique_strings_list.append(word)
    return (unique_strings_list)
            
import doctest
doctest.testmod ()

#5.6

def average_from_file(filename):
    """
    Returns an average mark from a file consisting of several marks.

    Argument:
    filename -- an input filename 

    Returns:
    average -- the average score (float)

    Tests:

    >>> average_from_file("marks.txt")
    47.5
    """
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    mark=contents.split(' ')

    total=[]
    for number in mark:
        if number in mark:
            total = total + [int(number)]
    average=sum(total)/len(total)

    return average
import doctest
doctest.testmod ()
    











    
    
   
