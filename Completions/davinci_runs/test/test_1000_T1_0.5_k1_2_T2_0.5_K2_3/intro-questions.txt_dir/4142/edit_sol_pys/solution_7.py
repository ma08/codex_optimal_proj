

s = list(input())

n = len(s)

even = [s[i] for i in range(n) if i % 2 == 0]
odd = [s[i] for i in range(n) if i % 2 == 1]

if all(x in 'RUD' for x in odd) and all(x in 'LUD' for x in even):
    print("Yes")
else:
    print("No")
