

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = []
        while n > 0:
            ans.append(n % 10)
            n //= 10
        for i in range(len(ans)):
            if ans[i] == 0:
                ans[i] = 10
            ans[i] = ans[i] * (10 ** i)
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    main()
