

def main():
    n, m = map(int, input().split())
    a_list = [int(input()) for _ in range(m)]

    min_dist = a_list[0] - a_list[-1]
    for i in range(n - 1):
        min_dist += a_list[i] - a_list[i + 1]
    print(min_dist)

if __name__ == '__main__':
    main()
