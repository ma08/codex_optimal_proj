

def main():
    x = int(input())
    count = 0
    balance = 100
    while balance < x:
        count += 1
        balance = balance + balance * 0.01
    print(count)

if __name__ == '__main__':
    main()
