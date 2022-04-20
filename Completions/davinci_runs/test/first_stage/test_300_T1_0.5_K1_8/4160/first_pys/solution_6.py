

def main():
    x = int(input())
    years = 0
    balance = 100
    while balance < x:
        balance += balance * 0.01
        years += 1
    print(years)

if __name__ == '__main__':
    main()