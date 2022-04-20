

def main():
    n = int(input())
    for i in range(n):
        s = input()
        if len(s) == len(set(s)) and len(set(s)) == max(map(ord,s))-min(map(ord,s))+1:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()