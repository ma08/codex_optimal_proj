import sys

def main():
    N = int(sys.stdin.readline())
    minions = []
    for i in range(N):
        minions.append([int(x) for x in sys.stdin.readline().split()])
    minions.sort(key=lambda x: x[1])
    ans = 0
    cur = 0
    for m in minions:
        if m[0] > cur:
            ans += 1
            cur = m[1]
    sys.stdout.write(str(ans))

main()
