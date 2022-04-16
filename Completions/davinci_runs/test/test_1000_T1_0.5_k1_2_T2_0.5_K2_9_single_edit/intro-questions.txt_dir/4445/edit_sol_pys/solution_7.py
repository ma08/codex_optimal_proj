
n = int(input())
a = list(map(int, input().split()))

# find the odd number of odd numbers
odd = 0
for i in a:
    if i % 2 == 1:
        odd += 1

for i in range(len(a)):
    if a[i] % 2 == odd % 2:
        print(sum(a) - a[i])
        exit()
