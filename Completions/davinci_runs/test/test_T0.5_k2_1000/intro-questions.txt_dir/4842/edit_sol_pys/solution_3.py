
import sys

def main():
    n = int(sys.stdin.readline().strip())
    v = [int(x) for x in sys.stdin.readline().strip().split()]
    diff = [v[i+1]-v[i] for i in range(n-1)]
    while True:
        d = diff[0]
        for i in range(1,len(diff)):
            if diff[i] != d:
                break
        else:
            break
        diff = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
    d = v[n-1]-d
    print(len(diff), d)

if __name__ == '__main__':
    main()
