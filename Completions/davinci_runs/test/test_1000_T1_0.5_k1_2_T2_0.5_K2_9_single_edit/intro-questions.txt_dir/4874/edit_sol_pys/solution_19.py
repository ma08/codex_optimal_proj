
#----Solution----

def main():
    n, m = map(int, input().split())
    l = []
    count = 0
    for i in range(n):
        l.append(input())
    for i in range(n):
        for j in range(m):
            if l[i][j] == '_':
                count += 1
    print(count)

main()
