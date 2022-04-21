
import heapq

def main():
    _, k = map(int, input().split())
    problems = list(map(int, input().split()))
    heapq.heapify(problems)
    cnt = 0
    while problems:
        if problems[0] <= k:
            cnt += 1
            heapq.heappop(problems)
            continue
        if len(problems) == 1:
            break
        if problems[0] > k and problems[-1] <= k:
            heapq.heappop(problems)
            cnt += 1
            continue
        break
    print(cnt)


if __name__ == '__main__':
    main()
