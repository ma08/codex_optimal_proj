

def main():
    swathers, stages = [int(x) for x in input().split()]
    times = []
    for i in range(swathers):
        times.append([int(x) for x in input().split()])
    times = sorted(times)
    for i in range(1,len(times)):
        for j in range(stages):
            times[i][j] += times[i-1][j]
    for i in range(swathers):
        print(times[i][stages-1], end=' ')

main()