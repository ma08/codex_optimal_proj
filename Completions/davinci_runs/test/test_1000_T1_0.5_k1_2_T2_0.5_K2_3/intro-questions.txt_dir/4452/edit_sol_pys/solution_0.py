

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = [int(i) for i in str(n)]
        for i in range(len(ans)):
            ans[i] = ans[i] * (10 ** i)
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    main()
