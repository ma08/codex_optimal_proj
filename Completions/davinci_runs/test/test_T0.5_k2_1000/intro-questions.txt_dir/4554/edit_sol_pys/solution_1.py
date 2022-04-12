

def main():
    # Get input and convert to int
    W, a, b = map(int, input().split()) 
    # Print the distance between the two rectangles
    print(max(0, abs(a-b)-W))

if __name__ == '__main__':
    main()
