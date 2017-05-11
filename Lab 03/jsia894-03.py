"""
Name: Juan Nicolas Sevilla Siasoco
UPI: jsia894
ID: 8104859

"""

import math

#exercise 3.6
def cone_volume (bottom_radius, top_radius, height):
    """ Calculates the volume of a truncated cone.

    Arguement:
    r1 -- the radius of the bottom circle (float)
    r2 -- the radius of the top circle (float)
    height -- the height in between the top and the bottom circle (float)

    Return:
    volume (float)

    Tests:
    >>> cone_volume(2,3,10)
    198.97

    >>> cone_volume(50,20,60)
    245044.23

    >>> cone_volume (80,10,20)
    152890.84


    """

    volume= (math.pi)/3 * height * (bottom_radius**2 + ((bottom_radius)*(top_radius)) + top_radius**2)
    return round(volume,2)

import doctest
doctest.testmod()
 

#exercise 3.7
def number_of_cups (bottom_radius, top_radius, height, liters_of_liquid):
    """Calculates the number of cups filled by liquid (liters).

    Arguement:
    bottom radius -- the radius of the bottom of the cup (float)
    top radius -- the radius of the top of the cup (float)
    height -- the height of the cup (float)
    liters of liquid -- the total amount of liquid in liters in all of the cups (int)

    Return:
    number of cups (int)

    Tests:
    
    >>> number_of_cups (2, 3, 10, 20)
    100

    >>> number_of_cups (3, 4, 5, 30)
    154
 
    >>> number_of_cups (4, 2, 15, 60)
    136
    
    """

    number_of_cups= math.floor(liters_of_liquid/((math.pi)/3 * height * (bottom_radius**2 + ((bottom_radius)*(top_radius)) + top_radius**2)/1000))
    return (number_of_cups)

import doctest
doctest.testmod ()
