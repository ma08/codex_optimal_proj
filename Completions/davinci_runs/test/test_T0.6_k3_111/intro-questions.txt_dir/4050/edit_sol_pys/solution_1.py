

def find_sub_arrays(arr, s):
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == s:
                print(arr[i:j+1])


find_sub_arrays([3, 4, -7, 1, 3, 3, 1, -4], 7)
