
import sys

def main():
    n = int(sys.stdin.readline().strip())
    v = [int(x) for x in sys.stdin.readline().split()]
    diff = [v[i+1]-v[i] for i in range(n)]
    while True:
        d = diff[0]
        for i in range(len(diff)-1):
            if diff[i] != d:
                break
        else:
            break
        diff = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
    d = v[n-1]-d
    print(len(diff), d)

if __name__ == '__main__':
    main()
