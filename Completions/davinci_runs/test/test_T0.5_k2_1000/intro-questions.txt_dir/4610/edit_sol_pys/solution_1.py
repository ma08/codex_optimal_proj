

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    print(max(A) - min(A))


if __name__ == '__main__':
    main()
