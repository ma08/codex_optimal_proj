

import sys

def main():
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        s = sys.stdin.readline().strip()
        m = int(sys.stdin.readline().strip())
        b = [int(x) for x in sys.stdin.readline().strip().split()]
        t = []
        for i in range(m):
            if b[i] <= i:
                t.append(s[i-b[i]])
            else:
                t.append(s[i])
        print(''.join(t))

if __name__ == "__main__":
    main()