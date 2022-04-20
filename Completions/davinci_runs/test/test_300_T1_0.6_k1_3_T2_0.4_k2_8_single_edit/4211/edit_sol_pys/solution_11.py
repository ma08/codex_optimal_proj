

def main():
    n = int(input())
    b = list(map(int, input().split()))
    
    a = [0] * n
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(1, n):
        a[i] = min(b[i-1], a[i-1])
    
    print(sum(a))

if __name__ == '__main__':
    main()
