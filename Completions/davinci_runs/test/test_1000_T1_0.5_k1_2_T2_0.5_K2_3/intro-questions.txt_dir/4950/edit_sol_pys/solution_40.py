
from sys import stdin

def main():
    n = int(stdin.readline().strip())
    times = [0]
    distances = [0]
    for i in range(n):
        t, d = map(int, stdin.readline().split())
        times.append(t)
        distances.append(d)
    max_speed = 0
    for i in range(n-1):
        speed = (distances[i+1]-distances[i])/(times[i+1]-times[i])
        if speed > max_speed:
            max_speed = speed
    print(max_speed)

main()
