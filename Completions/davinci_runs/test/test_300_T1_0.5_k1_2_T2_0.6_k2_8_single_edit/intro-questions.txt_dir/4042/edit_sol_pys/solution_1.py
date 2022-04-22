

def main():
    x = float(input())

    for i in range(10, 99):
        for j in range(10, 99):
            if float(i) / j == x:
                print(i, j)
                break

if __name__ == '__main__':
    main()
