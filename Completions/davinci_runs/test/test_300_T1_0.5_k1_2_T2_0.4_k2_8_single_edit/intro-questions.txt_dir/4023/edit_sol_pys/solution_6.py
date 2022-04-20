

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        if a[i] == a[i+1]:
            a[i] += 1
            a[i+1] += 1
    if a.count(a[0]) == n:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
