
def f(n):
    n = n + 1
    while n % 10 == 0:
        n = n // 10
    return int(n)

def main():
    n = int(input())
    memo = []
    while True:
        memo.append(n)
        n = f(n)
        if n in memo:
            break
    print(len(memo))

if __name__ == "__main__":
    main()
