

def main():
    _ = int(input())
    a = list(map(int, input().split()))
    if min(a) == max(a):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
