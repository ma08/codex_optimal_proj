

def main():
    N = int(input())
    A = [input() for _ in range(N)]
    M = int(input())
    B = [input() for _ in range(M)]

    ans = 0
    for a in A:
        if a in B:
            ans -= 1
        else:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
