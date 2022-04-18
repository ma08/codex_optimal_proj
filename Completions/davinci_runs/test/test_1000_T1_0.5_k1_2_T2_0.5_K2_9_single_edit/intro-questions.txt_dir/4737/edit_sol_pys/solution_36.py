

def main():
    n = int(input())
    if n % 2 == 1:
        print(0)
        return
    n //= 2
    ans = 0
    for i in range(1, n + 1):
        if i % 5 == 0:
            continue
        ans += 2 ** (n - i)
    print(ans)

if __name__ == "__main__":
    main()
