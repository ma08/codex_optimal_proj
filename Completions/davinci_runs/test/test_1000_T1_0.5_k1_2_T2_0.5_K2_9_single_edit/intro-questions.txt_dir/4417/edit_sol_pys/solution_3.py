

# cook your dish here
def main():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        arr = list(map(int,input().split()))
        arr.sort()
        flag = True 
        for i in range(1,n):
            if abs(arr[i]-arr[i-1])>k:
                flag = False
                break
        if flag:
            print(arr[n//2])
        else:
            print(-1)
            
if __name__ == '__main__':
    main()
