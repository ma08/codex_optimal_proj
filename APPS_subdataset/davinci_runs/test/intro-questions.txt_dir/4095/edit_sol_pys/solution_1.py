

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    left_list = []
    right_list = []
    for i in range(n):
        if p[i] < m:
            left_list.append(p[i])
        elif p[i] > m:
            right_list.append(p[i])
    left_list_len = len(left_list)
    right_list_len = len(right_list)
    left_list.sort(reverse=True)
    right_list.sort(reverse=True)
    if left_list_len == 0 or right_list_len == 0:
        print(0)
        return
    if left_list_len < right_list_len:
        print(left_list_len * (right_list_len - left_list_len))
    else:
        print(right_list_len * (left_list_len - right_list_len))


if __name__ == "__main__":
    main()
