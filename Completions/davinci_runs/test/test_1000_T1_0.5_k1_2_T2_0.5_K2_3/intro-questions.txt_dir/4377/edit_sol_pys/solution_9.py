

from sys import stdin

def main():
    a, b, c = [int(x) for x in stdin.readline().strip().split()]
    print(a * b * c)

 
if __name__ == '__main__':
    main()
