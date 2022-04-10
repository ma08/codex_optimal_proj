

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = r = 0
    res = ""
    while l < n and r < n:
        if a[l] < a[r]:
            res += "L"
            l += 1
        else:
            res += "R"
            r += 1
    print(len(res))
    print(res)

if __name__ == "__main__":
    main()