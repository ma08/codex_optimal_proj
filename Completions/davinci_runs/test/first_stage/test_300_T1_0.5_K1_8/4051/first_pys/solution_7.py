

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) > 1:
            print("NO")
            break
    else:
        print("YES")

main()