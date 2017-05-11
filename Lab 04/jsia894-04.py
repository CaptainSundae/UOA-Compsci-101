"""
Name: Juan Nicolas Sevilla Siasoco
UPI:jsia894
ID:
"""
#Exercise 4.7
def grade (mark):
    """
    Converts a numeric mark into a descriptive grade.

    Arguement:
    Mark -- marks out of 100 (float)

    Return:
    Grade -- a descriptive grade, either A, B, C or D (string)

    Tests:
    >>> grade(24)
    'D'

    >>> grade (80.0)
    'A'

    >>> grade (56.23)
    'C'

    """
    if mark < 50:
        grade=('D')
    elif 50 <= mark < 65:
        grade=('C')
    elif 65 <= mark < 80:
        grade=('B')
    elif mark >=80:
        grade=('A')
    return (grade)
import doctest
doctest.testmod ()

#Exercise 4.8

def calculate_day (day, month, year):
    """ Calculate the day of the week for a given date

    Arguement:
    year -- the year (int)
    month -- the month (int)
    day -- the day (int)

    Return:
    An integer coresponding to the day of the week,
    where Sunday=0, Monday=1 ... (int)

    >>> calculate_day(1,1,2014)
    3

    >>> calculate_day (3,3,2014)
    1

    >>> calculate_day (3,4,2014)
    4

"""
    a = (14-month)//12
    y = year - a
    m = month + 12 * a - 2
    d = (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12)% 7

    return d
import doctest
doctest.testmod ()

def day_of_week (day, month, year):
    """
    Returns the name of the day coresponding to a given date.

    Arguements:
    year -- the year (int)
    month -- the month (int)
    day -- the day (int)

    Returns:
    Name of the coresponding day -- A string coresponding to the day of the week (string)

    >>> day_of_week (3,3,2014)
    'Monday'

    >>> day_of_week (1,1,2014)
    'Wednesday'

    >>> day_of_week (3,4,2014)
    'Thursday'

    """
    day_number=calculate_day(day,month,year)
   
    
    if day_number == 0:
        name='Sunday'
    elif day_number == 1:
        name='Monday'
    elif day_number == 2:
        name= 'Tuesday'
    elif day_number == 3:
        name= 'Wednesday'
    elif day_number == 4:
        name= 'Thursday'
    elif day_number == 5:
        name= 'Friday'
    elif day_number == 6:
        name= 'Saturday'
    else:
        name= 'error. That is not a day of the week'

    
    return (name)

import doctest
doctest.testmod ()




