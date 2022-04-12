
def main():
    k, n = map(int, input().split())
    a_list = list(map(int, input().split())) + [0]
    a_list.append(a_list[0] + k)  # 先頭と末尾を繋げる

    min_dist = k
    for i in range(n):
        dist = a_list[i + 1] - a_list[i]
        if dist < min_dist:
            min_dist = dist

    print(min_dist)


if __name__ == '__main__':
    main()
