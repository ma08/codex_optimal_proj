
n = int(input('Enter the number of elements in the array: '))
array = list(map(int, input().split()))


    """
    Find the minimum instability of an array
    :param n: number of elements in the array
    :param array: list of integers
    :return: minimum instability
    """
def min_instability(n, array):
    array.sort()
    min_instability = array[-1] - array[0]

    for i in range(1, n - 1):
        if array[i] - array[i - 1] < min_instability:
            min_instability = array[i] - array[i - 1]
        if array[i + 1] - array[i] < min_instability:
            min_instability = array[i + 1] - array[i]
    return min_instability


print('Minimum instability:', min_instability(n, array))
