

from sys import stdin

def main():
    a = [int(x) for x in stdin.readline().strip().split()]
    a = [x if x % 2 == 0 else x - 1 for x in a]
    print(sum(a) // 2)

main()