

#----Solution----

def main():
    n, m = map(int, input().split())
    l = []
    count = 0
    for i in range(n):
        l.append(input())
    for i in range(m):
        if l[0][i] == '_':
            count += 1
    print(count + 1)

main()
