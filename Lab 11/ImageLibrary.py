import tkinter as tk
from tkinter.filedialog import askopenfilename
import pygame
import copy
import math
import sys

# Suppress root window that is shown on askopenfiledialog()
root = tk.Tk()
root.withdraw()


def pickAFile():
        return askopenfilename()


#----------------- Color ------------------------------------------

class Color:
	def __init__(self, r, g, b):
		self.r, self.g, self.b = 0, 0, 0
		self.setR(r)
		self.setG(g)
		self.setB(b)

	def __repr__(self):
		return 'color r=' + str(self.r) + ' g=' + str(self.g) + ' b=' + str(self.b)

	def setR(self, value):
		self.r = self.wrapValue(value)
		return

	def setG(self, value):
		self.g = self.wrapValue(value)
		return

	def setB(self, value):
		self.b = self.wrapValue(value)
		return

	# Wrap value (for example, 256 == 0). Text book specifies this functionality
	def wrapValue(self, value):
		return value % 256

	# Shallow copy
	def clone(self):
		return Color(self.r,self.g,self.b)

def makeColor(r, g, b):
        return Color(r,g,b)

def distance(color1, color2):
        (diffR, diffG, diffB) = (color1.r-color2.r,color1.g-color2.g,color1.b-color2.b)
        return math.sqrt(diffR**2+diffG**2+diffB**2)

def makeLighter(color):
        amount = 40
        (color.r, color.g, color.b)= (add(color.r,amount),add(color.g,amount),add(color.b,amount))
        return

def makeDarker(color):
        amount = 40
        (color.r, color.g, color.b)= (sub(color.r,amount),sub(color.g,amount),sub(color.b,amount))
        return

# Subtracts a from b with min result 0.
def sub(a,b):
        result = a - b
        if (result < 0):
                result = 0
        return result

# Adds a and b together with max result 255.
def add(a,b):
        result = a + b
        if (result > 255):
                result = 255
        return result




#------------------ Built-in colors ------------------------------------

white = Color(255,255,255)
black = Color(0,0,0)
red = Color(255,0,0)
green = Color(0,255,0)
blue = Color(0,0,255)
grey = Color(190,190,190)
lightGrey = Color(225,225,225)
darkGrey = Color(120,120,120)
yellow = Color(255,255,0)
orange = Color(255,165,120)
pink = Color(255,192,203)
magenta = Color(255,0,255)
cyan = Color(0,255,255)



#-------------------- Extra color functions ----------------------------


# Very roughly converts a color to a near(ish) primary color
def makePrimary(col):
        if col.r>200 and col.g<200 and col.b<200:
                col=red
        elif col.g>200 and col.b<200 and col.r<200:
                col=green
        elif col.b>200 and col.g<200 and col.r<200:
                col=blue
        elif col.b>200 and col.r>200 and col.g>200:
                col=white
        elif col.b<100 and col.r<100 and col.g<100:
                col=black
        elif col.b>200 and col.r>200 and col.g<200:
                col=magenta
        elif col.r>200 and col.g>200:
                col=yellow
        elif 80<col.r<120 and 80<col.g<120 and 80<col.b<120:
                col=cyan
        else :
                col=grey
        return col.clone()

#make a lego-esque block size * size pixels of the color of the centre pixel,p,
#converted to a primary-ish color

def makeBlock(pict,p,size):
        col=getColor(p)
        col=makePrimary(col)
        i=getX(p)
        j=getY(p)
        if (i<=getWidth(pict)-size/2-1) and (j<=getHeight(pict)-size/2-1):
                for a in range(i-size/2,i+size/2+1):
                        for b in range(j-size/2,j+size/2+1):
                                setColor(getPixel(pict,a,b),col)
        return


#return a brightness value between 0 and 255 for a color
def brightness(color):
        bright=0.299*color.r + 0.587*color.g + 0.114*color.b
        return bright


#------------------ Pixel ----------------------------------------------

class Pixel:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def __repr__(self):
		return 'Pixel, color=' + str(getColor(self))

def getX(pixel):
        return pixel.x

def getY(pixel):
        return pixel.y

def getColor(pixel):
        return pixel.color.clone()

def setColor(pixel, color):
        pixel.color = color.clone()
        return

def getRed(pixel):
        return pixel.color.r

def setRed(pixel, r):
        pixel.color.setR(r)
        return

def getGreen(pixel):
        return pixel.color.g

def setGreen(pixel, g):
        pixel.color.setG(g)
        return

def getBlue(pixel):
        return pixel.color.b

def setBlue(pixel, b):
        pixel.color.setB(b)
        return

#-------------------- Picture ------------------------------------------

class Picture:
	def __init__(self, filename, image):
		self.image = image
		self.filename = filename
		self.pixels = self.getPixelsFromImage()

	def __repr__(self):
		return 'Picture, filename ' + self.filename + ', height ' + str(self.getHeight()) + ', width ' + str(self.getWidth())

	def getWidth(self):
		return self.image.get_width()

	def getHeight(self):
		return self.image.get_height()

	def getImage(self):
		self.writePixelsToImage()
		return self.image

	def setImage(self,image):
		self.image = image
		self.pixels = self.getPixelsFromImage()

        # Read 2D image into 1D array of pixels (row by row)
	def getPixelsFromImage(self):
		pixels = []
		for y in range(self.getHeight()):
			for x in range(self.getWidth()):
				(r,g,b,a) = self.image.get_at((x,y))
				pixels.append(Pixel(x,y,Color(r,g,b)))
		return pixels

        # Write 1D array of pixels to 2D image
	def writePixelsToImage(self):
		pixels = self.pixels
		for pix in pixels:
			(r,g,b) = (pix.color.r, pix.color.g, pix.color.b)
			self.image.set_at((pix.x, pix.y),(r,g,b))
		return

def getWidth(picture):
        return picture.getWidth()

def getHeight(picture):
        return picture.getHeight()

def getPixels(picture):
        return picture.pixels

def getPixel(picture,x,y):
        return picture.pixels[y*picture.getWidth()+x]

# Displays the given picture
def show(picture):
        # Close existing display window
        pygame.display.quit()

        # Create new display window of the appropriate dimensions
        resolution = (picture.getWidth(), picture.getHeight())
        screen = pygame.display.set_mode(resolution)

        # Display image on window
        screen.blit(picture.getImage(), (0,0))
        pygame.display.flip()
        return

# Creates picture from file and returns
def makePicture(filename):
        image = pygame.image.load(filename)
        image = image.convert()
        return Picture(filename, image) # Create and return picture object


# Returns empty picture of given height and width. Empty picture is white.
def makeEmptyPicture(height,width):
        # Create an empty picture using a blank surface object
        image = pygame.Surface((width,height)).convert()
        picture = Picture("Undefined",image)
        # Set all pixels from the default black to white
        for p in getPixels(picture):
                setColor(p,white)
        return picture


# Save the picture to the given filename
def writePictureTo(picture, filename):
        pygame.image.save(picture.getImage(), filename)
        return

# Opens a file dialog and saves the picture to the selected file
def writePictureToSelect(picture):
        pygame.image.save(picture.getImage(), pickAFile())
        return


# Need to have a window open to run the convert
# function in makePicture() and makeEmptyPicture()
screen = pygame.display.set_mode((200, 200))
