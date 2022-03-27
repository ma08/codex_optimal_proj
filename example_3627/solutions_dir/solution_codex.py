
# def sort_arrays(arr1, arr2):
#     arr1.sort()
#     arr2.sort()
#     for i in range(len(arr1)):
#         if arr1[i] != arr2[i]:
#             arr1[arr2.index(arr1[i])], arr2[arr1.index(arr2[i])] = arr2[arr1.index(arr2[i])], arr1[arr2.index(arr1[i])]
#     return [arr1, arr2]

def sort_arrays(arr1, arr2):
    arr1.sort(key=lambda x: (arr2.index(x), x))
    arr2.sort(key=lambda x: (arr1.index(x), x))
    return [arr1, arr2]

arr1=[5,4,3,2,1]
arr2=[6,5,7,8,9]

print(sort_arrays(arr1, arr2))

#[[4,5,3,2,1],[9,8,7,5,6]]

# arr1=[2,1,3,4,5]
# arr2=[5,6,7,8,9]

# print(sort_arrays(arr1, arr2))

#[[2,1,3,4,5],[6,5,7,8,9]]

# arr1=[5,6,9,2,6,5]
# arr2=[3,6,7,4,8,1]

# print(sort_arrays(arr1, arr2))

#[[5,5,2,6,9,6],[4,3,1,6,8,7]]
