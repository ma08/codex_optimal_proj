



def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    p = [0]*n
    p[0] = 1
    for i in range(n):
        p[a[i][0]-1] = a[i][1]
        p[a[i][1]-1] = a[i][0]
    for i in range(n):
        if p[i] == 0:
            p[i] = i+2
    print(*p)

if __name__ == "__main__":
    main()