from ImageLibrary import *

def negative(pixel):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    new_r=255-r
    new_g=255-g
    new_b=255-b
    color=makeColor(new_r, new_g, new_b)
    setColor(pixel,color)


pict = makePicture("caterpillarSmall.jpg")
for pixel in getPixels(pict):
    negative(pixel)
show(pict)



