import sys; args = sys.argv[1:]
idx = int(args[0]) - 50

myRegexLst = [
  r"/(\w)+\w*\1\w*/i",
  r"/(\w)+(\w*\1){3}\w*/i",
  r"/^(0[01]*0|1[01]*1|0|1)$/",
  r"/(?=\w*cat)\b\w{6}\b/i",
  r"/(?=\w*bri)(?=\w*ing)\b\w{5,9}\b/i",
  r"/(?!\w*cat)\b\w{6}\b/i",
  r"/(?!\w*(\w)\w*\1)\b\w+\b/i",
  r"/^(?![01]*10011)[01]*$/",
  r"/\w*([aeiou])(?!\1)[aeiou]\w*/i",
  r"/^(?![01]*(1[01]1))[01]*$/",]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Sahiti Kota, period 8, 2023