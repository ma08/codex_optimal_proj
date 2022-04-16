n=input("Enter string:")
k=0
for i in range(len(n)):
  if(n[i].isdigit()):
    k=k+1
print(k)
