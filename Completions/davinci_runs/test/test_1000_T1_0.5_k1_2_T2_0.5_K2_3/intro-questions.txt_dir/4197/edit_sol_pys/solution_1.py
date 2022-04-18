

def main():
    A = [int(i) for i in input().split()]
    N = int(input())

    for i in range(N):
        print(A.index(i+1)+1, end=' ')


if __name__ == '__main__':
    main()
