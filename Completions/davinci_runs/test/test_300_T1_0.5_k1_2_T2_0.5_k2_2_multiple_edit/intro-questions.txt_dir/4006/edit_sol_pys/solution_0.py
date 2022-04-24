
def f(n, k):
    if n >= k:
        return n - k
    else:
        return f(n * 2, k) + 1

def main():
    n = int(input())
    k = int(input())
    memo = set()
    while n not in memo:
        memo.add(n)
        n = f(n, k)
    print(len(memo))

if __name__ == "__main__":
    main()
