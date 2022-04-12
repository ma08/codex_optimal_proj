
def main():
    n = int(input())
    bites = list(map(int, input().split()))
    for i in range(n):
        if bites[i] != i+1:
            print("something is fishy")
            return
    print("makes sense")

main()
