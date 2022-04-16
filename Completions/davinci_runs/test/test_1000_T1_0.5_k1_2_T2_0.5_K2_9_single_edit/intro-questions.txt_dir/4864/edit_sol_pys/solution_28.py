

def main():
    R, C, Zr, Zc = [int(i) for i in input().split()]
    article = [input() for i in range(R)]

                new_line = ''
    for i in range(R):
        for j in range(Zr):
            for k in range(C):
                for l in range(Zc):
                    new_line += article[i][k]
                print(new_line)

if __name__ == '__main__':
    main()
