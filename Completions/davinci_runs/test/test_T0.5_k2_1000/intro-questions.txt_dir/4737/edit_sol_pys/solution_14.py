
def main():
    n, p = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    times.sort()
    if times[p] > 300:
        print("0 0")
        return
    ans = 0
    for i in range(p, n):
        if times[i] > 300:
            break
        ans += 1
    print(ans, sum(times[:ans]))

main()
