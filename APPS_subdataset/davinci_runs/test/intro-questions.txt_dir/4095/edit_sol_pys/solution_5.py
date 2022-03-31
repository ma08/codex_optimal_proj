import sys
input = sys.stdin.readline



def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))[:n]
    left_list = []
    right_list = []
    for i in range(n):
        if p[i] < m:
            left_list.append(p[i])
        elif p[i] > m:
            right_list.append(p[i])
    left_len = len(left_list)
    right_len = len(right_list)
    left_list.sort()
    right_list.sort()
    if left_len == 0 or right_len == 0:
        print(0)
        return
    if left_len < right_len:
        print(left_len * (n - right_len))
    else:
        print(right_len * (n - left_len))


if __name__ == "__main__":
    main()
