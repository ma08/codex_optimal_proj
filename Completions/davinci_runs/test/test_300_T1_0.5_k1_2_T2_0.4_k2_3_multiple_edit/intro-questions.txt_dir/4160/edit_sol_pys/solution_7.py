

def main():
    x = int(input("Enter a number: "))
    count = 0
    balance = 1000
    while balance <= x:
        count += 1
        balance += 1
    print(count)

if __name__ == '__main__':
    main()
