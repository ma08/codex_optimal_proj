

arr = input()
arr = arr.split(" ")

for i in range(0,len(arr)):
    arr[i] = int(arr[i])

arr.sort()
print(arr)
#print(message)

count = 1

    if arr[i] == arr[i+1]:
        count += 1
    else:
        print(arr[i], end = " ")
