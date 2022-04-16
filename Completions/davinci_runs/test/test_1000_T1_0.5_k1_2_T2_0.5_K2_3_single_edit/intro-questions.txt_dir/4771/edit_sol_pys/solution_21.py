
# Solution
def main():
    # Read the input
    n, v = [int(x) for x in input().split()] # read number of boxes and volume
    boxes = []
    for i in range(n): # read the dimensions of each box
        boxes.append([int(x) for x in input().split()]) # add each box to the list
    # Sort the boxes by volume
    boxes.sort(key=lambda box: box[0]*box[1]*box[2], reverse=True) # sort the list of boxes by volume
    # Print the difference between the largest box and the volume required
    print(boxes[0][0]*boxes[0][1]*boxes[0][2]-v) # print the difference between the largest box and the volume required
    
main()
