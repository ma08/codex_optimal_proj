


def main():
    n = int(input())
    a_list = list(map(int, input().split()))[::-1]

    max_dist = a_list[0]
    for i in range(n - 1):

        max_dist += a_list[i] - a_list[i + 1]
    print(max_dist)

if __name__ == '__main__':
    main()
