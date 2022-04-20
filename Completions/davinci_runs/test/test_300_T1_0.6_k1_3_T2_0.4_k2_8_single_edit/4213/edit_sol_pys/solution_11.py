#----INPUT----
#5
#1 2 3 4 5

#----CODE----
N = int(input())
A_list = list(map(int, input().split()))

#----CODE----
def find_max_diff(A_list):
    max_diff = A_list[1] - A_list[0]
    for i in range(N):
        for j in range(0, i):
            if A_list[i] - A_list[j] > max_diff:
                max_diff = A_list[i] - A_list[j]
    return max_diff

print(find_max_diff(A_list))
