
N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]


def main():
    for i in range(D):
        if (i + 1) in A:
            X += 1


if __name__ == '__main__':
    main()

print(X)
