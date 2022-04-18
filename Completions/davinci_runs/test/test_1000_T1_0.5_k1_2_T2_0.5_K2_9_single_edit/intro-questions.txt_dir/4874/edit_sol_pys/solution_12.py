

#----Solution----

def main():
    n, m = map(int, input().split()) # n is no. of rows, m is no. of columns
    l = []
    count = 0 # count is no. of columns with '_'
    for i in range(n):
        l.append(input())
    for i in range(m):
        if l[0][i] == '_':
            count += 1
    print(count)

main()
