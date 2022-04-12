

def main():
    R, C, ZR, ZC = [int(i) for i in input().split()]
    article = [input() for i in range(R)]

                new_line = ''
    for i in range(R):
        for j in range(ZR):
            for k in range(C):
                for l in range(ZC):
                    new_line += article[i][k]
                print(new_line)

if __name__ == '__main__':
    main()
