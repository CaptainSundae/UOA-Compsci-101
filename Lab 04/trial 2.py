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
    4

"""
    a = (14-month)//12
    y = year - a
    m = month + 12 * a - 2
    d = (day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12)% 7

    return d
import doctest
doctest.testmod ()
