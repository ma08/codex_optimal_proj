

def main():
    R, C, ZR, ZC = map(int, input().split())
    line_num = 0
    article = [input() for _ in range(R)]
        line_num += 1
        if line_num == R:
            line_num = 0
    for row in article:
        for i in range(ZR):
            for char in row:
                for j in range(ZC):
                    print(char, end='')
            if line_num == 0:
                print()
            else:
                print('', end='\n')

if __name__ == '__main__':
    main()
