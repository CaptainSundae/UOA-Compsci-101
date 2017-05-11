"""
UPI: jsia894
ID: 8104859
Name: Juan Nicolas Sevilla Siasoco
"""

#ex8.4
def which_animal(boolean_list):
    """
    Determines the class of an animal based off a list of booleans

    Arguement:
    boolean_list -- a list of booleans

    Return:
    type -- animal type


    Test Cases:
    >>> which_animal([True,True,True,True,True,True,True])
    'Mammal'

    >>> which_animal([False,False,False, False, False, False, False])
    'Arachnid'

    >>> which_animal([True,False,False,False,False,False,False])
    'Reptile'
    """

    for i in range (0, len(boolean_list)-1,1):
        if boolean_list[i] == True:
            if boolean_list[i+3]==True:
                return("Mammal")
            elif boolean_list[i+4] == True:
                return ("Bird")
            elif boolean_list[i+5] == True:
                return ("Fish")
            elif boolean_list[i+6] == True:
                return("Amphibian")
            else:
                return ("Reptile")

        else:
            if boolean_list[i+1] == True:
                return ("Mollusc")
            if boolean_list [i+2] == True:
                return ("Insect")
            else:
                return ("Arachnid")



#8.5
def movie_price(day_of_week,hour):
    """
    Gives the price of a movie ticket during a given day and time.

    Arguement:
    day_of_week -- the day of the week (string)
    hour -- time given on a 24 hour clock (integer)

    Return:
    price -- the price of the movie ticket (float)

    Tests:
    >>> movie_price('Tuesday',4)
    10.75

    >>> movie_price('Saturday',15)
    15.75

    >>> movie_price('Friday',17)
    15.75
    """
    
    if day_of_week == 'Tuesday':
        return 10.75

    elif day_of_week == 'Wednesday':
        return 5.75

    elif day_of_week=='Saturday' or day_of_week=='Sunday':
        return 15.75

    elif day_of_week=='Monday' or day_of_week=='Thursday'or day_of_week=='Friday' :
        if hour in range(0,17):
            return 12.75
        elif hour in range(17,24):
            return 15.75


import doctest
doctest.testmod()
