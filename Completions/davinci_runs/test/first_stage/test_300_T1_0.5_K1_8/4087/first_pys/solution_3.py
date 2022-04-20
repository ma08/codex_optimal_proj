

def sum_digits(n):
    return sum(map(int, str(n)))

def is_interesting(n):
    return sum_digits(n) % 4 == 0

def main():
    a = int(input().strip())
    while not is_interesting(a):
        a += 1
    print(a)

if __name__ == '__main__':
    main()