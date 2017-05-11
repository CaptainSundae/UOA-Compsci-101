def calculate_day (day, month, year):
    """ Calculate the day of the week for a given date

    Arguement:
    year -- the year (int)
    month -- the month (int)
    day -- the day (int)

    Return:
    An integer coresponding to the day of the week,
    where Sunday=0, Monday=1 ...

    >>> calculate_day(1,1,2014)
    3

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
    Name of the coresponding day -- A string coresponding to the day of the week

    >>> day_of_week (3,3,2014)
    'Monday'

    >>> day_of_week (1,1,2014)
    'Wednesday'

    """
  
   
    
    if calculate_day(day,month,year) == 0:
        name='Sunday'
    elif calculate_day(day,month,year) == 1:
        name='Monday'
    elif calculate_day == 2:
        name= 'Tuesday'
    elif calculate_day == 3:
        name= 'Wednesday'
    elif calculate_day == 4:
        name= 'Thursday'
    elif calculate_day == 5:
        name= 'Friday'
    elif calculate_day == 6:
        name= 'Saturday'
    else:
        name= 'error. That is not a day of the week'

    
    return (name)

import doctest
doctest.testmod ()
