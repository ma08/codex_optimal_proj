

n = int(input())
array = list(map(int, input().split()))

def min_instability(array):
    array.sort()
    min_instability = array[-1] - array[0]

    for i in range(1, n-1):
        if array[i] - array[i-1] < min_instability:
            min_instability = array[i] - array[i-1]
        if array[i+1] - array[i] < min_instability:
            min_instability = array[i+1] - array[i]
    return min_instability

print(min_instability(array))
