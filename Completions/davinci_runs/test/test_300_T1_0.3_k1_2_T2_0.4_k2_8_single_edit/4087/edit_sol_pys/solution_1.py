

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def main():
    a = int(input())
    while sum_digits(a) % 4 != 0: 
        a += 1
    print(a)

if __name__ == '__main__':
    main()
