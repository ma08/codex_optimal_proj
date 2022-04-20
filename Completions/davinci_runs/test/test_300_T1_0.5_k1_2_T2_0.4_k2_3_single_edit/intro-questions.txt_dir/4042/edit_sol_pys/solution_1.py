

def main():
    x = float(input("Enter a float number: "))

    for i in range(1, 11):
        for j in range(1, 11):
            if i / j == x and i % j == 0:
                print("{} / {} = {}".format(i, j, x))

if __name__ == '__main__':
    main()
