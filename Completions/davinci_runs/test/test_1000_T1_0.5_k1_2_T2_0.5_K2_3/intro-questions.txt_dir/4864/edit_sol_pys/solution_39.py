

def main():
    r, c, zr, zc = [int(i) for i in input().split()]
    article = [input() for i in range(r)]

    for i in range(r):
        for j in range(zr):
            new_line = []
            for k in range(c):
                for l in range(zc):
                    new_line.append(article[i][k])
            new_line = ''.join(new_line)
            print(new_line)

if __name__ == '__main__':
    main()
