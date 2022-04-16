

def main():
    """Sock Paring."""
    n = int(input())
    data = list(map(int, input().split()))
    count = [0 for _ in range(10000)]
    for i in data:
        count[i] += 1
    sum_ = 0
    for i in count:
        if i % 2 != 0:
            sum_ += 1
    if sum_ > 2:
        print("impossible")
    else:
        print(n - sum_)

main()
