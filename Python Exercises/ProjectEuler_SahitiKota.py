# Sahiti Kota
# 08/31/2021
import math 

# Problem 1
sum1 = 0
for i in range(1000):
    if (i % 3) == 0 or (i % 5) == 0:
        sum1 += i
print("#1: ", sum1)

# Problem 2
sum2 = 0
def fibonacci(a):
    if a == 0 or a == 1:
        return 1
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

term = 0
while fibonacci(term) < 4000000:
    if fibonacci(term) % 2 == 0:
        sum2 += fibonacci(term)

    term += 1

print("#2: ",sum2)

# Problem 3
def largestPrimeFactor(x):
    while x % 2 == 0:
        largestPrime = 2
        x = x/ 2
    for i in range (3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            largestPrime = i
            x = x/ i
    return largestPrime

print("#3: ", largestPrimeFactor(600851475143))

# Problem 4
largestPalindrome = -1
for i in range (100,1000):
    for j in range (100, 1000):
        currentProduct = i * j
        if str(currentProduct) == str(currentProduct)[::-1] and currentProduct > largestPalindrome:
            largestPalindrome = currentProduct
print("#4: ",largestPalindrome)

# Problem 5
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

i = lcm(1, 2)
for n in range (3, 21):
    i = lcm(i, n)
print("#5: ",i)

# Problem 6
sqsum = 0
sumsq = 0
for i in range (1, 101):
    sqsum += i ** 2
    sumsq += i
sumsq = sumsq ** 2
print("#6: ", (sumsq - sqsum))

# Problem 7
def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primesNum = 0
prime = 1
while primesNum < 10001:
        prime += 1
        if isPrime(prime):
            primesNum += 1

print("#7: ",prime)

# Problem 8
num = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
i = 0
largestProduct = 0
while (i + 13) < len(num):
    firstNum = int(num[i])
    secondNum = int(num[i + 1])
    thirdNum = int(num[i + 2])
    fourthNum = int(num[i + 3])
    fifthNum = int(num[i + 4])
    sixthNum = int(num[i + 5])
    seventhNum = int(num[i + 6])
    eighthNum = int(num[i + 7])
    ninthNum = int(num[i + 8])
    tenthNum = int(num[i + 9])
    eleventhNum = int(num[i + 10])
    twelfthNum = int(num[i + 11])
    thirteenthNum = int(num[i + 12])
    if (firstNum * secondNum * thirdNum * fourthNum * fifthNum * sixthNum * seventhNum * eighthNum * ninthNum * tenthNum *  eleventhNum * twelfthNum * thirteenthNum) > largestProduct:
        largestProduct = (firstNum * secondNum * thirdNum * fourthNum * fifthNum * sixthNum * seventhNum * eighthNum * ninthNum * tenthNum *  eleventhNum * twelfthNum * thirteenthNum)
    i += 1

print("#8: ",largestProduct)

# Problem 9
for a in range(1, 333):
    for b in range(a, 500):
        for c in range(b, 1000):
            if a < b < c and a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print("#9: ", a * b * c)

# Problem 29
powersList = []
for a in range (2, 101):
    for b in range(2, 101):
        powersList.append(a ** b)
powersSet = set(powersList)
print("#29: ", len(powersSet))
