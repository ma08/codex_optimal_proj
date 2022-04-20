

def f(n):
    if n % 10 == 0:
        return f(n // 10)
    else:
        return n + 1

def f_r(n):
    s = set([])
    while True:
        s.add(n)
        n = f(n)
        if n in s:
            break
    return s

def main():
    n = int(input())
    print(len(f_r(n)))

if __name__ == "__main__":
    main()
