


def main():
    n = int(input())
    ans = ""
    if n == 0:
        ans = "0"
    else:
        while n != 0:
            if n % 2 == 0:
                ans = "0" + ans
                n = n // (-2)
            else:
                ans = "1" + ans
                n = (n - 1) // (-2)
        ans = ans[1:] if ans[0] == "0" else ans
    print(ans)


if __name__ == "__main__":
    main()