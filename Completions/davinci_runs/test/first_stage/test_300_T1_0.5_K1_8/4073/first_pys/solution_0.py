

def solve(n, arr):
    arr.sort()
    return arr[-1] - arr[0]

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(n, arr))