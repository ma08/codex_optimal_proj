

#----Solution----

def main():
    n, m = map(int, input().split())
    l = [0]*n
    count = 0
    for i in range(n):
        l[i] = input()
    for i in range(m):
        if l[0][i] == '_':
            count += 1
    print(count)

main()
