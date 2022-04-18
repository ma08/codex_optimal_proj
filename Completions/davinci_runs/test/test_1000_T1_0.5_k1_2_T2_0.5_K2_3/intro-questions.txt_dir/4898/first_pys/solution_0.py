

def main():
    N = int(input())
    minions = []
    for i in range(N):
        minions.append([int(x) for x in input().split()])
    # print(minions)
    minions.sort(key=lambda x: x[1])
    # print(minions)
    ans = 0
    cur = 0
    for m in minions:
        if m[0] > cur:
            ans += 1
            cur = m[1]
    print(ans)

main()