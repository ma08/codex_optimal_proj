

# cook your dish here
def main():
    for _ in range(int(input())):
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        if k>=max(arr):
            print(k)
            continue
        if k<min(arr):
            print(min(arr))
            continue
        arr.append(k)
        arr.sort(reverse=True)
        print(arr[arr.index(k)+1])
            
if __name__ == '__main__':
    main()
