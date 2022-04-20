

def ravioli_sort(arr):
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) == 1:
            return "NO"
    return "YES" if len(arr) > 1 else "NO"

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(ravioli_sort(arr))

if __name__ == "__main__":
    main()
