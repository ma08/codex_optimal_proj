
from sys import stdin

def main():
    n = int(input())
    times = []
    distances = []
    for i in range(n):
        t, d = map(int, input().split())
        times.append(t)
        distances.append(d)
    max_speed = 0
    for i in range(n-1):
        speed = (distances[i+1]-distances[i])/(times[i+1]-times[i])*3600
        if speed > max_speed:
            max_speed = speed
    print(max_speed)

main()
