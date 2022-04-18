
# test

def main():
    k, n = map(int, input().split())
    a_list = [0] + list(map(int, input().split()))
    a_list.append(k)

    min_dist = k
    for i in range(n):
        dist = a_list[i + 1] - a_list[i]
        if dist < min_dist:
            min_dist = dist

    print(min_dist)


if __name__ == '__main__':
    main()
