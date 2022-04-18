a,b=input().split()
for i in range(len(a)):
 if a[i] in b:
  j=0
  while j<len(b):
   if a[i]==b[j]:
    break
   j+=1
  break
for i in range(len(a)):
 if a[i] in b:
  print("."*j+a[i]+"."*(len(b)-j-1))
 else:
  print("."*len(b))
