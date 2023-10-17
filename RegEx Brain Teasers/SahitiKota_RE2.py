import sys; args = sys.argv[1:]
idx = int(args[0]) - 40

myRegexLst = [
  r"/^[x.o]{64}$/i",
  r"/^[xo]*\.[xo]*$/i"
  r"/^(\..*|.*\.|x+o*\..*|.*\.o+x+)$/i",
  r"/^.(..)*$/s",
  r"/^(0([01]{2})*|1([01]{2})*[01])$/",
  r"/\w*(a[eiou]|e[aiou]|i[eaou]|o[eiau]|u[eioa])\w*/i",
  r"/^(0*|1*|(0|10)*1*)$/",
  r"/^\b[bc]*a?[bc]*\b$/",
  r"/^\b[bc]*((a[bc]*){2})*\b$/",
  r"/^\b(2[02]*)*((1[02]*){2})*\b$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Sahiti Kota, period 8, 2023