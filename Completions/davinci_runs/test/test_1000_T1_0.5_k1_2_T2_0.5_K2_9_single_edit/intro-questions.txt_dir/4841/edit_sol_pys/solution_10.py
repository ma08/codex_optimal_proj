

def main():
    n = int(input())
    bites = input().split()
    for i in range(1, n+1):
        if bites[i-1] != 'mumble' and int(bites[i-1]) != i:
            print("something is fishy")
            return
    print("makes sense")

main()
