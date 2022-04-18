def main():
    t = list(map(int,input().split()))
    s = list(map(int,input().split()))
    t.sort()
    s.sort()
    if t == s:
        print("array are identical")
    else:
        print("array are not identical")



if __name__ == "__main__":
    main()
