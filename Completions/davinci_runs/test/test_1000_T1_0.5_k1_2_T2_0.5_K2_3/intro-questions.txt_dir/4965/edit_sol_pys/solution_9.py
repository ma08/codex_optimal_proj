

n = int(input())
temps = list(map(int,input().split()))

# sort the temperatures
temps.sort()

if n==1:
    print(*temps)
else:
    # check if the temperature differences are increasing
    inc = True
    for i in range(1,n-1):
        if abs(temps[i-1]-temps[i]) > abs(temps[i]-temps[i+1]):
            inc = False
            break

    if inc:
        print(*temps)
    else:
        print("impossible")
