

def main():
    x = float(input("Enter float number:\n"))

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x:
                print(f"{i}/{j}")
                break

if __name__ == '__main__':
    main()
