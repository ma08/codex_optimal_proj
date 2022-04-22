

def main():
    x = int(input())
    count = 0
    balance = 100
    while balance < x:
        count += 1
        balance += 1
    print(count, balance)

if __name__ == '__main__': 
    main()
