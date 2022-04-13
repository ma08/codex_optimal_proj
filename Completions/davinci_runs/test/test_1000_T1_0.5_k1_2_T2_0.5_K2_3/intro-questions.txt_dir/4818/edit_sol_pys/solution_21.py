
    # input
def main():
    n, m = map(int, input().split())
    tasks = sorted(map(int, input().split()), reverse=True)
    breaks = sorted(map(int, input().split()), reverse=True)
    # process
    total = 0
    for i in range(n):
        if total >= m:
            break
        if tasks[i] <= breaks[total]:
            total += 1
    print(total)

main()
