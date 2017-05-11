"""
UPI: jsia894
Name: Juan Nicolas Sevilla Siasoco
ID: 8104859
"""
from ImageLibrary import *

#11.4
def create_marks_dict(list_of_strings):
    """
    Argument:

    list_of_string -- a list of strings (str)

    Return:
    student_dict -- a dictionary of (mark, [list of students who got that mark])
    """
    
    student_dict={}
    for marks in list_of_strings:
        (student_name,mark)=marks.split(",")
        if mark in student_dict:
            student_dict[mark]=student_dict[mark]+[student_name]
        else:
            student_dict[mark]=[student_name]
    return student_dict

#11.5
def count_rgb_frequency(filename): 
    """
    Argument:
    filename -- an image filename

    Return:
    rgb_frequency -- A dictionary of pixel colours and frequencies
    """
    pict = makePicture(filename)
    rgb_frequency = {}
    for pixel in getPixels(pict):
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)
        color = (r, g, b)
        if color not in rgb_frequency:
            rgb_frequency[color] = 1
        else:
            rgb_frequency[color] += 1
    return(rgb_frequency)
