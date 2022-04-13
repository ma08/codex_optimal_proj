

arr = input()
arr = arr.split(" ")

for i in range(0,len(arr)):
    arr[i] = int(arr[i])

arr.sort()

#print(message)

count = 1
for i in range(0,len(arr)):
    if arr[i] == arr[i+1]:
        count += 1
    else:
        print(arr[i], end = " ") 
        count = 1
