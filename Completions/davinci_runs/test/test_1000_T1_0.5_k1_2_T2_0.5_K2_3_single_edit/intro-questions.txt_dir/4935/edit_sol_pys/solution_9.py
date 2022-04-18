import math


def main():
    numSegments, gravity = map(float, input().split())  # Read in number of segments and gravity
    segmentData = []  # Create segment data array
    for _ in range(int(numSegments)):  # Read in segment data
        segmentData.append(list(map(float, input().split())))  # Add segment data to array
    segmentData.reverse()  # Reverse segment data array
    speeds = []  # Create speeds array
    segmentData[0].append(0)  # Set height of first segment to 0
    for i in range(1, int(numSegments)):  # Calculate height of all other segments
        segmentData[i].append(segmentData[i-1][2] + (segmentData[i-1][0] * math.tan(math.radians(segmentData[i-1][1]))))  # Calculate height of segment
    for segment in segmentData:  # Calculate speeds
        speeds.append(math.sqrt(2 * gravity * segment[2]))  # Calculate speed of segment
    speeds.reverse()  # Reverse speeds array
    for speed in speeds:  # Print speeds
        print(speed)  # Print speed

main()
