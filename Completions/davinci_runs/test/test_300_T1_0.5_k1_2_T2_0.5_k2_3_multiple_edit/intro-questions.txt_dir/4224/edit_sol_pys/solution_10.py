n = int(input())
numbers = [int(x) for x in input().split()]
count = 0
for number in numbers:
    while number % 2 == 0:
        number //= 2
        count += 1

print(count)
