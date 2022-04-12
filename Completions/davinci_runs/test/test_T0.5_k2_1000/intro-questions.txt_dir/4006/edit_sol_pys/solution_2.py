def f(n):
    n = n + 1
    while n % 10 == 0 and n > 0:
        n = n // 10
    return n

def main():
    n = int(input())
    memo = set()
    while n not in memo and n > 0:
        memo.add(n)
        n = f(n)
    print(len(memo))

if __name__ == "__main__":
    main()
