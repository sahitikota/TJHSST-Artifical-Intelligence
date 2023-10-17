# Sahiti Kota
# 08/26/2021
import sys
import math 

sum = 0

if sys.argv[1] == "A":
    for i in range (2, 5):
        sum += int(sys.argv[i])
        print(sum)
elif sys.argv[1] == "B":
    for i in range (2, len(sys.argv)):
        sum += int(sys.argv[i])
        print(sum)
elif sys.argv[1] == "C":
    for i in range (2, len(sys.argv)):
        if int(sys.argv[i]) % 3 == 0:
            sum += int(sys.argv[i])
            print(sum)
elif sys.argv[1] == "D":
    nTerms = int(sys.argv[2])
    n1 = 0
    n2 = 1
    for i in range (nTerms - 2):
        print (n1)
        print (n2)
        n1 = n1 + n2
        n2 = n1 + n2
elif sys.argv[1] == "E":
    for i in range (int(sys.argv[2]), int (sys.argv[3]) + 1):
        print ((i ** 2) - (3 * i) + 2)
elif sys.argv[1] == "F": 
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    c = float(sys.argv[4])
    p = (a + b + c) / 2
    if a + b > c and a + c > b and b + c > a:
        print (math.sqrt(p * (p - a) * (p - b) * (p - c)))
    else:
        print ("Error: Side lengths do not make a valid triangle.")
elif sys.argv[1] == "G":
    word = str(sys.argv[2])
    count = 0
    for i in word:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U") :
            count += 1
    print (count)