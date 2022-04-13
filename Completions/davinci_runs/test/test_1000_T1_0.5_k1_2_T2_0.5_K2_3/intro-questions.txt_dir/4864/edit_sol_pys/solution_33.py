

def main():
    r, c, zr, zc = [int(i) for i in input().split()]
    article = [input() for i in range(r)]

    for i in range(r * zr):
        new_line = ''
        for j in range(c):
            for k in range(zc):
                new_line += article[int(i / zr)][j]
        print(new_line)

if __name__ == '__main__':
    main()
