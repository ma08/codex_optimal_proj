

n = int(input())
array = list(map(int, input().split()))

def find_set_of_blocks(array):
    if n == 1:
        return array[0]
    else:
        sum_array = sum(array)
        if sum_array % n != 0:
            return array[0]
        else:
            return sum_array / n

def find_index(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i

def find_blocks(array, number):
    index = find_index(array, number)
    blocks = []
    for i in range(len(array)):
        if array[i] == number:
            blocks.append([i+1, i+1])
        else:
            blocks.append([i+1, index])
    return blocks

print(len(find_blocks(array, find_set_of_blocks(array))))
for i in find_blocks(array, find_set_of_blocks(array)):
    print(' '.join(map(str, i)))