

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input()) #input the data
a = list(map(int,input().split())) #input the elements of the array

g = a[0]
for i in range(1,n):
    g = gcd(g,a[i])

print(g)
