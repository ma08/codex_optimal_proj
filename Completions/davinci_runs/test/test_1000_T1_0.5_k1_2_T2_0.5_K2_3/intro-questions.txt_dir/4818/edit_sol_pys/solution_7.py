# this is the file

def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    intervals = list(map(int, input().split()))[::-1]
    # print(tasks)
    # print(intervals)
    tasks.sort(reverse=True)
    # print(tasks)
    total = 0
    # print(tasks)
    # print(intervals)
    for i in range(n):
        # print(total)
        if total >= m:
            break
        if tasks[i] <= intervals[total]:
            total += 1
            # print(total)
    print(total)

main()
