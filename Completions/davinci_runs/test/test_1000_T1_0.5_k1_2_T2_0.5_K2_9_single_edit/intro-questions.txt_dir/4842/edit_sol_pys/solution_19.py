import sys

def main():
    n = int(sys.stdin.readline().strip())
    v = [int(x) for x in sys.stdin.readline().strip().split()]
    diff = [v[i+1]-v[i] for i in range(n-1)]
    d = diff[0]
    for i in range(1,len(diff)):
        if diff[i] != d:
            break
    else:
        d = v[n-1]+d
        print(len(diff), d)
        return
    diff = [diff[i+1]-diff[i] for i in range(len(diff)-1)]
    print(len(diff)+1, v[n-1]+d)

if __name__ == '__main__':
    main()
