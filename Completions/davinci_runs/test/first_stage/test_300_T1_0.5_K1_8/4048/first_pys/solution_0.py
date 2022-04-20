

def main():
    N = int(input())
    ans = 0
    while N > 0:
        ans += 1
        if N & 1:
            N -= 1
        else:
            N //= 2
    print(ans)

if __name__ == "__main__":
    main()