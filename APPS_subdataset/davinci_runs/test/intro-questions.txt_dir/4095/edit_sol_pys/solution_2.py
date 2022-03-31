

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
    left_list_length = len(left_list)
    right_list_length = len(right_list)
    left_list.sort()
    right_list.sort()
    if left_list_length == 0 or right_list_length == 0:
        print(0)
        return
    if left_list_length < right_list_length:
        print(left_list_length * (n - right_list_length))
    else:
        print(right_list_length * (n - left_list_length))


if __name__ == "__main__":
    main()
