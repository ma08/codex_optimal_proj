
n = int(input())  # number of elements
p = [int(x) for x in input().split()]  # elements

count = 0  # count of peaks
for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1

print(count)
