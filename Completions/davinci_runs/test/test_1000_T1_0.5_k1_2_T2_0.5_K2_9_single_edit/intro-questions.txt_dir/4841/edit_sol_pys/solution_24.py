
def main():
    n = int(input())
    a = input().split()
    
    for i in range(n):
        if a[i] != "mumble" and int(a[i]) != i+1:
            print("something is fishy")
            exit()
    
    print("makes sense")
if __name__ == "__main__":
    main()
