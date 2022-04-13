

def main():
    R, C, ZR, ZC = map(int, input().split())
    article = [list(input()) for _ in range(R)]
    for row in article:  # row: list
        for _ in range(ZR):
            for char in row:
                for _ in range(ZC):
                    print(char, end='')
            print()

if __name__ == '__main__':
    main()
