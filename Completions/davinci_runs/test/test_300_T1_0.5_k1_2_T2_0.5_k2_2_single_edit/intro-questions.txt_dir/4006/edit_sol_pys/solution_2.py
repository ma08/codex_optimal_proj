
def f(n):
    return n + 1

def main():
    n = int(input())
    memo = set()
    while n not in memo:
        memo.add(n)
        n = f(n)
    print(len(memo))

if __name__ == "__main__":
    main()
