

def main():
    a = int(input('Enter number: '))
    while True:
        if a % 4 == 0:
            print('Result: ', a)
            break
        else:
            a += 1

if __name__ == '__main__':
    main()
