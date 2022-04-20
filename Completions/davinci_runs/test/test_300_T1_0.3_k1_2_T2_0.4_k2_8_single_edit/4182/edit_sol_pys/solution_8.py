
from sys import stdin

def main():
    n, m, x, y = [int(x) for x in stdin.readline().split()] # read n, m, x, y
    xs = [int(x) for x in stdin.readline().split()] # read xs
    ys = [int(x) for x in stdin.readline().split()] # read ys
    if x < y:
        for i in range(x+1, y+1): # loop from x+1 to y
            if all(i > x for x in xs) and all(i <= y for y in ys): # if i > all xs and i <= all ys, print 'No War' and exit
                print('No War')
                exit()
    print('War')

if __name__ == '__main__':
    main()
