
import sys

def main():
    # read input and convert to int
    n, m = map(int, input().split())  # n: number of cows, m: number of stalls
    x = list(map(int, input().split()))  # x: list of stall positions

    # sort the coordinates
    x.sort()

    # find the minimum number of moves required to achieve the objective
    ans = 0
    for i in range(m):
        ans += abs(x[i] - x[i-1])
    print(ans)

if __name__ == '__main__':
    main()
