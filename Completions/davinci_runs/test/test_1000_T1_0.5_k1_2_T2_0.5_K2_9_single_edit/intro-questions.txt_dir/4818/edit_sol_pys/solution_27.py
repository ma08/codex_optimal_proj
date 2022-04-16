

def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    intervals = list(map(int, input().split()))
    tasks.sort()
    intervals.sort()

    print(tasks)


if __name__ == '__main__':
    main()
