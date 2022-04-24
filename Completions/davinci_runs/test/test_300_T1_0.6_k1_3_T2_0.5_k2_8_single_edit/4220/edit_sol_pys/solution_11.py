
k = int(input()) 
s = str(input()) 

print(s[0:k] + "..." if len(s) > k else s)
