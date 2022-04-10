
def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        l = []
        for j in range(n):
            a = input().split()
            b = input().split()
            l.append(a + b)
        l.sort()
        x = 0
        flag = False
        while x < n:
            if l[x][0] == l[x][2] and l[x][1] == l[x][3]:
                flag = True
                break
            x += 1
        if flag:
            print("YES") 
        else:
            print("NO")
if __name__ == '__main__':
    main()
