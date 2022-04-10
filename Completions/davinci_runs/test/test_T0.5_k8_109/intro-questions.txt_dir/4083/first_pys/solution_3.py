

def main():
    """
    The idea is to add up all the numbers. If the sum is divisible by k, then the answer is 0.
    Otherwise, if the sum is not divisible by k, then the answer is -1.
    """
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    if s % k == 0:
        print(0)
    else:
        print(-1)

if __name__ == '__main__':
    main()