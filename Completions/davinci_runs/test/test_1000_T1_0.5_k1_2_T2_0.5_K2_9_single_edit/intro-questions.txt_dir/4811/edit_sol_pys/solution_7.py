
N = int(input())

min_size = 1
min_breaks = 0
while min_size < N:
    min_size *= 2
    min_breaks += 1

print(min_size, min_breaks)
