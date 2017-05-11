"""
UPI: jsia894
ID: 8104859
Create a function that calculates the volume of a truncated cone.
"""

import math

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
 
    
