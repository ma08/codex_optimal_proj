


def main():
    # input
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    # initialization
    answer = 'No War'
    for i in range(X+1, Y+1):
        if i not in x_list and i not in y_list:
            answer = 'War'
            break

    # output
    print(answer)


if __name__ == '__main__':
    main()
