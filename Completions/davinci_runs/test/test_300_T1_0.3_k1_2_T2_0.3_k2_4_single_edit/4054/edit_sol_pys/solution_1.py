

def main():
    # Read input
    a = [int(x) for x in input().split()]  # a is a list of integers
    # Compute answer
    ans = 0  # ans is an integer
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            ans += a[i]*a[j]
    # Print answer
    print(ans)

if __name__ == '__main__':
    main()
