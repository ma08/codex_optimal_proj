

def main():
    x = int(input())  # x is the amount of money you want to save
    count = 0
    balance = 100  # balance is the amount of money you have
    while balance < x:
        count += 1
        balance += 1
    print(count)


if __name__ == '__main__':
    main()
