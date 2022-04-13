

def main():
    n = int(input())
    s = input().split()

    if len(s) != n:
            print("Something is fishy")
    else:
        for i in range(n):
            if s[i] == "mumble":
                continue
            if int(s[i]) != i+1:
                print("Something is fishy")
                break
        else:
            print("Makes sense")

if __name__ == "__main__":
    main()
