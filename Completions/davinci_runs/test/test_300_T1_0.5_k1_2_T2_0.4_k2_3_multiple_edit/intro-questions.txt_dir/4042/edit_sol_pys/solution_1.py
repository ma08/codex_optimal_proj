

def main():
    x = float(input('Enter a number: '))

    for i in range(1, 100):
        for j in range(1, 100):
            if i / j == x:
                print(i, j)
                break

if __name__ == '__main__':
    main()
