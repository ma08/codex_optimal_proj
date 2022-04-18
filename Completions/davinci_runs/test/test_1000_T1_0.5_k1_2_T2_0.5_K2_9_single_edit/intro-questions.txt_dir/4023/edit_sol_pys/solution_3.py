

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            a[i] += 1  
            a[i + 1] += 1
    if len(set(a)) == 1:  
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
