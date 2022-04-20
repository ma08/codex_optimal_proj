
# Python3 program to find GCD of two numbers

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input("Enter the number of elements in the list: "))
a = list(map(int, input("Enter the elements of the list: ").split()))

g = a[0]
for i in range(1,n):
    g = gcd(g,a[i])

print(g)
