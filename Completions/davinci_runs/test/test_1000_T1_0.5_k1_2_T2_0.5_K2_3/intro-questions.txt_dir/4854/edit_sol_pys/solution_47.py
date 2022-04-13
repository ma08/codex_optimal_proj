

arr = input()
arr = arr.split(" ")

for i in range(0,len(arr)):
    arr[i] = int(arr[i])

arr.sort()

#print(message)

count = 1

    if arr[i] == arr[i+1]:
        count += 1
    else:
        print(arr[i], end = " ") #end = " " to print in a single line
        count = 1
