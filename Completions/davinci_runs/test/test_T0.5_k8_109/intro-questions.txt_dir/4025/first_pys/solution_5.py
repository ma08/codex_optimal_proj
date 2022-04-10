

from sys import stdin

def main():
    a, b, c = [int(x) for x in stdin.readline().split()]
    print(min(a, b//2, c//3)*7)

main()