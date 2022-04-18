

def main():
    x = int(input())
    balance = 100
    for i in range(x):
        balance = balance * 1.01
        balance = int(balance)
    print(balance)

if __name__ == '__main__':
    main()
