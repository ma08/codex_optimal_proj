

def main():
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    segments = sorted(segments)
    # print(segments)
    max_intersection = 0
    for i in range(n - 1):
        l = segments[i][0]
        r = segments[i][1]
        l_next = segments[i + 1][0]
        r_next = segments[i + 1][1]
        if l_next > r:
            if max_intersection < 0:
                max_intersection = 0
        elif l_next <= r:
            if r_next <= r:
                max_intersection = max(max_intersection, r_next - l_next)
            else:
                max_intersection = max(max_intersection, r - l_next)
    print(max_intersection)

if __name__ == "__main__":
    main()