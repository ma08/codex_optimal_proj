

def solve():
    n = int(input())
    b = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    if n == 2:
        print(0 if b[0] == b[1] else 1)
        return
    dif = b[1] - b[0]
    for i in range(2, n):
        if dif != (b[i] - b[i-1]):
            if dif == (b[i] - b[i-1] + 1) and (b[i-1] - 1) == b[i-2]:
                b[i-1] -= 1
            elif dif == (b[i] - b[i-1] - 1) and (b[i-1] + 1) == b[i-2]:
                b[i-1] += 1
            else:
                print(-1)
                return
    print(sum(1 for i in range(1, n) if b[i] != b[i-1]))

solve()