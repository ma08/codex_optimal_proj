
def main():
    r, c, zr, zc = [int(i) for i in input().split()]
    article = [input() for i in range(r)]

    for i in range(r):
        for _ in range(zr):
            new_line = ''
            for k in range(c):
                for _ in range(zc):
                    new_line += article[i][k]
            print(new_line)

if __name__ == '__main__':
    main()
