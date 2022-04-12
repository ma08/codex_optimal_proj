

import sys

def main():
    n = int(sys.stdin.readline().strip())
    balloons = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    balloons.sort()
    balloons.reverse()
    canisters = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    canisters.sort()
    canisters.reverse()
    for i in range(n):
        if balloons[i] > canisters[i]:
            print('impossible')
            return
    print(int(canisters[n-1] // balloons[n-1]))

main()
