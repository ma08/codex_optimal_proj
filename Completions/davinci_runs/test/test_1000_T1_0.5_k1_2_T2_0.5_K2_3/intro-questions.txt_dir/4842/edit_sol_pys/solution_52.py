
import sys

def main():
    n = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))
    d = 1
    while True:
        v_diff = []
        for i in range(len(v) - 1):
            v_diff.append(v[i + 1] - v[i])
        v = v_diff
        if len(set(v)) == 1:
            print(d, v[0] * d + v[0])
            break
        d += 1

if __name__ == '__main__':
    main()
