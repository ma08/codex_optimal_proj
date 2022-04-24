
def f(n):
    return n + 1 if n % 10 else f(n // 10)

def r(n):
    s = set([])
    while True:
        s.add(n)
        n = f(n)
        if n in s: break
    return s

def main():
    n = int(input())
    print(len(r(n)))

if __name__ == "__main__":
    main()
