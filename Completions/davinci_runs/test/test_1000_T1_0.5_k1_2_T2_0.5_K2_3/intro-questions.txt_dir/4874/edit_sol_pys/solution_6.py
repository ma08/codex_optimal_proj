
#----Solution----#

def main():
    n, m = map(int, input().split())
    li = []
    count = 0
    for i in range(n):
        li.append(input())
    for i in range(m):
        if li[0][i] == '_':
            count += 1
    print(count)
main()
