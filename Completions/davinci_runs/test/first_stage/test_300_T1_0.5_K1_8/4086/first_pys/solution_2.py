

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for i in range(n-1, -1, -1):
        if a[i] in s:
            a.pop(i)
        else:
            s.add(a[i])
    print(len(a))
    print(*a)

main()