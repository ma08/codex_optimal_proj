
# Solution

n, k = map(int, input().split())  # input
a = list(map(int, input().split()))  # input

if k == 1:
    print(max(a))  # output
else:
    print(max(a) - min(a) + 1)  # output
