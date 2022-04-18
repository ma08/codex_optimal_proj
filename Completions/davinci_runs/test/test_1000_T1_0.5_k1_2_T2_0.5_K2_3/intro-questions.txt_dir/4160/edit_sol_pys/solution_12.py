

def main():
    x = int(input())
    count = 1
    balance = 10
    while balance <= x:
        count += 1
        balance *= 1.01
    print(count)

if __name__ == '__main__':
    main()
