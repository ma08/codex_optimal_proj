

def process(n, k, aList):
    if n < k:
        return -1
    else:
        return sum(aList)

def main():
    n, k = [int(x) for x in input().strip().split()]
    aList = [int(x) for x in input().strip().split()]
    result = process(n, k, aList)
    print(result)

if __name__ == "__main__":
    main()
