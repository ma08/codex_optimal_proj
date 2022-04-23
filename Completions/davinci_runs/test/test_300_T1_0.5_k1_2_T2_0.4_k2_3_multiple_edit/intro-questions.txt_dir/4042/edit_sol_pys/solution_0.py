
def main():
    x = float(input())

    for i in range(1, 100):
        for j in range(1, 100):
            if i / j == x and i % j == 0:
                print(i, j)
                break

if __name__ == '__main__':
    main()
