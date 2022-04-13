
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
alice = 0
bob = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        alice += a[-i]
    elif i % 2 == 0:
        bob += a[-i]
print(alice, bob)
