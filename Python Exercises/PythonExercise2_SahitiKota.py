# Sahiti Kota
# 08/28/2021
import sys

s = sys.argv[1]
print("#1: " + s[2])
print("#2: " + s[4])
print("#3: " + str(len(s)))
print("#4: " + s[0])
print("#5: " + str([len(s) - 1]))
print("#6: " + s[len(s) - 2])
print("#7: " + s[3:8])
print("#8: " + s[-5:])
print("#9: " + s[2:])
print("#10: " + s[::2])
print("#11: " + s[1::3])
print("#12: " + s[::-1])
print("#13: " + str(s.find(" ")))
print("#14: " + s[:len(s) - 1])
print("#15: " + s[1:])
print("#16: " + s.lower())
print("#17: " + str(s.split("  ")))
print("#18: " + str(len(s.split("  "))))
print("#19: " + str(list(s)))
print("#20: " + "".join(sorted(list(s))))
print("#21: " + s[0:s.find(" ")])
print("#22: " + str(s == s[::-1])) 