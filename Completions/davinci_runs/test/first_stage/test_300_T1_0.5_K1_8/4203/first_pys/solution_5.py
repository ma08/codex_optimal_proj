

s = input()

if s[0] == 'A' and s[2:len(s)-1].count('C') == 1:
  for i in range(1,len(s)):
    if s[i] == 'C':
      continue
    if s[i].islower():
      continue
    else:
      print("WA")
      exit()
  print("AC")
else:
  print("WA")