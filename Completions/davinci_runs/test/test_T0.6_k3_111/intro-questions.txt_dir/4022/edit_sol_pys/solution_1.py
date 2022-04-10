

class Segment:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def main():
    segments = []
    n = int(input())
    for _ in range(n):
        l, r = [int(i) for i in input().split()]
        segments.append(Segment(l, r))
    print(solve(segments))

def solve(segments):
    segments = sorted(segments, key=lambda x: (x.left, x.right))
    max_length = 0
    for i in range(len(segments)):
        left = segments[i].left
        right = segments[i].right
        max_right = right
        for j in range(i+1, len(segments)):
            if segments[j].left <= right:
                max_right = max(max_right, segments[j].right)
            else:
                break
        max_length = max(max_length, max_right - left)
    return max_length

if __name__ == "__main__":
    main()
