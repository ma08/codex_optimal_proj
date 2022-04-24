

def main():
    x = float(input())
    count = 0
    balance = 100.0
    while balance < x:
        count += 1
        balance += balance * 0.01
    print(count)

if __name__ == '__main__':
    main()
