import math



def main():
    num_segments, gravity = map(float, input().split())
    segment_data = []
    for _ in range(int(num_segments)):
        segment_data.append(list(map(float, input().split())))
    segment_data.reverse()
    speeds = []
    segment_data[0].append(0)
    for i in range(1, int(num_segments)):
        segment_data[i].append(segment_data[i-1][2] + (segment_data[i-1][0] * math.tan(math.radians(segment_data[i-1][1]))))  # noqa
    for segment in segment_data:
        speeds.append(math.sqrt(2 * gravity * segment[2]))
    speeds.reverse()
    for speed in speeds:
        print(speed)

main()
