

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())


    if n <= min(a, b, c, d, e):
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
