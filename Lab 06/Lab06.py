#ex 6.1
def get_runway_length(a,v):
    """
    Arguement:
    a -- acceleration (float)
    v -- speed (float)

    >>> get_runway_length(3.5,60.0)
    515
    
    """
    import math
    length=math.ceil((v**(2))/(2*a))
    return length
import doctest
doctest.testmod()

#ex 6.2


def get_gender(gender):
    """
    Argument:
    gender-- male or female

    >>> get_gender("F")
    'Female'

    >>> get_gender("M")
    'Male'

    >>> get_gender("A")
    'Unknown'
    """
    if gender == 'F':
        return 'Female'
    elif gender == 'M':
        return 'Male'
    else:
        return 'Unknown'
    

import doctest
doctest.testmod ()

#ex 6.3

def five_letter_words(filename,output_filename):
    """
    Argument:
    input_filename -- input name of a file
    output_filename -- output name of file
    """
    file=open(filename,'r')
    contents=file.read()
    file.close()

    string_list=contents.split()
    output_file=open(output_filename,'w')
    for word in string_list:
        if len(word)== 5:
            output_file.write(word)
            output_file.write('\n')
    output_file.close()

#ex 6.4
def add_mark(filename,number):
    """
    Arguement:
    filename
    number_list
    """
    file=open(filename,'a')
    contents=file.write(' '+ (str(number)))
    file.close()


        
    
    
    
    







































    
        
          

        
        
