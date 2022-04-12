

def main():
    R, C, ZR, ZC = map(int, input().split())  # R: 行数、C: 列数、ZR: 行方向に倍率、ZC: 列方向に倍率
    article = [input() for _ in range(R)]
    for i in range(ZR):
        for row in article:
            for j in range(ZC):
                for char in row:
                    print(char, end='')
                print()
        print()

if __name__ == '__main__':
    main()
