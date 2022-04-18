


def main():
    X = int(input())
    N = int(input())
    megabytes = X
    for i in range(N):
        megabytes = megabytes - int(input())
    print(megabytes)

if __name__ == '__main__':
    main()
