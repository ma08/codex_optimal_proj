

#----CODE----

#input
N = int(input())
a_list = list(map(int, input().split()))

#finds the max diff between two elements
def find_max_diff(a_list):
    max_diff = 0
    for i in range(N):
        for j in range(i+1, N):
            diff = a_list[j] - a_list[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(find_max_diff(a_list))
