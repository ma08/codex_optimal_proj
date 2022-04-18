

def main():
    a = int(input("Enter number: "))
    while True:
        if a % 5 == 0:
            print(a)
            break
        else:
            a += 1

if __name__ == '__main__':
    main()
