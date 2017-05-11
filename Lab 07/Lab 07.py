
#Ex 7.1
def get_smallest_number(number_list):
    """Gets the smallest number from a list.

    >>> get_smallest_number([62, 38, 19, 7])
    7

    >>> get_smallest_number([1, 66, 2, 38, 19, 7, 29, 35, 42, 15])
    1
    """
    smallest =number_list[0]
    for i in range(0,len(number_list)):
        if number_list[i] < smallest:
            smallest= number_list[i]
    return smallest

import doctest
doctest.testmod()

#Ex 7.2

def sum_series(n):
    """
    Takes an odd integer as a parameter and returns the sum of the following series.

    >>> sum_series(99)
    45.12
    """
    sum_of_int=0
    for i in range(1,n,2):
        sum_of_int=sum_of_int+ (i/(i+2))
    return round(sum_of_int,2)

import doctest
doctest.testmod()

def is_arithmetic_sequence(integer_list):
    """
    >>> is_arithmetic_sequence([5, 10, 15, 20, 25, 30, 35])
    True
    """
    difference = integer_list[1] - integer_list[0]
    for i in range(0,len(integer_list)-1):
        if integer_list[i+1] != integer_list[i]+difference:
            return False
    return True

import doctest
doctest.testmod()
    

    


        
        
        
        
    
    
    
    


    


