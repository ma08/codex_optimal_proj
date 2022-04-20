
import sys

def main():    
    n = int(input())
    a = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == '#':
                if a[i - 1][j] == '#' and a[i + 1][j] == '#' and a[i][j - 1] == '#' and a[i][j + 1] == '#':
                    continue
                else:
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()
