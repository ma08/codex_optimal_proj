

def main():
    x = float(input("Enter a number: "))

    for i in range(1, 10):
        if i / x == i // x:
            print(i, x)
            break

if __name__ == '__main__':
    main()
