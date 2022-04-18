
def main():
    # Read the input
    n, v = [int(x) for x in input().split()]
    boxes = []
    for i in range(n):
        boxes.append([int(x) for x in input().split()])
    # Sort the boxes by volume
    boxes.sort(key=lambda box: box[0]*box[1]*box[2])
    # Print the difference between the largest box and the volume required
    print(boxes[0][0]*boxes[0][1]*boxes[0][2]-v)
    
main()
