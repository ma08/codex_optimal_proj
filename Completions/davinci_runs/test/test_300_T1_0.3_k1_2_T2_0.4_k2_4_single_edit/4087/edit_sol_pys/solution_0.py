
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def main():
    n = int(input())
    while sum_digits(n) % 4 != 0:
        n += 1
    print(n)

if __name__ == '__main__':
    main()
