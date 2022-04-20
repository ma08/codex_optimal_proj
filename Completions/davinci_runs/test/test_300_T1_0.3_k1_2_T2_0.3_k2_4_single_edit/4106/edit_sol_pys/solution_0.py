

def main():
    n = int(input())
    a = list(map(int, input().split()))[::-1]
    b = [0]*n
    for i in range(n):
        if i == 0:
            b[i] = a[i]
        else:
            b[i] = b[i-1]+a[i]
    print(sum(b))

main()
