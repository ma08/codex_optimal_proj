def main():
    R, C, Zr, Zc = map(int, input().split())
    rows = [input() for _ in range(R)]
    for row in rows:
        for _ in range(Zr):
            for char in row:
                print(char * Zc, end='')
            print()

if __name__ == '__main__':
    main()
