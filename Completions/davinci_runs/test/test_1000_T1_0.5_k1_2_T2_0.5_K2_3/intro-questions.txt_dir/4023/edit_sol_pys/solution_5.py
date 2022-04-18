

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == a[i + 1]:
            a[i] = a[i] + 1
            a[i + 1] = a[i + 1] + 1
    if len(set(a)) == 1 and a[0] != 0 and a[n-1] != 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
