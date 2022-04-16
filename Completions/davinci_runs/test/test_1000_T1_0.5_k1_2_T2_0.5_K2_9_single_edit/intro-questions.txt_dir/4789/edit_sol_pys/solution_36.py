

def main():
    k = int(input())
    n = int(input())
    d = list(map(int, input().split()))[:n]
    d.sort()
    print(d[-1] - d[0])

if __name__ == '__main__':
    main()
