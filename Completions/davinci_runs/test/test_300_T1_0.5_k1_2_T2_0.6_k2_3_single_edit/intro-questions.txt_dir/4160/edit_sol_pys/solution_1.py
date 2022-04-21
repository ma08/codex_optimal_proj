

def main():
    x = int(raw_input())
    count = 0
    balance = 100
    while balance < x:
        count += 1
        balance += 1
    print count

if __name__ == '__main__':
    main()
