

def main():
    x = int(input('Enter balance: '))
    count = 0
    balance = 100
    while balance < x:
        count += 1
        balance *= 1.01
    print('Need', count, 'days')

if __name__ == '__main__':
    main()
