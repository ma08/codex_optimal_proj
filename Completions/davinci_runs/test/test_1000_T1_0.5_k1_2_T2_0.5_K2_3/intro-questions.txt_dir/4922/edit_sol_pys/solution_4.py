
#get input
m, n = map(int, input().split()) #m = number of clauses, n = number of variables
clauses = []
for i in range(m):
    clauses.append(list(map(int, input().split())))

#check if it is unsatisfactory and print result
if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")
