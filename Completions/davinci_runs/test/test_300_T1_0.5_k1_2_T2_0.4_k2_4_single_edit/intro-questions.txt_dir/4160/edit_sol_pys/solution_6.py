
def main():
    x = int(input("Enter the balance: "))
    count = 0
    balance = 100
    while balance < x:
        count += 1
        balance += 1
    print("The number of years is: ", count)

if __name__ == '__main__':
    main()
