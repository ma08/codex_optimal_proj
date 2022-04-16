

def main():
    N = int(input())
    minions = []
    for i in range(N):
        minions.append([int(x) for x in input().split()])
    # print(minions)
    minions.sort(key=lambda x: x[1])  # sort by end time
    # print(minions)
    ans = 0
    cur = 0  # current end time
    for m in minions:  # for each minion
        if m[0] > cur:
            ans += 1
            cur = m[1]
    print(ans)

main()
