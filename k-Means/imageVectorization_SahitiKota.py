# Sahiti Kota
# 03/29/2022
import ssl
import random 
import sys
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
import io
from PIL import Image
URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
f = io.BytesIO(urllib.request.urlopen(URL).read()) # Download the picture at the url as a file object
img = Image.open(f) # You can also use this on a local file; just put the local filename in quotes in place of f.
'''img.show() # Send the image to your OS to be displayed as a temporary file
print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame'''
pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
'''print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].
pix[2,5] = (255, 255, 255) # Set the pixel to white. Note this is called on “pix”, but it modifies “img”.
img.show() # Now, you should see a single white pixel near the upper left corner
img.save("my_image.png") # Save the resulting image. Alter your filename as necessary.'''

# naive 8 color quanitization
'''for x in range(img.size[0]):
    for y in range(img.size[1]):
        red, green, blue = pix[x, y]
        if red < 128:
            red = 0
        if red > 128:
            red = 255
        if green < 128:
            green = 0
        if green > 128:
            green = 255
        if blue < 128:
            blue = 0
        if blue > 128:
            blue = 255
        pix[x, y] = (red, green, blue)
img.show()
img.save("sfranceNaive8.png")'''

# naive 27 color quanitization
'''for x in range(img.size[0]):
    for y in range(img.size[1]):
        red, green, blue = pix[x, y]
        if red < 255 // 3:
            red = 0
        elif red > 255 * 2 // 3:
            red = 255
        elif red < 255 * 2 // 3 and red > 255 // 3:
            red = 127
        if green < 255 // 3:
            green = 0
        elif green > 255 * 2 // 3:
            green = 255
        elif green < 255 * 2 // 3 and red > 255 // 3:
            green = 127
        if blue < 255 // 3:
            blue = 0
        elif blue > 255 * 2 // 3:
            blue = 255
        elif blue < 255 * 2 // 3 and red > 255 // 3:
            blue = 127
        pix[x, y] = (red, green, blue)
img.show()
img.save("sfranceNaive27.png")'''

# k-means 
'''k = int(sys.argv[2])
dataDict = {}
locations = {}
for x in range(img.size[0]):
    for y in range(img.size[1]):
        dataDict[tuple(pix[x, y])] = (x, y)
        if tuple(pix[x, y]) not in locations.keys():
            locations[tuple(pix[x, y])] = [(x, y)]
        else:
            locations[tuple(pix[x, y])].append((x, y))
# dictionary - (RGB, location)
means = random.sample(dataDict.keys(), k) 
meansPixels = [[] for i in range(k)]
for pixel in dataDict.keys():
    smallest = 1000000000000
    meanSmall = -1
    meanCount = 0
    for mean in means:
        se = 0
        for value in range(len(pixel)):
            se += (pixel[value] - mean[value]) ** 2
        if se < smallest:
            smallest = se
            meanSmall = meanCount
        meanCount += 1
    meansPixels[meanSmall].append(pixel)
x = 0
while 1 != 0:
    newMeans = []
    for group in meansPixels:
        red = 0
        green = 0
        blue = 0
        for values in group:
            red += values[0]
            green += values[1]
            blue += values[2]
        red = red/len(group)
        green = green/len(group)
        blue = blue/len(group)
        newMeans.append((red, green, blue))
    if means == newMeans:
        roundedMeans = []
        for mean in newMeans:
            newList = []
            for value in mean:
                newList.append(round(value))
            roundedMeans.append(tuple(newList))
        break
    means = newMeans
    meansPixels = [[] for i in range(k)]
    meansLocations = [[] for i in range(k)]
    for pixel in dataDict.keys():
        smallest = 1000000000000
        meanSmall = -1
        mC = 0
        for mean in means:
            se = 0
            for value in range(len(pixel)):
                se += (pixel[value] - mean[value]) ** 2
            if se < smallest:
                smallest = se
                meanSmall = mC
            mC += 1
        meansPixels[meanSmall].append(pixel)
        meansLocations[meanSmall].extend(locations[pixel])

print(roundedMeans)
for x in range(len(roundedMeans)):
    for location in meansLocations[x]:
        pix[location] = roundedMeans[x]
img.save("kmeansout.png")'''

#k-means++
