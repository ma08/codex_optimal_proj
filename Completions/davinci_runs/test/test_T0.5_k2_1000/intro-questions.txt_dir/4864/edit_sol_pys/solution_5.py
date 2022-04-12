
def main():
    R, C, ZR, ZC = map(int, input().split())
    matrix = [list(input()) for _ in range(R)]
    for row in range(R):
        for i in range(ZR):
            for char in matrix[row]:
                for j in range(ZC):
                    print(char, end='')
            print()

if __name__ == '__main__':
    main()
