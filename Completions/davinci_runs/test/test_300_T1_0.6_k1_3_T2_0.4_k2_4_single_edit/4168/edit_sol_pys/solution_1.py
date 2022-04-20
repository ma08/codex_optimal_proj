

def main():
    n = int(input())
    ans = ""
    if n == 0:
        ans = "0"

    else:
        while n != 0:
            if n % 2 == 0:
                ans += "0"
                n = n // -2
            else:
                ans += "1"
                n = (n - 1) // -2
        if ans[-1] == "1":
            ans += "1"
        ans = ans[::-1] 

    print(ans)

if __name__ == "__main__":
    main()
