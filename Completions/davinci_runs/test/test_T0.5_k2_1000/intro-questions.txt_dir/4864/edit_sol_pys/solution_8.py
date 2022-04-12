

def main():
    R, C, Zr, Zc = map(int, input().split())
    lines = [input() for _ in range(R)]
    for line in lines:
        for i in range(Zr):
            for char in line:
                for j in range(Zc):
                    print(char, end='')  # end='' is to avoid the newline
            print()  # newline

if __name__ == '__main__':
    main()
