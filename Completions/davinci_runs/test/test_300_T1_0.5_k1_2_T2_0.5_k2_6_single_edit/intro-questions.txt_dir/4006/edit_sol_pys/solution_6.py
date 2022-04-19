
def f(n):
    n = str(n + 1)
    while n.endswith('0'):
        n = n[:-1]
    return n

def main():
    n = int(input())
    memo = set()
    while n not in memo:
        memo.add(n)
        n = f(n)
    print(len(memo))

if __name__ == "__main__":
    main()
