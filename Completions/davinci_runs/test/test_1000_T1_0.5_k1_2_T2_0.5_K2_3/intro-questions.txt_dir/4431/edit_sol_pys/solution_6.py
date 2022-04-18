

def main():
    # input n,k
    n,k = map(int,input().split())
    # input k
    s = input()
    k = input().split()
    # initialise count
    c = 0
    for i in range(n):
        for j in range(i+1,n+1):
            # check if characters in substring are present in k
            if set(s[i:j])<=set(k):
                c+=1
    print(c)

if __name__ == "__main__":
    main()
