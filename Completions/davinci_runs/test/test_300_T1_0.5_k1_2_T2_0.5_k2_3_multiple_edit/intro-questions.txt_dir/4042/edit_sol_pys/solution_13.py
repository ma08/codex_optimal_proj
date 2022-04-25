

def main():
    x = int(input())

    for i in range(1, 100):
        if x % i == 0 and x / i < 100 and i % 10 != 0 and x / i % 10 != 0:
            print(i, int(x / i))

if __name__ == '__main__':
    main()
