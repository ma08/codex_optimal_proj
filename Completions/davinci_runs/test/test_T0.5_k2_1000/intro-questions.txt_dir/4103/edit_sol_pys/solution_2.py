

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0 
    for i in range(n):
        if i > 0 and a[i] == b[i] - 1:
            ans += c[b[i] - 1]
    print(ans)  

if __name__ == "__main__":
    main()
