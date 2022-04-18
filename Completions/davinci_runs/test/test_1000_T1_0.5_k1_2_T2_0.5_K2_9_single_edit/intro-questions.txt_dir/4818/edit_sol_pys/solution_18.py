
import sys

def main():
    n, m = map(int, input().split('\n'))
    task_lens = list(map(int, input().split(' ')))
    quiet_lens = list(map(int, input().split(' ')))

    task_lens.sort()
    quiet_lens.sort()

    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if task_lens[i] <= quiet_lens[j]:
            count += 1
            i += 1
        j += 1

    print(count, end='')

if __name__ == '__main__':
    main()
