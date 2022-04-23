
#----CODE----

#finds the max diff between two elements
def find_max_diff(A_list, N):
    max_diff = 0
    for i in range(N):
        for j in range(i+1, N):
            diff = A_list[j] - A_list[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(find_max_diff(A_list))
