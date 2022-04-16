
def main():
    n, p = [int(x) for x in input().split()]
    time = [int(x) for x in input().split()]
    time.sort()
    if time[p] > 300:
        print("0 0")
        return
    ans = 0
    for i in range(p, n):
        if time[i] > 300:
            break
        ans += 1
    print(ans, sum(time[:ans]))


main()
