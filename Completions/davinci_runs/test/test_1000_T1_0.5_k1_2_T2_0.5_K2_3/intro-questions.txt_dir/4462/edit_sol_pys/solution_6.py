
# My answer
'''
N = int(input())
a = list(map(int, input().split()))

if a[0] % 2 == 0:
    print("Yes")
    exit()

for i in range(N-1):
    if a[i] % 2 != 0:
        if a[i+1] % 2 != 0:
            print("No")
            exit()

if a[N-1] % 2 != 0:
    print("No")
    exit()

print("Yes")
'''

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
