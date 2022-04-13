

    # input n and k
def main():
    # input string
    n,k = map(int,input().split())
    # input k
    s = input()
    # initialise count
    s = input().split()
    # loop for substrings
    c = 0
    for i in range(n):
            # check if characters in substring are present in k
        for j in range(i+1,n+1):
                # increase count
            if set(s[i:j])<=set(k):
                c+=1
    print(c)

if __name__ == "__main__":
    main()
