
def main():
    n = int(input("Enter a number: "))
    count = 0
    while n > 0:
        if n % 6 == 0:
            n = n // 6
            count += 1
        elif n % 9 == 0:
            n = n // 9
            count += 1
        else:
            n = n - 1
            count += 1
    print("The answer is ", count)

if __name__ == '__main__':
    main()
