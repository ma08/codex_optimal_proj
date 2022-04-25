
N = int(input())
a = [int(x) for x in input().split()]

count = 0

for num in a:
    while num % 2 == 0:
        num /= 2
        count += 1

print(count)
