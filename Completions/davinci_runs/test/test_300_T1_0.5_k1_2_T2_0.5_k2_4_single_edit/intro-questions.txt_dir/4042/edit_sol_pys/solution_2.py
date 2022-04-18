

def main():
    x = int(input())

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x or i * j == x:
                print(i, j)
                break

if __name__ == '__main__':
    main()
