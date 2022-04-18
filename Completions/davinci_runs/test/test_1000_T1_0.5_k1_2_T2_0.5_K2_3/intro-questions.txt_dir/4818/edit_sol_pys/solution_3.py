

def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    intervals = list(map(int, input().split()))
    tasks.sort(reverse=True)
    intervals.sort(reverse=True)
    total = 0
    for j in range(n):
        if total < m and tasks[j] <= intervals[total]:
            total += 1
    print(total)

main()
