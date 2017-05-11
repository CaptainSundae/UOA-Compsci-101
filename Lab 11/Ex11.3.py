from ImageLibrary import *

def to_grayscale(pixel):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    grey=0.299*r+0.587*g+0.114*b
    red=grey
    green=grey
    blue=grey
    color=makeColor(red,green,blue)
    setColor(pixel,color)



pict = makePicture("caterpillarSmall.jpg")
for pixel in getPixels(pict):
    to_grayscale(pixel)
show(pict)



