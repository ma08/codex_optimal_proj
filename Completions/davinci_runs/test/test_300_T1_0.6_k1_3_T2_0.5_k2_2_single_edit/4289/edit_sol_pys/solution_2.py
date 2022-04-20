

n = int(input()) #number of inputs
t, a = map(int, input().split()) #temperature and humidity
h = list(map(int, input().split())) #heights

index = 0 #index of the nearest height
diff = 10000 #difference between the nearest height and the temperature

for i in range(n):
    if abs(a - (t - h[i] * 0.006)) < diff: #if the distance between the nearest height and the temperature is less than the previous one
        diff = abs(a - (t - h[i] * 0.006)) #update the difference
        index = i + 1 #update the index

print(index)
