

def main():
    n = int(input())
    bites = input().split()  # bites is a list of strings 
    for i in range(n):
        if bites[i] != 'mumble' and int(bites[i]) != i+1:  # bites[i] is a string
            print("something is fishy")
            return
    print("makes sense")

main()
