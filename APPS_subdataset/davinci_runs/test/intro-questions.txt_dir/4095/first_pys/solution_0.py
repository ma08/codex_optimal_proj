

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    left = []
    right = []
    for i in range(n):
        if p[i] < m:
            left.append(p[i])
        elif p[i] > m:
            right.append(p[i])
    left_len = len(left)
    right_len = len(right)
    left.sort()
    right.sort()
    if left_len == 0 or right_len == 0:
        print(0)
        return
    if left_len < right_len:
        print(left_len * (n - right_len))
    else:
        print(right_len * (n - left_len))


if __name__ == "__main__":
    main()