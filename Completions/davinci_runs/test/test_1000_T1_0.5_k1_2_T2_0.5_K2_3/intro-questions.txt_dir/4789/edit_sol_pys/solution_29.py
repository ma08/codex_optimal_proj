import sys

def main():
    N, K = [int(x) for x in sys.stdin.readline().strip().split()]
    desks = sorted([int(x) for x in sys.stdin.readline().strip().split()])

    count = 0
    for i in range(N):
        count += 1
        if desks[i] < i+1:
            count += i - desks[i]
    print(count)

main()
