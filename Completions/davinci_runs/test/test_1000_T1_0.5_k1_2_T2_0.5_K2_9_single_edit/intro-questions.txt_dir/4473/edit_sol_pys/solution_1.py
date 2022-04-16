

# cook your dish here\


def solve(arr):
    for i in range(len(arr)):
        if arr[i] != i+1:
            return i+1
    return len(arr)+1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))
