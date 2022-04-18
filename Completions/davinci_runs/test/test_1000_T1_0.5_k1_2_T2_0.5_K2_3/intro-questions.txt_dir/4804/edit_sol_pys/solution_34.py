

def main():
    # Read input
    S = int(input())
    
    # Determine star patterns
    print(S,":")
    for x in range(2,S):
        if S%(x*2) == 0:
            print(x,',',x,sep='')
        elif S%(x*2-1) == 0:
            print(x,',',x-1,sep='')
    

if __name__ == "__main__":
    main()
