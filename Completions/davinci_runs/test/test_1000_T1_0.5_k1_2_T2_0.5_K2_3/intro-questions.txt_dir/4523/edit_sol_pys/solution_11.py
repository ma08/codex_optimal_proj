
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # if n == 1:
        #     print("YES")
        # else:
        #     if len(set(a)) == 1:
        #         print("YES")
        #     else:
        #         print("NO")
        print(a)

if __name__ == "__main__":
    main()
