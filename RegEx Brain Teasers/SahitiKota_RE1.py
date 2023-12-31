import sys; args = sys.argv[1:]
idx = int(args[0])-30

myRegexLst = [
  r"/^0$|^10[10]$/",
  r"/^[01]*$/",
  r"/0$/",
  r"/\b\w*[aeiou]\w*[aeiou]\w*\b/i",
  r"/^[1]+[01]*0$|^0$/",
  r"/^[01]*110[01]*$/",
  r"/^.{2,4}$/s",
  r"/^\d{3}[ ]*-?[ ]*\d\d[ ]*-?[ ]*\d{4}$/",
  r"/^[a-ce-z ]*d[a-z]*/im",
  r"/^1*$|^0*$|^0[01]*0$|^1[01]*1$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Sahiti Kota, period 8, 2023