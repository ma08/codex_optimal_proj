

def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    breaks = list(map(int, input().split()))
    tasks.sort(reverse=True)
    breaks.sort(reverse=True)
    total = 0
    for i in range(n):
        if total >= m:
            break
        if tasks[i] <= breaks[total]:
            total += 1
    print(total)

if __name__ == '__main__':
    main()
