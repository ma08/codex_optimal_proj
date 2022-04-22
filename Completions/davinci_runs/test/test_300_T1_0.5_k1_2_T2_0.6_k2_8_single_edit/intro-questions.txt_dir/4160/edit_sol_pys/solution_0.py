

def main():
    x = int(input())
    count = 0
    balance = 1000
    while balance <= x:
        count += 1
        balance += balance // 10
    print(count)

if __name__ == '__main__':
    main()
