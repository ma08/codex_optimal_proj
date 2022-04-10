
def read_input():
    n, m = map(int, input().split())  # n - number of elements in array, m - number of segments
    a = list(map(int, input().split()))
    segments = []
    for _ in range(m):
        l, r = map(int, input().split())
        segments.append((l, r))
    return a, segments

def solution(a, segments):
    d = max(a) - min(a)
    q = 0
    chosen_segments = []
    for l, r in segments:
        if max(a[l-1:r]) - min(a[l-1:r]) > d:
            q = 1
            chosen_segments = [l]
            d = max(a[l-1:r]) - min(a[l-1:r])
        elif max(a[l-1:r]) - min(a[l-1:r]) == d:
            q += 1
            chosen_segments.append(l)
    print(d)
    print(q)
    print(*chosen_segments)

if __name__ == "__main__":
    a, segments = read_input()
    solution(a, segments)
