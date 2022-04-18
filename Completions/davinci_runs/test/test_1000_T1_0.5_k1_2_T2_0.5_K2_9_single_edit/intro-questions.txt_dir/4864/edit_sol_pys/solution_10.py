

def main():
    r, c, zr, zc = [int(i) for i in input().split()]
    article = [input() for _ in range(r)]
    for i in range(r):
        for _ in range(zr):
            print(''.join(c * zc for c in article[i]))

if __name__ == '__main__':
    main()
