
def main():
    R, C, ZR, ZC = map(int, input().split())
    article = [list(input()) for _ in range(R)]  # article: list of list of str
    for row in article:  # row: list of str
        for i in range(ZR):
            for char in row:  # char: str
                for j in range(ZC):
                    print(char, end='')
            print()

if __name__ == '__main__':
    main()
