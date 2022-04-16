

def main():
    # Get input
    n, V = map(int, input().split())
    boxes = []
    for i in range(n):
        boxes.append(tuple(map(int, input().split())))
    # Calculate volume of each box and find largest box
    largest = max([box[0] * box[1] * box[2] for box in boxes])
    # Print difference
    print(largest - V)

if __name__ == '__main__':
    main()
