

def coconut(n):
    s = 0
    for i in range(n):
        s += i
    return s

def main():
    n = int(input())
    print(coconut(n))

if __name__ == "__main__":
    main()
