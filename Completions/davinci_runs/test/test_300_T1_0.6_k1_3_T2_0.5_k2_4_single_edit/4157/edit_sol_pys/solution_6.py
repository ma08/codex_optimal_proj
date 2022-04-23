

def solve(arr):
    pass
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if not solve(arr):
        arr.reverse()
        if not solve(arr):
            print("No")
            return
    print(*arr)

if __name__ == '__main__':
    main()
