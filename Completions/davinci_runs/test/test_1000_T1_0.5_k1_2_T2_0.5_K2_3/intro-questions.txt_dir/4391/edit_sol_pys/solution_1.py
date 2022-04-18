
n = int(input())

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a_odd = 0
b_odd = 0

for i in a:
    if i%2 != 0:
        a_odd += 1

for i in b:
    if i%2 != 0:
        b_odd += 1

print(min(a_odd, n-b_odd) + min(n-a_odd, b_odd))
