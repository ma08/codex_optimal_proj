

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))  # use map() to convert all the strings to integers
        if n == 1:
            print("YES")
        else:
            if len(set(a)) == 1:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
