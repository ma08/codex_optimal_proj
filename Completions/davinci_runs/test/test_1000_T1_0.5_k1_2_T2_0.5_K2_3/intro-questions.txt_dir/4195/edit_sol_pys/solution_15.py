
n, k = map(int, input().split())

if n % (k + 1) == 0:
    print("Drew")
elif n % (k + 1) == 1:
    print("Won")
else: 
    print("Lost")
