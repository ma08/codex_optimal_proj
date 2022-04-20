

def main():
    n,r = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1])
    for i in a:
        if r < i[0]:
            print("NO")
            return
        r += i[1]
    print("YES")

if __name__ == '__main__':
    main()