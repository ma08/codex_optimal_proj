

def main():
    R, C, Zr, Zc = [int(i) for i in input().split()]
    article = [input() for _ in range(R)]

    for i in range(R * Zr):
        for j in range(Zc):
            new_line = ''
            for k in range(C * Zc):
                new_line += article[i // Zr][k // Zc]
            print(new_line)

if __name__ == '__main__':
    main()
