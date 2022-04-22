

def main():
    x = int(input("Enter the amount you want to withdraw"))
    # initial balance
    count = 0

    balance = 100
    while balance < x:
        count += 1

        balance += 1

    print(count)

if __name__ == '__main__':
    main()
