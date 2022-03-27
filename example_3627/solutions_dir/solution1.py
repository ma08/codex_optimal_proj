import numpy as np

def sort_two_arrays(arr1, arr2):
    idx2 = np.argsort(arr2, kind='mergesort')
    idx1 = np.argsort(arr1, kind='mergesort')
    return [[arr1[i] for i in idx2], [arr2[i] for i in idx1]]


arr1=[5,4,3,2,1]
arr2=[6,5,7,8,9]

print(sort_two_arrays(arr1, arr2))

#[[4,5,3,2,1],[9,8,7,5,6]]

arr1=[2,1,3,4,5]
arr2=[5,6,7,8,9] 

print(sort_two_arrays(arr1, arr2))

#[[2,1,3,4,5],[6,5,7,8,9]]

arr1=[5,6,9,2,6,5]
arr2=[3,6,7,4,8,1]

print(sort_two_arrays(arr1, arr2))

#[[5,5,2,6,9,6],[4,3,1,6,8,7]]
