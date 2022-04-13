

import sys

def main():
    n = int(sys.stdin.readline().strip())
    balloons = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    balloons.sort()
    balloons.reverse()
    cannisters = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    cannisters.sort()
    cannisters.reverse()
    for i in range(n):
        if balloons[i] > cannisters[i]:
            print('impossible')
            return
    print(cannisters[n-1] // balloons[n-1])

main()
