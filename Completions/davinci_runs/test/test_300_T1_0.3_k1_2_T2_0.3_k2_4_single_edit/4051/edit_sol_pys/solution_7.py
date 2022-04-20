

def ravioli_sort(arr):
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) > 1:
            return False
    return True

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    if ravioli_sort(arr):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
