



def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y, h = map(int, input().split())
        points.append([x, y, h])

    for Cx in range(101):
        for Cy in range(101):
            H = 0
            for i in range(N):
                H = max(H, abs(points[i][0]-Cx)+abs(points[i][1]-Cy)+points[i][2])
            if all(abs(points[i][0]-Cx)+abs(points[i][1]-Cy)+H==points[i][2] for i in range(N)):
                print(Cx, Cy, H)
                break

if __name__ == '__main__':
    main()