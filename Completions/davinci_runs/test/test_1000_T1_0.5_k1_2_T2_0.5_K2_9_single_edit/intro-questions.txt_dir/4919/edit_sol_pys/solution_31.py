n = int(input())  # number of elements in set A
A = set(map(int, input().split()))  # elements of set A
m = int(input())  # number of elements in set B
B = set(map(int, input().split()))  # elements of set B
print(len(A.union(B)))
