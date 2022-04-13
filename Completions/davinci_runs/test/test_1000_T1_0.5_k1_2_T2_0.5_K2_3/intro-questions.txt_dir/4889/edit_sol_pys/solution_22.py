

n = int(input())
l = [int(x) for x in input().split()]

#l = [21,34,18,9,11,2]
#n = 6

def max_javalin(lis):
    if len(lis) == 1:
        return lis[0]
    else:
        lis = sorted(lis)
        return lis[-1] + max_javalin(lis[:-1]) - 1

print(max_javalin(l))
