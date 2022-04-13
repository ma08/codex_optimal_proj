

def main():
    workers, stages = [int(x) for x in input().split()]
    times = []
    for i in range(workers):
        times.append([int(x) for x in input().split()])
    times = sorted(times, key=lambda x: x[0])
    for i in range(1, len(times)):
        for j in range(stages):
            times[i][j] += times[i - 1][j]
    for i in range(workers):
        print(times[i][stages - 1], end=' ')


main()
