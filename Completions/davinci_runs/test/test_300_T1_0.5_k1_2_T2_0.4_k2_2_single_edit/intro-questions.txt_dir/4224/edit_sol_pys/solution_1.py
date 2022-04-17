
N = int(input())
a = [int(x) for x in input().split()]  # list comprehension

count = 0

for i in a:
    while i % 2 == 0:  # while loop
        i /= 2
        count += 1

print(count)
