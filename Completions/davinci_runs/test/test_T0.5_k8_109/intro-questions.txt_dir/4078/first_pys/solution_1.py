

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    segments = []
    for _ in range(m):
        l, r = map(int, input().split())
        segments.append((l, r))
    max_diff = max(a) - min(a)
    if max_diff == 0:
        print(0)
        print(0)
        return
    # print(segments)
    # print(max_diff)
    # print(max(a))
    # print(min(a))
    # print(a)
    # print("----")
    # print(segments)
    # print(a)
    # print(max_diff)
    # print("----")
    for i in range(m):
        for j in range(i+1, m):
            # print("----")
            # print(i, j)
            # print(segments[i])
            # print(segments[j])
            # print("----")
            left = max(segments[i][0], segments[j][0])
            right = min(segments[i][1], segments[j][1])
            # print("----")
            # print(left, right)
            # print("----")
            if left <= right:
                # print("----")
                # print(left, right)
                # print("----")
                for k in range(left, right+1):
                    a[k] -= 1
                # print(a)
                diff = max(a) - min(a)
                # print(diff)
                if diff > max_diff:
                    max_diff = diff
                for k in range(left, right+1):
                    a[k] += 1
    print(max_diff)
    print(0)

if __name__ == '__main__':
    main()