

def main():
    n = int(input())
    t = list(map(int, input().split()))
    for i in range(n):
        if i == 0:
            print(t[i])
        elif i == n-1:
            print(t[i])
        else:
            print(max(t[i-1], t[i+1]))

if __name__ == "__main__":
    main()
