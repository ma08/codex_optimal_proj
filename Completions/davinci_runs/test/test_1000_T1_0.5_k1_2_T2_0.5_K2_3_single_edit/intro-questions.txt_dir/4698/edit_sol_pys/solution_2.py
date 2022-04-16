
# Get input
N = int(input())
T_list = list(map(int, input().split()))
M = int(input())
PX_list = [list(map(int, input().split())) for _ in range(M)]

# Solve
for P, X in PX_list:
    T_list[P - 1] = X
    print(sum(T_list)) 
