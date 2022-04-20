

def f(x):
    return int(str(x+1).rstrip("0")) - 1

def main():
    n = int(input())
    s = set()
    while n not in s and n != 0:
        s.add(n)
        n = f(n)
    print(len(s))

if __name__ == "__main__":
    main()
