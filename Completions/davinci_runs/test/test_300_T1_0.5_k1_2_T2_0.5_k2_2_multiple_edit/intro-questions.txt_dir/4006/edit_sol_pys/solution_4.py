def f(x):
    x = x + 1
    while x % 10 == 0:
        x = x // 10
    return x

def main():
    x = int(input())
    s = set()
    while x not in s:
        s.add(x)
        x = f(x)
    print(len(s))

if __name__ == "__main__":
    main()
