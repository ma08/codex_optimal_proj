

# n: number of stations
# s: number of people who left the train
# e: number of people who entered the train
# w: number of people who had to stay at a station
n = int(input())
s = [int(x) for x in input().split()]
e = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]

C = e[0]

if C < 0 or C > s[0]:
    print("impossible")
    exit(0)

for i in range(1, n):
    C = C + s[i] - e[i]
    if C < 0 or C > s[i]:
        print("impossible")
        exit(0)

print("possible")    
