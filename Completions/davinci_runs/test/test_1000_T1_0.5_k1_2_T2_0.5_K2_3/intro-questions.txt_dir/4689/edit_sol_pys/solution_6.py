
def main():
    k, n = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x_list[0] + k)

    min_dist = k
    for i in range(n):
        dist = x_list[i + 1] - x_list[i]
        if dist < min_dist:
            min_dist = dist

    print(min_dist)


if __name__ == '__main__':
    main()
