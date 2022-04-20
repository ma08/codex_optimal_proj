

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    seen = set()
    for i in range(n-1, -1, -1):
        if a[i] in seen:
            a.pop(i)
        else:
            seen.add(a[i])
    
    print(len(a))
    print(*a)

if __name__ == "__main__":
    main()