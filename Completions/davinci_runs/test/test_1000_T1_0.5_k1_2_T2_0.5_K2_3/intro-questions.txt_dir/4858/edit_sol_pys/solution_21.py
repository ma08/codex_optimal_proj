

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

    # find the centroid of the falcon in the first frame (x, y)
    cx1 = 0
    cy1 = 0
    for point in falcon1:
        cx1 += point[0]
        cy1 += point[1]
    cx1 = int(cx1/len(falcon1))
    cy1 = int(cy1/len(falcon1))

    # find the centroid of the falcon in the second frame (x, y)
    cx2 = 0
    cy2 = 0
    for point in falcon2:
        cx2 += point[0]
        cy2 += point[1]
    cx2 = int(cx2/len(falcon2))
    cy2 = int(cy2/len(falcon2))

    # find the distance between the centroids
    distance = int(((cx1-cx2)**2 + (cy1-cy2)**2)**0.5)

    # find the direction of the falcon
    direction = [cx2-cx1, cy2-cy1]

    # find the movement of the falcon
    if distance != 0:
        movement = [int(direction[0]/distance), int(direction[1]/distance)]
    else:
        movement = [0, 0]

    # find the new position of the falcon
    cx3 = cx2 + movement[0]
    cy3 = cy2 + movement[1]

    # create the new frame
    frame3 = []
    for i in range(M):
        frame3.append(frame2[i])

    # move the falcon
    for point in falcon2:
        frame3[point[0]][point[1]] = '.'
        if cx3 < M and cy3 < N and cx3 >= 0 and cy3 >= 0:
            frame3[point[0]+movement[0]][point[1]+movement[1]] = C

    for line in frame3:
        print(line)
    print()

if __name__ == '__main__':
    main()
