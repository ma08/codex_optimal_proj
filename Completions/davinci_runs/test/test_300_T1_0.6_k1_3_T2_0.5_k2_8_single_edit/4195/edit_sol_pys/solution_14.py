

def main():
    D, N = map(int, input().split())  # D, N = int(input().split())

    if D == 0:
        print(N)  # print('{}'.format(N))
    elif D == 1:
        print(100 * N)  # print('{}'.format(100 * N))
    else:
        print(10000 * N)  # print('{}'.format(10000 * N))

if __name__ == '__main__':
    main()
