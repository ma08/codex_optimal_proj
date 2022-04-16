import sys

def main():
    n, p = [int(x) for x in sys.stdin.readline().split()]
    time = [int(x) for x in sys.stdin.readline().split()]
    time.sort()
    if time[p-1] > 300:
        print("0 0")
        return
    ans = 0
    for i in range(p-1, n):
        if time[i] > 300:
            break
        ans += 1
    print(ans, sum(time[:ans]))

main()
