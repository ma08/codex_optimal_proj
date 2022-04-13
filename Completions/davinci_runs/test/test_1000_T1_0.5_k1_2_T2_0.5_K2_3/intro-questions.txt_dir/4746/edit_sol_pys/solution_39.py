

C, n = [int(x) for x in input().split()]

for i in range(n):
    s, e, w = [int(x) for x in input().split()]
    if i == 0:
        #first station
        if s > 0 or e > C or w > C or (w > 0 and e > 0):
            print("impossible")
            exit(0)
        else:
            C -= e
            continue
    elif i == n-1:
        #last station
        if s > C or e > 0 or w > 0:
            print("impossible")
            exit(0)
        else:
            C += s
            continue
    else:
        #middle station
        if s > C or e > C or w > C or (w > 0 and e > 0):
            print("impossible")
            exit(0)
        else:
            C += s
            C -= e
            continue

print("possible")
