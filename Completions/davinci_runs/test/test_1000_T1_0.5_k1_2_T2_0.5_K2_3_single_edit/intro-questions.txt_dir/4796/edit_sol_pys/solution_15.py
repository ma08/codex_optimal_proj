

def main():
    # Get the input and do some preprocessing
    a, b, c = map(int, input().split())
    # Compute the answer
    answer = (a + b + c) // 3
    # Output the results 
    print(answer)

if __name__ == '__main__':
    main()
