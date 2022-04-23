

def main():
    x = int(input())
    y = int(input())

    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    main()
