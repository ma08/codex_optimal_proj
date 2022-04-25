

def main():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split())) # inputをintに変換
    f.insert(0, 0)

    for i in range(n):
        a[i] = str(f[int(a[i])])

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
