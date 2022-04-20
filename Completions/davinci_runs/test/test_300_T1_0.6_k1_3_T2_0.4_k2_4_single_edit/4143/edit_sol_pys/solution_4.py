

def main():
    N, A, B, C, D, E = list(map(int, input().split()))


    A, B = A - 1, B - 1
    C, D = C - 1, D - 1

    ans = 0

    for n in range(N):
        if n % (A + B) < A:
            ans += 1

        if n % (C + D) < C:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
