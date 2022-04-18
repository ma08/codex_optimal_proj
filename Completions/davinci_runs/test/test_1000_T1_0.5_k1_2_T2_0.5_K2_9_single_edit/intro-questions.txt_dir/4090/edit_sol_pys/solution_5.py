

def largest_rectangle(n, heights):
    max_area = 0
    for i in range(n):
        min_height = heights[i]
        for j in range(i, n):
            min_height = min(min_height, heights[j])
            max_area = max(max_area, (j - i + 1) * min_height)
    return max_area

n = int(input())
heights = [int(x) for x in input().split()]

print(largest_rectangle(n, heights))
