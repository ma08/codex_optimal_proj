
def main():
    # get input
    n, V = map(int, input().split())
    boxes = []
    for i in range(n):
        boxes.append(tuple(map(int, input().split())))
    # calculate volumes of each box
    volumes = [box[0] * box[1] * box[2] for box in boxes]
    # find largest box
    largest = max(volumes)
    # calculate difference
    difference = largest - V
    # print difference
    print(difference)

if __name__ == '__main__':
    main()
