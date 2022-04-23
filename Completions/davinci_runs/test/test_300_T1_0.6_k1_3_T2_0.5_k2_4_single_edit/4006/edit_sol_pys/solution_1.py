
def f(n):
    if n % 10 == 0:  # if n is a multiple of 10
        return f(n // 10)
    else:
        return n + 1

def r(n):
    s = set([])
    while True:
        s.add(n)
        n = f(n)
        if n in s:  # if n is already in the set
            break
    return s

def main():
    n = int(input())
    print(len(r(n)))

if __name__ == "__main__":
    main()
