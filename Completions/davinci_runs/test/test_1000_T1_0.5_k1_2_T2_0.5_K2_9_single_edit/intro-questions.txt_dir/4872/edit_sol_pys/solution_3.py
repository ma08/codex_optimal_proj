
import sys, heapq
def main():
    n = int(sys.stdin.readline())
    tasks = []
    for i in range(n):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        heapq.heappush(tasks, (a, b))
    current_time = 0
    total_time = 0
    while tasks:
        task = heapq.heappop(tasks)
        task_time = task[0]
        task_value = task[1]
        if current_time + task_time <= total_time:
            current_time += task_time
            total_time += task_value
        else:
            current_time = total_time + task_time
            total_time += task_value
    print(total_time)

if __name__ == '__main__':
    main()
