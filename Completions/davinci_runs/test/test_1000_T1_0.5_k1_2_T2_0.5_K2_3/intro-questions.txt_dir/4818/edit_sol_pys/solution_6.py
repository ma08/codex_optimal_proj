

def main():
    n, m = map(int, input().split(' '))
    task_lengths = list(map(int, input().split(' ')))
    quiet_lengths = list(map(int, input().split(' ')))

    task_lengths.sort()
    quiet_lengths.sort()

    i = 0
    j = 0
    count = 0
    while i < len(task_lengths) and j < len(quiet_lengths):
        if task_lengths[i] <= quiet_lengths[j]:
            count += 1
            i += 1
        j += 1

    print(count)

if __name__ == '__main__':
    main()
