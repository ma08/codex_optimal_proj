

def main():
    # Read input
    a = [int(x) for x in input().split()]  # a is a list of integers
    # Compute answer
    ans = 0  # ans is an integer
    for i in range(len(a)):  # i is an integer
        for j in range(i+1, len(a)):  # j is an integer
            ans += a[i]*a[j]  # ans is an integer
    # Print answer
    print(ans)

if __name__ == '__main__':
    main()
