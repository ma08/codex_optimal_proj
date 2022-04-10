

n = int(input())
heights = list(map(int, input().split()))

if n == 1:
    print("YES")
else:
    # Find the max height
    max_h = 0
    for i in range(1, n):
        if heights[i] > max_h:
            max_h = heights[i]

    # All heights must be equal to the max height
    for i in range(1, n):
        if heights[i] != max_h:
            print("NO")
            break
    else:
        print("YES")