

def main():
    """
    1. Read the first line, which is the length of the array.
    2. Read the second line, which is the array.
    3. For each element in the array, check if it has a subarray sum of zero.
    4. If so, add 1 to the count
    5. Return the count.
    """
    n = int(input())
    array = list(map(int, input().split()))
    count = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)+1):
            if sum(array[i:j]) == 0:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()