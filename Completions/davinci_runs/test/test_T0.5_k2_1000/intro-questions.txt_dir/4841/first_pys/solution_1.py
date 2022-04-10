

def main():
    n = int(input())
    bites = input().split()
    for i in range(n):
        if bites[i] != 'mumble' and int(bites[i]) != i+1:
            print("something is fishy")
            return
    print("makes sense")

main()