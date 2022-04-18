

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = [0]
            if ans[-1] >= 10:
                ans.append(0)
        while n > 0:
            ans[-1] += n % 10
            n //= 10
        for i in range(len(ans)-1, -1, -1):
            if ans[i] == 0:
                ans[i] = 10
            else:
                ans[i] = ans[i] * (10 ** (len(ans) - i - 1))
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    main()
