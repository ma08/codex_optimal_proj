

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d = [a[i+1] - a[i] for i in range(n-1)]
    d.append(float('inf'))
    d.sort()
    print(n - d[k-1] + 1)

if __name__ == '__main__':
    main()