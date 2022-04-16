# Solution

def main():
    n, v = [int(x) for x in input().split()] # Read the input
    boxes = []
    for i in range(n):
        boxes.append([int(x) for x in input().split()])
    boxes.sort(key=lambda box: box[0]*box[1]*box[2], reverse=True) # Sort the boxes by volume
    print(boxes[0][0]*boxes[0][1]*boxes[0][2]-v) # Print the difference between the largest box and the volume required
    
main()
