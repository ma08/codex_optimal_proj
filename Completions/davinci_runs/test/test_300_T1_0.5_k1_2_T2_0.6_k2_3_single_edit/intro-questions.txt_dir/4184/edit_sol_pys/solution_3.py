

def solve(arr, money):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == money:
                return i + 1, j + 1


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = solve(arr, money)
        print(result)
