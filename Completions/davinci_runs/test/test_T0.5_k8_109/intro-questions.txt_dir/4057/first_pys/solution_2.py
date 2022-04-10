

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    c = 0
    for i in a:
        if i in s:
            c += 1
            s = set()
        s.add(i)
    print(c + 1)

main()