

def process(n, k, x, aList):
    if x < n - k + 1 or x > n:
        return -1
    else:
        return sum(aList)

def main():
    n, k, x = [int(x) for x in input().strip().split()]
    aList = [int(x) for x in input().strip().split()]
    result = process(n, k, x, aList)
    print(result)

if __name__ == "__main__":
    main()
