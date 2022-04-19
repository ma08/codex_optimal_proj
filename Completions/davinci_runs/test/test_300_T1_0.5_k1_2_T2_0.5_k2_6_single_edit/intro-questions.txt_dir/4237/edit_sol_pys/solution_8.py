

a = input()
b = input()
c = input()
d = input()

count = 0

for i in range(a, b+1):
    if i % c != 0 and i % d != 0:
        count += 1

print(count)
