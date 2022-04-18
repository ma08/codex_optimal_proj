def main():
    R, C, ZR, ZC = map(int, input().split())
    article = [input() for _ in range(R)]
    for row in article:  # row: str
        for i in range(ZR):
            for char in row:  # char: str
                for j in range(ZC):
                    print(char, end='')
            print()

if __name__ == '__main__':
    main()
