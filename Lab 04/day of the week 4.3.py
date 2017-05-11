def day_name (number_representing_the_day):
    """Changes the number of the day of the week into the name of the day

    Arguement:
    a number representing the day -- the number of the day of the week (int)

    Return:
    name of the day -- the name of the day of the week

    Tests:

    >>> day_name (0)
    'Sunday'

    >>> day_name (4)
    'Thursday'
    
    """
    if number_representing_the_day == 0:
        name='Sunday'
    elif number_representing_the_day == 1:
        name='Monday'
    elif number_representing_the_day == 2:
        name= 'Tuesday'
    elif number_representing_the_day == 3:
        name= 'Wednesday'
    elif number_representing_the_day == 4:
        name= 'Thursday'
    elif number_representing_the_day == 5:
        name= 'Friday'
    elif number_representing_the_day == 6:
        name= 'Saturday'
    else:
        name= 'error. That is not a day of the week'
    return name
import doctest
doctest.testmod ()
