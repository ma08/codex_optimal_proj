

def main():
    N = int(input())
    ans = 0
    for A in range(1, N + 1):
        for B in range(1, N + 1):
            if A * B + B <= N:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()