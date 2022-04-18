

n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

diag1 = [x[i] + y[i] for i in range(n)]
diag2 = [x[i] - y[i] for i in range(n)]

if len(set(x)) == len(x) and len(set(y)) == len(y) and len(set(diag1)) == len(diag1) and len(set(diag2)) == len(diag2):
    print('CORRECT')
else:
    print('INCORRECT')
