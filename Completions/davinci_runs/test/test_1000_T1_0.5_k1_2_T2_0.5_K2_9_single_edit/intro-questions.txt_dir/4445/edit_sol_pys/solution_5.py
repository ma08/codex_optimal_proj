

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    if n % 2 == 1:
        print(sum(a[n//2+1:]) - sum(a[:n//2]))
    else:
        print(sum(a[n//2:]) - sum(a[:n//2]))

if __name__ == "__main__":
    main()
