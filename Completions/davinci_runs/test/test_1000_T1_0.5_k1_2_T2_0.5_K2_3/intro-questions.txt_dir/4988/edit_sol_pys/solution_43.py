

def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a-1)

def last_digit(n):
    return fact(n) % 10

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n = int(input().strip())
        print(last_digit(n))

if __name__ == '__main__':
    main()
