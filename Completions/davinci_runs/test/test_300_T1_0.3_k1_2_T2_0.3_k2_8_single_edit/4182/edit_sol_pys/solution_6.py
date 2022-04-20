

from sys import stdin

def main():
    n, m, x, y = [int(x) for x in stdin.readline().split()]
    xs = [int(x) for x in stdin.readline().split()]
    ys = [int(x) for x in stdin.readline().split()]
    for i in range(x+1, y+1):
        if all(i > x for x in xs) and all(i <= y for y in ys):
            print('No War')
            exit()
    print('War')

if __name__ == '__main__':
    main()
