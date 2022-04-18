


def is_war(X, Y, x_list, y_list):
    for i in range(X+1, Y+1):
        if i not in x_list and i not in y_list:
            return False
    return True


def main():
    # input
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    # initialization
    answer = 'No War' if is_war(X, Y, x_list, y_list) else 'War'

    # output
    print(answer)


if __name__ == '__main__':
    main()
