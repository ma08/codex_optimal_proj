

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    a_list.reverse()

    min_dist = a_list[0]
    for i in range(n - 1):
        min_dist += a_list[i] - a_list[i + 1]
    print(min_dist)

if __name__ == '__main__':
    main()
