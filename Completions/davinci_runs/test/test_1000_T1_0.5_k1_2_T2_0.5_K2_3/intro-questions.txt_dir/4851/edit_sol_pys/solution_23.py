
def sum_digits(n):

    return sum(int(x) for x in str(n))

def main():
    num = int(input())
    while num % sum_digits(num) != 0:
        num += 1
    print(num)

if __name__ == '__main__':
    main()
