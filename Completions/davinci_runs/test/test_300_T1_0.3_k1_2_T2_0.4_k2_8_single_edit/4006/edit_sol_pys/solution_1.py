

def f(x):
    return int(str(x + 1).rstrip("0"))

def main():
    n = int(input())
    s = set()
    while n not in s:
        s.add(n)
        n = f(n)
    print(len(s))

if __name__ == "__main__":
    main()
