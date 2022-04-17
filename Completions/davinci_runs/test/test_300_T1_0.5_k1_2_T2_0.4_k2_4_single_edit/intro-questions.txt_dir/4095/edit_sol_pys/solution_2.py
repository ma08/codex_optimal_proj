

def median(nums):
    return sum(nums) / len(nums)

def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    print(sum([1 for i in range(n) for j in range(i, n) if median(seq[i:j+1]) == m]))

if __name__ == '__main__':
    main()
