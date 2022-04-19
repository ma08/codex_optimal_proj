

def sum_digits(a):
    s = 0
    while a:
        s += a % 10
        a //= 10
    return s

def main():
    a = int(input())
    while sum_digits(a) % 4 != 0:
        a += 1
    print(a)

if __name__ == '__main__':
    main()
