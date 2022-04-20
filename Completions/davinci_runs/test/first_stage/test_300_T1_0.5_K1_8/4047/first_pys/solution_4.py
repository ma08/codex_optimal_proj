

n = int(input())
chips = list(map(int, input().split()))

# print(chips)

ans = 0

if (n == 1):
    print(0)
else:
    chips.sort()
    # print(chips)
    mid = chips[n//2]
    # print(mid)

    for i in range(n):
        ans += abs(chips[i] - mid)

    print(ans)