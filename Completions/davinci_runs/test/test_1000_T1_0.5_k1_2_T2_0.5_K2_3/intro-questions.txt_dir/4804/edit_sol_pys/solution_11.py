

def main():
    # Read input
    S = int(input())
    
    # Determine star patterns
    print(S,":")
    for x in range(S//2,S+1):
        for y in range(x,S+1):
            if x*y == S:
                print(x,',',y,sep='')
    

if __name__ == "__main__":
    main()
