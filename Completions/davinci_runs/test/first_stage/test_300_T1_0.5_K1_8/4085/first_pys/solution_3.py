

def find_min(n, arr):
    if n == 1:
        return arr[0] * 2
    for i in range(2, arr[-1]):
        for j in range(len(arr)):
            if i % arr[j] != 0:
                break
            if j == len(arr) - 1:
                return i
    return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(find_min(n, arr))