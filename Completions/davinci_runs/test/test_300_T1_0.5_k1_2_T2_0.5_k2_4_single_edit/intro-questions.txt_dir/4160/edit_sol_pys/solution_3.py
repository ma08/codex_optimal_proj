

def main():
    y = int(input())
    x = int(input())
    count = 0
    balance = 100
    while balance < y:
        count += 1
        balance += 1
    print(count)

if __name__ == '__main__':
    main()
