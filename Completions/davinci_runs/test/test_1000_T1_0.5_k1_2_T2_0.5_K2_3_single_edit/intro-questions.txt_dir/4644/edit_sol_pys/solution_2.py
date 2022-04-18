
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))  # taking input and converting to list
    if sum(a) % 2 == 0:  # checking if sum is even
        print("NO")
    else:
        print("YES")
