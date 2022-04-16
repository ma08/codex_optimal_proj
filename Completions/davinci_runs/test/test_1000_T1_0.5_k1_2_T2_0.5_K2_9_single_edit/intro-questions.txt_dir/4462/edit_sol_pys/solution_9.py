
# My answer (Time-over)
N = int(input())  # input N
a = list(map(int, input().split()))  # input N numbers

# if N is even
if N % 2 == 0:
    for i in range(N):
        if a[i] % 2 == 0:
            continue
        else:
            print("No")
            exit()
    print("Yes")

# if N is odd
else:
    for i in range(N):
        if a[i] % 2 == 0:
            continue
        elif a[i] % 4 == 0:
            continue
        else:
            print("No")
            exit()
    print("Yes")

# Other's answer (AC)
N, *a = map(int, open(0).read().split())

if N % 2 == 1 and all(x % 2 == 0 for x in a):
    print("Yes")
elif N % 2 == 0 and all(x % 2 == 0 for x in a):
    print("Yes")
elif N % 2 == 0 and all(x % 2 == 1 for x in a):
    print("Yes")
else:
    print("No")

print("Yes")
