

def main():
    numSegments, gravity = map(float, input().split())
    segmentData = []
    for _ in range(int(numSegments)):
        segmentData.append(list(map(float, input().split())))
    segmentData.reverse()
    speeds = []
    segmentData[0].append(0)
    for i in range(1, int(numSegments)):
        segmentData[i].append(segmentData[i-1][2] + (segmentData[i-1][0] * math.tan(math.radians(segmentData[i-1][1])) * 2))
    for segment in segmentData:
        speeds.append(math.sqrt(2 * gravity * segment[2]))
    speeds.reverse()
    for speed in speeds:
        print(speed)

main()
