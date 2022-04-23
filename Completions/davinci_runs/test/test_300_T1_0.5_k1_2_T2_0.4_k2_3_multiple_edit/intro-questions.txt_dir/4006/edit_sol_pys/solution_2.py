import sys
input = sys.stdin.readline

def f(x):
    x = x + 1
    while x % 10 == 0:
        x = x // 10
    return x

def main():
    x = int(input())
    memo = set()
    while x not in memo:
        memo.add(x)
        x = f(x)
    print(len(memo))

if __name__ == "__main__":
    main()
