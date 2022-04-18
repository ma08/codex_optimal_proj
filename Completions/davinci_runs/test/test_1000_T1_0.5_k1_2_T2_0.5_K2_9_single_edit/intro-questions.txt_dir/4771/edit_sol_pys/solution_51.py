
def main():
    n = int(input())
    for i in range(n):
        l = input().split()
        if int(l[0]) > int(l[1]):
            print("Yes")
        else:
            print("No")




if __name__ == "__main__":
    main()
