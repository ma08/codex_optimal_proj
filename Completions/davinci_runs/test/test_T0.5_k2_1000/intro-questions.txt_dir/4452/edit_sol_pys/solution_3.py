

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = []
        while n > 0:
            ans.append(n % 10)  # get the last digit
            n //= 10
        for i in range(len(ans)):
            if ans[i] == 0:  # if the last digit is zero, replace it with 10
                ans[i] = 10
            else:
                ans[i] = ans[i] * (10 ** i)
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    main()
