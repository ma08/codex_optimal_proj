

def get_segments(a, m):
    segments = []
    for i in range(m):
        l, r = map(int, input().split())
        segments.append((l-1, r-1))
    return segments

def get_max_min(a, segments):
    max_min = 0
    for i, j in segments:
        max_min = max(max_min, max(a[i:j+1]) - min(a[i:j+1]))
    return max_min

def find_max_segments(a, segments):
    max_min = 0
    res = []
    for i, j in segments:
        if max(a[i:j+1]) - min(a[i:j+1]) == max_min:
            res.append((i, j))
        elif max(a[i:j+1]) - min(a[i:j+1]) > max_min:
            max_min = max(a[i:j+1]) - min(a[i:j+1])
            res = [(i, j)]
    return max_min, res

def find_max_segments_index(segments, res):
    res_index = []
    for i in range(len(segments)):
        if segments[i] in res:
            res_index.append(i+1)
    return res_index

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    segments = get_segments(a, m)
    max_min, res = find_max_segments(a, segments)
    res_index = find_max_segments_index(segments, res)
    print(max_min)
    print(len(res_index))
    print(*res_index)

if __name__ == '__main__':
    main()