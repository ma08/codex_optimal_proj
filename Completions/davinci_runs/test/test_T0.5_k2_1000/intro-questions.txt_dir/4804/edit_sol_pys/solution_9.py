

def main():
    # Read input
    S = int(input())
    
    # Determine star patterns
    print(S,":")
    for x in range(S//2,S):
        for y in range(x,x+2):
            if x*y == S:
                print(x,',',y,sep='') # print the two factors
    

if __name__ == "__main__":
    main()
