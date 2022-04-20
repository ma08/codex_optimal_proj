

N, M, X, Y = list(map(int,input().split(" ")))
x = list(map(int,input().split(" ")))
y = list(map(int,input().split(" ")))

#X < Z <= Y
#x_1, x_2, ..., x_N < Z
#y_1, y_2, ..., y_M >= Z

if X < Y:
    for Z in range(X+1,Y+1):
        if all(i < Z for i in x) and all(i >= Z for i in y):
            print("No War")
            exit()
print("War")