

def main():
    x = int(input("please enter a number: "))
    count = 0
    balance = 100
    while balance < x:
        count += 1
        balance += 1
    print(count)

if __name__ == '__main__':
    main()
