

def main():
    x = float(input())

    for i in range(1, 100):
        if i / x == int(i / x):
            print(i, int(i / x))
            break

if __name__ == '__main__':
    main()
