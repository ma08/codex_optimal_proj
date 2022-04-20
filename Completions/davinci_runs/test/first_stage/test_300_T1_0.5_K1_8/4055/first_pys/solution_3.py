

def main():
    # Read input
    n = int(input())
    array = [int(x) for x in input().split()]
    
    # Find the minimum number k
    k = 0
    for i in range(1, n-1):
        if array[i-1] == array[i+1] == 1 and array[i] == 0:
            k += 1
            array[i] = 1
    
    # Print the result
    print(k)

if __name__ == "__main__":
    main()