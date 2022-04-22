
n = int(input())
a = list(map(int, input().split()))
max_cont = 0
cont = 0
for i in a:
    if i == 0:
        max_cont = max(max_cont, cont)
        cont = 0
    else:
        cont += 1
max_cont = max(max_cont, cont)
print(max_cont)
