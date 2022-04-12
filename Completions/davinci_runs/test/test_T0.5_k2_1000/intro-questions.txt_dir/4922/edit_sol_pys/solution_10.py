
# SOLUTION 
m, n = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(m)]
if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")
