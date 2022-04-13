# this is the file

def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    intervals = [0] + list(map(int, input().split()))
    tasks.sort(reverse=True)
    intervals.sort()
    total = 1
    for i in range(n):
        if total >= m:
            break
        if tasks[i] <= intervals[total] - intervals[total - 1]:
            total += 1
    print(total)

main()
