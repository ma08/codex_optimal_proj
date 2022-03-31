

def main():
    n, k = map(int, input().split())
    print("YES")
    for i in range(n):
        print(i%k+1, i%k+1)

if __name__ == "__main__":
    main()