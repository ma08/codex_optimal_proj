
n = int(input()) # input number
p = list(map(int, input().split())) # input list of numbers

count = 0 # count variable
for i in range(1, n - 1):
    if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
        count += 1
print(count)
