


def main():
    # input
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    # initialization
    answer = 'War'
    for i in range(X+1, Y):
        if i not in x_list and i not in y_list:
            answer = 'No War'
            break

    # output
    print(answer)


if __name__ == '__main__':
    main()
