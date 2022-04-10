
def read_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    segments = []
    for _ in range(m):
        l, r = map(int, input().split())
        segments.append((l, r))
    return a, segments

def solution(a, segments):
    max_so_far, min_so_far = a[0], a[0]
    for i in range(1, len(a)):
        if a[i] > max_so_far:
            max_so_far = a[i]
        elif a[i] < min_so_far:
            min_so_far = a[i]
    d = max_so_far - min_so_far # the difference between the max and min of the whole array (initially set to 0)
    q = 0
    chosen_segments = [] # store the indices of the chosen segments (initially empty)
    for l, r in segments:
        min_in_segment = a[l-1]
        max_in_segment = a[l-1]
        for i in range(l-1, r):
            if a[i] > max_in_segment:
                max_in_segment = a[i]
            elif a[i] < min_in_segment:
                min_in_segment = a[i]
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
