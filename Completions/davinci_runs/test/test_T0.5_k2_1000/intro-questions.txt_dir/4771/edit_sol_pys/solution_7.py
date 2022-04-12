

def main():
    # Get input
    n, v = map(int, input().split())
    boxes = []
    for i in range(n):
        boxes.append(tuple(map(int, input().split())))
    # Calculate the volume of each box
    volumes = []
    for box in boxes:
        volumes.append(box[0] * box[1] * box[2])
    # Find largest box
    largest = max(volumes)
    # Calculate difference
    difference = largest - v
    # Print difference
    print(difference)

if __name__ == '__main__':
    main()
