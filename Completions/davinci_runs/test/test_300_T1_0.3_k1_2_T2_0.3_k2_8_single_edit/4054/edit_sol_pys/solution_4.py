

def main():
    # Read input
    a = [int(x) for x in input().split()] # a = [1,2,3]
    # Compute answer
    ans = 0 # ans = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            ans += a[i]*a[j] # ans = 1*2 + 1*3 + 2*3
    # Print answer
    print(ans)

if __name__ == '__main__':
    main()
