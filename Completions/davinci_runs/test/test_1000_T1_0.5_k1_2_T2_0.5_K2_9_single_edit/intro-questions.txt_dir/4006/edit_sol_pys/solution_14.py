
def f(x):
    x = x + 1
    while x % 10 == 0:
        x = x // 10
    return x

def main():
    n = int(input())
    memo = set()
    while n not in memo:
        memo.add(n)
        n = f(n)
    print(len(memo))

if __name__ == "__main__":
    main()
