import sys


def solve(n, s):
    max_count = 0
    max_gram = ''
    for i in range(len(s) - 1):
        gram = s[i:i+2]
        count = s.count(gram)
        if count > max_count:
            max_count = count
            max_gram = gram
    return max_gram

def main():
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    print(solve(n, s))

if __name__ == '__main__':
    main()
