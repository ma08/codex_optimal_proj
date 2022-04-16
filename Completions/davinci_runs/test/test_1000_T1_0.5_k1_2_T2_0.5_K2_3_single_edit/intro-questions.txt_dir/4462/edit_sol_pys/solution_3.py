# My answer
"""
N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    if a[i] % 4 == 0:
        continue
    elif a[i] % 2 == 0:
        continue
    else:
        print("No")
        exit()

print("Yes")
"""

# Other's answer
N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    if a[i] % 2 == 0:
        continue
    elif a[i] % 4 == 0:
        continue
    else:
        print("No")
        exit()

print("Yes")
