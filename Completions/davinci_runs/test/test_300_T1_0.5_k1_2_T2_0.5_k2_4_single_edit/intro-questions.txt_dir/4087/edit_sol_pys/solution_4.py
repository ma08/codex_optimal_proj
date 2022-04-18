

def main():
    a = int(input('Enter a year: '))
    while True:
        if a % 4 == 0:
            print(a)
            break
        else:
            a += 1

if __name__ == '__main__':
    main()
