

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] //= 2
        else:
            a[i] += 1
    if len(set(a)) == 1:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
