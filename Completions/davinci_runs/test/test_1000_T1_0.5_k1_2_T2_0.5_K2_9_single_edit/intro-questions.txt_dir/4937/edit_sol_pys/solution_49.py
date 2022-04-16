


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(e)
    count = 0
    for i in range(n):
        if a[i] == a[i+1]:
            count += 1
            a.remove(a[i])
        else:
            a.remove(a[i])
            break
    print(count)

def main():
    n, a = map(int, sys.stdin.readline().split())
    e = list(map(int, sys.stdin.readline().split()))
    e.sort()
    #print(e)
    count = 0
    for i in range(n):
        if a >= e[i]:
            count += 1
            a -= e[i]
        else:
            break
    print(count)

main()
