

# Solution 1 - O(n log n)

def solve(segments):
    segments.sort()
    current_max_length = 0
    for i in range(len(segments) - 1):
        current_max_length = max(current_max_length, min(segments[i][0], segments[i+1][1]) - max(segments[i][1], segments[i+1][0]))

    return current_max_length

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(solve(segments))
