

# If you remove a segment, you can only do one of two things: 
# 1. remove a segment that is entirely contained within another segment 
# 2. remove a segment that contains another segment entirely 
# 
# If you remove a segment that is entirely contained within another segment, the maximum length of the resulting intersection is the length of the smallest remaining segment 
# 
# If you remove a segment that contains another segment entirely, the maximum length of the resulting intersection is the length of the largest remaining segment 
# 
# This means that the maximum length of the intersection is the maximum of the length of the smallest remaining segment and the length of the largest remaining segment 

def main():
    n = int(input())
    segments = []
    for _ in range(n):
        segments.append([int(x) for x in input().split()])
    segments.sort(key=lambda x: x[0])

    largest = segments[0][1]
    smallest = segments[0][1] - segments[0][0]
    for i in range(1, n):
        if segments[i][0] >= segments[i - 1][0]:
            largest = max(largest, segments[i][1] - segments[i - 1][0])
        else:
            smallest = min(smallest, segments[i][1] - segments[i][0])
    print(max(largest, smallest))

main()
