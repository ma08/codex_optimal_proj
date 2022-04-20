

def main():
    # Read input
    a = [int(x) for x in input().split() if x != ""]
    # Compute answer
    ans = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            ans += a[i]*a[j]
    # Print answer
    print(ans)

if __name__ == '__main__':
    main()
