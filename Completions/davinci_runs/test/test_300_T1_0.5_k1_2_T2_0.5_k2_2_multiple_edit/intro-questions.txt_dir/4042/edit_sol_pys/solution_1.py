

def main(x):

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x:
                print(i, j, sep=' ')
                break

if __name__ == '__main__':
    x = float(input())
    main(x)
