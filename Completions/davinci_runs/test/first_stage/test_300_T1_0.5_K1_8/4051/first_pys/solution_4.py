

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        if arr[i] > 1:
            if i == 0:
                if arr[i+1] == arr[i]-1:
                    arr[i+1] += 1
                    arr[i] -= 1
                    break
            elif i == n-1:
                if arr[i-1] == arr[i]-1:
                    arr[i-1] += 1
                    arr[i] -= 1
                    break
            else:
                if arr[i-1] == arr[i]-1:
                    arr[i-1] += 1
                    arr[i] -= 1
                    break
                elif arr[i+1] == arr[i]-1:
                    arr[i+1] += 1
                    arr[i] -= 1
                    break
    if arr == sorted(arr):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()