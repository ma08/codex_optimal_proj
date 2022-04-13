

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    ans = True
    for i in range(n):
        if a[i] + b[i] < k:
            ans = False
            break
    print("Yay!" if ans else ":(" ) 

if __name__ == "__main__":
    main()
