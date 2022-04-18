


def main():
    N = int(input())
    S = [0] * 100001
    for i in range(N):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            S[j] = 1
    print(sum(S))

if __name__ == '__main__':
    main()
