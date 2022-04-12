

def main():
    R, C, ZR, ZC = [int(i) for i in input().split()]
    article = [input() for _ in range(R)]

    for i in range(R):
        for _ in range(ZR):
            new_line = ''
            for k in range(C):
                for _ in range(ZC):
                    new_line += article[i][k]
            print(new_line, end='')
        print()

if __name__ == '__main__':
    main()
