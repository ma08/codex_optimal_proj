
# Enter your code here. Read input from STDIN. Print output to STDOUT




if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    arr = list(arr)
    max = 0
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            max = max + 1
    print(max)
