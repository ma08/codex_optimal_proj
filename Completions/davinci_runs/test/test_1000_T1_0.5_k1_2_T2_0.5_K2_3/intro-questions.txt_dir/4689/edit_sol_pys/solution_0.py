
# test

def main():
    k, n = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list.append(a_list[0] + k)

    min_dist = a_list[1] - a_list[0]
    for i in range(n):
        dist = a_list[i + 1] - a_list[i] + k
        if dist < min_dist:
            min_dist = dist

    print(min_dist)


if __name__ == '__main__':
    main()
