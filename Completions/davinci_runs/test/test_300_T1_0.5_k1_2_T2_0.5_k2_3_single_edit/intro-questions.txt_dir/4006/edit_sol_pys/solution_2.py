
def f(n):
    n = n + 1
    while n % 10 == 0:
        n = n / 10
    return n

def main():
    n = int(input())
    memo = []
    while True:
        if n in memo:
            break
        memo.append(n)
        n = f(n)
    print(len(memo))

if __name__ == "__main__":
    main()
