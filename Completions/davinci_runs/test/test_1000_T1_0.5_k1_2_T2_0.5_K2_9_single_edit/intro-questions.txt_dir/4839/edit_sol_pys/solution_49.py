

def main():
    n = int(input())
    balloons = [int(x) for x in input().split(' ')]
    balloons.sort()
    balloons.reverse()
    canisters = [int(x) for x in input().split(' ')]
    canisters.sort()
    canisters.reverse()
    for i in range(n):
        if balloons[i] > canisters[i]:
            print('impossible')
            return
    print(canisters[n-1] / balloons[n-1])

if __name__ == '__main__':
    main()
