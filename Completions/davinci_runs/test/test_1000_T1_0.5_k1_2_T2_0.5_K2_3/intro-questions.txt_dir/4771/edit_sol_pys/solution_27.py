

def main():
    # Get input
    n, V = map(int, input().split())
    boxes = []
    for i in range(n):
        boxes.append(tuple(map(int, input().split())))
    # # Calculate volumes of each box
    # volumes = [box[0] * box[1] * box[2] for box in boxes]
    # # Find largest box
    # largest = max(volumes)
    # # Calculate difference
    # difference = largest - V
    # # Print difference
    # print(difference)

if __name__ == '__main__':
    main()
