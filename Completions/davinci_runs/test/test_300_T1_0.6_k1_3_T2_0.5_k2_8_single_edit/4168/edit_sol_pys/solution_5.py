

def main():
    n = int(input())
    ans = []
    if n == 0:
        ans.append("0")

    else:
        while n != 0:
            if n % 2 == 0:
                ans.append("0")
                n = n // -2
            else:
                ans.append("1")
                n = (n - 1) // -2
        if ans[0] == "1":
            ans.append("1")
        ans.reverse()

    print(ans)

if __name__ == "__main__":
    main()
