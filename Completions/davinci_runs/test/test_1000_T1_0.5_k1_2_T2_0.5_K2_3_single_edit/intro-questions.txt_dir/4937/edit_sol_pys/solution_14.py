

    a = int(input())
def main():
    n, a = map(int, input().split())
    b = list(map(int, input().split()))
    b.sort()
    res = 0
    for i in b:
        if a >= i:
            a -= i
            res += 1
    print(res)

main()
