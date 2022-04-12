

def calc_min_dist(a_list):
    min_dist = 0
    for i in range(len(a_list) - 1):
        min_dist += abs(a_list[i] - a_list[i + 1])
    return min_dist * 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    a_list.reverse()
    print(a_list)

    print(calc_min_dist(a_list))

if __name__ == '__main__':
    main()
