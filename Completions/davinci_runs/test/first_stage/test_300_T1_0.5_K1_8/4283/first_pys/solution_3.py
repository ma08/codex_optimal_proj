

n = int(input())
a = list(map(int, input().split()))

a.sort()

max_size = 0

for i in range(n-1):
    if a[i+1] - a[i] > 5:
        continue
    else:
        curr_size = 2
        for j in range(i+1, n-1):
            if a[j+1] - a[j] > 5:
                break
            else:
                curr_size += 1
        if curr_size > max_size:
            max_size = curr_size

print(max_size)