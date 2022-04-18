

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)

    max_dist = 0
    for i in range(1, n):
        max_dist += a_list[i] - a_list[i - 1]
    print(max_dist)

if __name__ == '__main__':
    main()
