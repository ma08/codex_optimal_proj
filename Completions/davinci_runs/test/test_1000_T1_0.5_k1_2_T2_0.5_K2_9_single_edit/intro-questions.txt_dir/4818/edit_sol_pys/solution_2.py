

def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))[:n]
    intervals = list(map(int, input().split()))[:m]
    tasks.sort()
    intervals.sort()
    total = 0
    for i in range(n):
        if total >= m:
            break
        if tasks[i] <= intervals[total]:
            total += 1
    print(total)

main()
