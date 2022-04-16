import sys

def main():
    n, m = map(int, input().split())
    task_times = list(map(int, input().split()))
    quiet_times = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if task_times[i] <= quiet_times[j]:
                print(j+1)
                break

if __name__ == "__main__":
    main()
