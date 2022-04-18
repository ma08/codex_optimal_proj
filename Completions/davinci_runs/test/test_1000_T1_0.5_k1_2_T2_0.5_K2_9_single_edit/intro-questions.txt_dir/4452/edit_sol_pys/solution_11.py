

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = [10]
        for i in range(9, 1, -1):
            while n % i == 0:
                ans.append(i)
                n //= i
        ans.sort()
        if n == 1:
            print(len(ans))
            print(*ans)
        else:
            print(-1)

if __name__ == "__main__":
    main()
