

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    a_list.reverse()
        print(max_dist)
    print(a_list)

    max_dist = a_list[0] - a_list[-1]
    for i in range(n - 1):
        max_dist += a_list[i] - a_list[i + 1]
    print(max_dist)

if __name__ == '__main__':
    main()
