
def main(n,arr):
    if n==1:
        print(0)
    elif n==2:
        if arr[0]==arr[1]:
            print(0)
        else:
            print(1)
    else:
        d = arr[1] - arr[0]
        ans = 0
        for i in range(2,n-1):
            if arr[i] - arr[i-1] != d or arr[i+1]-arr[i]!=d:
                ans += 1
        return ans
