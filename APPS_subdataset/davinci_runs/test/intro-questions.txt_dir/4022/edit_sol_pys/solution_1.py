

# Solution

def solve(segments):
    segments.sort()
    max_length = 0
    for i in range(1, len(segments)):
        max_length = max(max_length, min(segments[i][0], segments[i-1][1]) - max(segments[i][1], segments[i-1][0]))

    return max_length

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
print(solve(segments))
