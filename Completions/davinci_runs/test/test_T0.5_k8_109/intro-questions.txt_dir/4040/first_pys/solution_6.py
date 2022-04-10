

# cook your dish here
n,m,d = map(int,input().split())
c = list(map(int,input().split()))

# print(n,m,d)
# print(c)

# check if the sum of c is less than n
if sum(c) > n:
    print("NO")
    exit()

# check if d is less than n
if d > n:
    print("YES")
    print("0 "*n)
    exit()

# check if d is less than or equal to n-m
if d <= n-m:
    print("YES")
    print("0 "*d+"1 "*c[0]+"0 "*(n-d-c[0]))
    exit()

# check if d is more than n-m
if d > n-m:
    print("NO")
    exit()