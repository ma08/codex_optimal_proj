

if __name__ == "__main__":
    a, b, x = map(int, input().split())
    if x < a:
        print(0)
    else:
        n = 10**9
        while n >= 1:
            if a * n + b * len(str(n)) <= x:
                print(n)
                exit()
            n -= 1
        print(0)