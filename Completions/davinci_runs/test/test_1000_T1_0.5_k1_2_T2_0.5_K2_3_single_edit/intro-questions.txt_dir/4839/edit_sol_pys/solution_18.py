

import sys

def main():
    n = int(input())
    canisters = list(map(int, input().split()))
    canisters.sort()
    balloons = list(range(n, 0, -1))
    balloons.sort()
    balloon_sum = sum(balloons)
    canister_sum = sum(canisters)
    if canister_sum < balloon_sum:
        print('impossible')
        return
    i = 0
    j = 0
    while i < n and j < n:
        if canisters[i] >= balloons[j]:
            balloon_sum -= balloons[j]
            canister_sum -= canisters[i]
            i += 1
            j += 1
        else:
            canister_sum -= canisters[i]
            i += 1
    if canister_sum >= balloon_sum:
        print(balloon_sum / sum(balloons))
    else:
        print('impossible')

if __name__ == "__main__":
    main()
