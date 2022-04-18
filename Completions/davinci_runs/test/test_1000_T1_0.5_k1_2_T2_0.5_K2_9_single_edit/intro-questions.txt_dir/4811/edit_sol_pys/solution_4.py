

N = int(input())

size = 1
breaks = 0
while size < N:
    size *= 2
    breaks += 1

print(size, breaks)
