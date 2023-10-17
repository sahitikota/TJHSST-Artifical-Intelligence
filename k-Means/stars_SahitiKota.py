# Sahiti Kota
# 03/28/2022
import csv
from math import log
import random

rowCount = 0
dataDict = {}
with open('star_data.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    for row in csvReader:
        if rowCount == 0:
            rowCount += 1
        else:
            dataDict[tuple([log(int(row[0])), log(float(row[1])), log(float(row[2])), float(row[3])])] = row[4]
k = 5
means = random.sample(dataDict.keys(), k) 
meansStars = [[] for i in range(k)]
for star in dataDict.keys():
    smallest = 1000000000000
    meanSmall = -1
    mC = 0
    for mean in means:
        se = 0
        for value in range(len(star)):
            se += (star[value] - mean[value]) ** 2
        if se < smallest:
            smallest = se
            meanSmall = mC
        mC += 1
    meansStars[meanSmall].append(star)
while 1 != 0:
    newMeans = []
    for group in meansStars:
        temp = 0
        lum = 0
        rad = 0
        mag = 0
        for values in group:
            temp += values[0]
            lum += values[1]
            rad += values[2]
            mag += values[3]
        temp = temp/len(group)
        lum = lum/len(group)
        rad = rad/len(group)
        mag = mag/len(group)
        newMeans.append((temp, lum, rad, mag))
    if means == newMeans:
        break
    means = newMeans
    meansStars = [[] for i in range(k)]
    for star in dataDict.keys():
        smallest = 1000000000000
        meanSmall = -1
        mC = 0
        for mean in means:
            se = 0
            for value in range(len(star)):
                se += (star[value] - mean[value]) ** 2
            if se < smallest:
                smallest = se
                meanSmall = mC
            mC += 1
        meansStars[meanSmall].append(star)

for x in range(len(meansStars)):
    print("MEAN:", means[x])
    for star in meansStars[x]:
        print(star, "type:", dataDict[star])
