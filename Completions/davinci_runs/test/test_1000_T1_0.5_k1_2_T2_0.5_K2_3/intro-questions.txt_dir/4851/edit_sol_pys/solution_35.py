

def sum_digits(n):
    return sum(int(x) for x in str(n) if x != '-')

def main():
    num = int(input())
    if num < 0:
        while num % sum_digits(num) != 0:
            num -= 1
    else:
        while num % sum_digits(num) != 0:
            num += 1
    print(num)

if __name__ == '__main__':
    main()
