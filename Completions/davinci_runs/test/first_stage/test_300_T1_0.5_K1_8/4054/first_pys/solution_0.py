

from sys import stdin

def main():
    a = [int(x) for x in stdin.readline().split()]
    print(a.count(0))

main()