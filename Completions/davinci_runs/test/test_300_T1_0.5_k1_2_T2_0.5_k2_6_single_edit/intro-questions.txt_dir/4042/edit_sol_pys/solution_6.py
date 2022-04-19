

def main():
    x = float(input())

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x:
                print(i, j, sep=' ')
                break

if __name__ == '__main__':
    main()
