

def find_subarrays(arr):
    for i in range(len(arr)):
        
        for j in range(i, len(arr)):
            print(arr[i:j+1])