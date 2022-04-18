

def main():
    n = int(input())
    ans = 0
    p = 1
    while p < n:
        p *= 2
        ans += 1
    print(ans + 1)

if __name__ == "__main__":
    main()
