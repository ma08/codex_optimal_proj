# AtCoder Beginner Contest 048
# C - Boxes and Candies
# https://atcoder.jp/contests/abc048/tasks/arc064_a


def main():
    N, x = map(int, input().split())
    a_list = list(map(int, input().split()))

    # initialization
    answer = 0
    for i in range(N-1):
        if a_list[i] + a_list[i+1] > x:
            answer += a_list[i] + a_list[i+1] - x
            if a_list[i+1] > x:
                a_list[i+1] = x
            else:
                a_list[i+1] = 0

    # output
    print(answer)    


if __name__ == '__main__':
    main()
