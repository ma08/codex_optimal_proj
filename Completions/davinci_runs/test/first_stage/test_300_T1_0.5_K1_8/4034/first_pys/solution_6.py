

def main():
    n = int(input())
    s = input()

    if s == ''.join(sorted(s)):
        print("YES")
        print("0" * n)
    else:
        print("YES")
        print("1" * n)

if __name__ == "__main__":
    main()