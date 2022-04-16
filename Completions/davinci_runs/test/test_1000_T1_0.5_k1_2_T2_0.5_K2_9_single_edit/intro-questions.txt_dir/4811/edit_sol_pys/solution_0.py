N = int(input())
if N == 1:
    print(1, 0)
else:
    min_size = 1
    min_breaks = 0
    while min_size < N:
        min_size *= 2
        min_breaks += 1


    print(min_size, min_breaks)
