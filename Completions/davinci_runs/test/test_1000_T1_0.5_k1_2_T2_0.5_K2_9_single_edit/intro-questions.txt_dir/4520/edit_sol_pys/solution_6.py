

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    segments = []
    for i in range(n):
        segments.append(list(map(int, sys.stdin.readline().split())))
    print(n - len(SegmentTree(segments, k)))
    print(" ".join(map(str, SegmentTree(segments, k).remove().reverse())))

class SegmentTree:
    def __init__(self, segments, k):
        self.segments = sorted(segments, key=lambda x: x[0])
        self.k = k
        self.tree = self.build(0, len(segments) - 1, 0)

    def build(self, left, right, i):
        if left == right:
            return self.segments[left]
        mid = (left + right) // 2
        return self.merge(self.build(left, mid, 2 * i + 1), self.build(mid + 1, right, 2 * i + 2))

    def merge(self, s1, s2):
        if s1[0] > s2[1]:
            return s1
        if s2[0] > s1[1]:
            return s2
        return [min(s1[0], s2[0]), max(s1[1], s2[1])]

    def query(self, left, right, segment):
        if segment[1] < left or segment[0] > right:
            return 0
        if left <= segment[0] and right >= segment[1]:
            return 1
        mid = (segment[0] + segment[1]) // 2 + 1
        return self.query(left, right, segment[:mid]) + self.query(left, right, segment[mid:])

    def remove(self):
        removed = []
        for i in range(len(self.segments)):
            if self.query(self.segments[i][0], self.segments[i][1], self.tree) <= self.k:
                removed.append(i + 1)
        return removed

if __name__ == "__main__":
    main()
