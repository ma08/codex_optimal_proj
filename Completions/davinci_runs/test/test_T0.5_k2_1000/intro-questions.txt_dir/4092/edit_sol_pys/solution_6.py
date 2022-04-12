
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {0: [-1]}
    for i in range(n):
        if s[i + 1] in d:
            d[s[i + 1]].append(i)
        else:
            d[s[i + 1]] = [i]
    print(sum(len(d[x]) - 1 for x in d))

if __name__ == '__main__':
    main()
