def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))  # map is used to convert the list of strings to list of integers
        if n == 1:
            print("YES")
        else:
            if len(set(a)) == 1:  # set is used to remove duplicates from the list
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
