

def main():
    M, N, C = input().split()
    M = int(M)
    N = int(N)

    frame1 = []
    frame2 = []
    for i in range(M):
        frame1.append(input())
    input()
    for i in range(M):
        frame2.append(input())

    #print(frame1)
    #print(frame2)

    # find the falcon in the first frame
    falcon1 = []
    for i in range(M):
        for j in range(N):
            if frame1[i][j] == C:
                falcon1.append((i, j))

    # find the falcon in the second frame
    falcon2 = []
    for i in range(M):
        for j in range(N):
            if frame2[i][j] == C:
                falcon2.append((i, j))

    # find the centroid of the falcon in the first frame
    cx1 = 0
    cy1 = 0
    for point in falcon1:
        cx1 += point[0]
        cy1 += point[1]
    cx1 = int(cx1/len(falcon1))
    cy1 = int(cy1/len(falcon1))
    #print(cx1, cy1)

    # find the centroid of the falcon in the second frame
    cx2 = 0
    cy2 = 0
    for point in falcon2:
        cx2 += point[0]
        cy2 += point[1]
    cx2 = int(cx2/len(falcon2))
    cy2 = int(cy2/len(falcon2))
    #print(cx2, cy2)

    # find the distance between the centroids
    distance = ((cx1-cx2)**2 + (cy1-cy2)**2)**0.5
    #print(distance)

    # find the direction of the falcon
    direction = [cx2-cx1, cy2-cy1]
    #print(direction)

    # find the movement of the falcon
    movement = [int(direction[0]/distance), int(direction[1]/distance)]
    #print(movement)

    # find the new position of the falcon
    cx3 = cx2 + movement[0]
    cy3 = cy2 + movement[1]
    #print(cx3, cy3)

    # create the new frame
    frame3 = []
    for i in range(M):
        frame3.append(frame2[i])
    for point in falcon2:

    # move the falcon
    for point in falcon2:
        frame3[point[0]][point[1]] = '.'
        frame3[point[0]+movement[0]][point[1]+movement[1]] = C

    #print(frame3)
    for line in frame3:
        print(line)
    print()

if __name__ == '__main__':
    main()
