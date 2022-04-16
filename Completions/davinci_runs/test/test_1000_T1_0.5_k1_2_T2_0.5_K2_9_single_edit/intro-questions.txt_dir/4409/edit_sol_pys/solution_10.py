# cook your dish here
n=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(0,n):
    if i==0:
        if arr[i]>arr[i+1]:
            arr[i]=arr[i]-arr[i+1]
            count+=1
            print(2,i+1,i+2)
    elif i==n-1:
        if arr[i]>arr[i-1]:
            arr[i]=arr[i]-arr[i-1]
            count+=1
            print(2,i+1,i)
    else:
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            arr[i]=arr[i]-max(arr[i-1],arr[i+1])
            count+=1
            if arr[i-1]>arr[i+1]:
                print(2,i+1,i)
            else:
                print(2,i+1,i+2)
        elif arr[i]<arr[i+1] and arr[i]<arr[i-1]:
            arr[i]=arr[i]+max(arr[i-1],arr[i+1])
            count+=1
            if arr[i-1]>arr[i+1]:
                print(1,i+1,i)
            else:
                print(1,i+1,i+2)
        elif arr[i]>arr[i-1]:
            arr[i]=arr[i]-arr[i-1]
            count+=1
            print(2,i+1,i)
        elif arr[i]>arr[i+1]:
            arr[i]=arr[i]-arr[i+1]
            count+=1
            print(2,i+1,i+2)
        elif arr[i]<arr[i-1]:
            arr[i]=arr[i]+arr[i-1]
            count+=1
            print(1,i+1,i)
        elif arr[i]<arr[i+1]:
            arr[i]=arr[i]+arr[i+1]
            count+=1
            print(1,i+1,i+2)
print(count)
