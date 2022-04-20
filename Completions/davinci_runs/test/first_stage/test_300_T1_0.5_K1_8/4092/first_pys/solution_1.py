

def main():

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    suma = 0
    s = set()

    for i in range(n):
        suma += a[i]
        if suma == 0:
            ans += 1
            suma = 1
        elif suma in s:
            ans += 1
            suma = 1
            s.clear()
        s.add(suma)
    print(ans)

if __name__ == '__main__':
    main()