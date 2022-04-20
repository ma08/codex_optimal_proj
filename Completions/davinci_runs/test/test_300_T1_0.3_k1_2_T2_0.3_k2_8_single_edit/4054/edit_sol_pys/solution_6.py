

def main():
    # Read input
    a = [int(x) for x in input().split()]  # Read input
    # Compute answer
    ans = 0  # Initialize answer
    for i in range(len(a)):  # Loop over i
        for j in range(i+1, len(a)):  # Loop over j
            ans += a[i]*a[j]  # Update answer
    # Print answer
    print(ans)  # Print answer

if __name__ == '__main__':
    main()
