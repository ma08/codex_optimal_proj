
from collections import defaultdict
from sys import stdin, stdout

def read_ints():
    return [int(x) for x in stdin.readline().strip().split()]

def read_int():
    return int(stdin.readline().strip())

def main():
    n = read_int()
    a = read_ints()
    d = defaultdict(int)
    for x in a:
        d[x] += 1
    result = 1
    for x in d:
        result = result * (d[x]+1) % MOD
    stdout.write(str(result))


if __name__ == "__main__":
    main()
