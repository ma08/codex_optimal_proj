
def median(arr):
    if len(arr) % 2 == 0:
        return (arr[int(len(arr)/2)] + arr[int(len(arr)/2)-1])/2
    else:
        return arr[int(len(arr)/2)]

def main():
    n, m = map(int, input().split())  # n is the length of the array, m is the median
    arr = list(map(int, input().split()))  # arr is the array
    count = 0
    for i in range(n):
        for j in range(i, n):  # iterate through the array
            if median(arr[i:j+1]) == m:  # if the median of the subarray is equal to the median, increase the count
                count += 1
    print(count)

if __name__ == "__main__":
    main()
