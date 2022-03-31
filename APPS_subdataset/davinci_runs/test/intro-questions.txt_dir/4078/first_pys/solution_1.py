
def read_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    segments = []
    for _ in range(m):
        l, r = map(int, input().split())
        segments.append((l, r))
    return a, segments

def solution(a, segments):
    max_so_far = max(a)
    min_so_far = min(a)
    d = max_so_far - min_so_far
    q = 0
    chosen_segments = []
    for l, r in segments:
        min_in_segment = min(a[l-1:r])
        max_in_segment = max(a[l-1:r])
        if max_in_segment - min_in_segment > d:
            q = 1
            chosen_segments = [l]
            d = max_in_segment - min_in_segment
        elif max_in_segment - min_in_segment == d:
            q += 1
            chosen_segments.append(l)
    print(d)
    print(q)
    print(*chosen_segments)

if __name__ == "__main__":
    a, segments = read_input()
    solution(a, segments)