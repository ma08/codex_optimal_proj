

def main():
    # Get input
    n, V = map(int, input().split())
    boxes = []
    for i in range(n):
        boxes.append(tuple(map(int, input().split())))
    # Sort boxes by volume
    boxes.sort(key=lambda x: x[0] * x[1] * x[2])
    # Find first box that is larger than V
    for box in boxes:
        if box[0] * box[1] * box[2] > V:
            # Calculate difference
            difference = box[0] * box[1] * box[2] - V
            # Print difference
            print(difference)
            break

if __name__ == '__main__':
    main()
