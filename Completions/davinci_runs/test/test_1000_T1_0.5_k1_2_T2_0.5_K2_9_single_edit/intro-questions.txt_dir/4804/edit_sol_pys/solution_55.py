

def main():
    # Read input
    S = int(input())
    
    # Determine star pattern
    print(S,":")
    for x in range(S//2,S+1):
        for y in range(x,x+1):
            if x*y == S:
                print(x,',',y)
    

if __name__ == "__main__":
    main()
