
import sys, heapq

def main():
    n, k = sys.stdin.readline().strip().split()
    n = int(n)
    k = int(k)
    nums = [int(x) for x in sys.stdin.readline().strip().split()][::-1]
    heapq.heapify(nums)
    answer = -1
    while k > 0:
        answer += 1
        while nums and nums[0] <= answer:
            heapq.heappop(nums)
            k -= 1
        if k == 0:
            break
    else:
            print(answer)
    if k > 0:
        print(-1)

if __name__ == "__main__":
    main()
