

def main():
    swathers, stages = [int(x) for x in input().split()] #number of swathers and stages
    times = []
    for i in range(swathers): #input time for each stage
        times.append([int(x) for x in input().split()]) #append to list
    times = sorted(times)
    for i in range(1,len(times)): #add the time for each stage
        for j in range(stages):
            times[i][j] += times[i-1][j]
    for i in range(swathers): #print the total time for each swather
        print(times[i][stages-1], end=' ')

main()
