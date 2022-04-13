

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def main():
    n = int(input())
    print(lucas(n))

if __name__ == '__main__':
    main()
