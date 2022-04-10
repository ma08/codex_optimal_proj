

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n > 1:
        for i in range(n):
            for j in range(n):
                if a[i] == a[j]:
                    a[i], a[j] = a[j], a[i]
                    break
    print('YES')
    for i in range(n):
        print(*a[i*n:(i+1)*n])

main()