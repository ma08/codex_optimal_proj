

def sum_digits(n):
    return sum(int(x) for x in str(n)) # sum of digits

def main():
    n = int(input())
    while n % sum_digits(n) != 0: # if the number is not divisible by the sum of its digits
        n += 1
    print(n)

if __name__ == '__main__':
    main()
