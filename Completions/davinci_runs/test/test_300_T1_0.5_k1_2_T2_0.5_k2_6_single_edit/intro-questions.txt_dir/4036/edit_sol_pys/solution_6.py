

def find_min_arr(a, b, c):
    if a < b < c:
        return [1,2,3]
    elif a < c < b:
        return [1,3,2]
    elif b < a < c:
        return [2,1,3]
    elif b < c < a:
        return [2,3,1]
    elif c < a < b:
        return [3,1,2]
    elif c < b < a:
        return [3,2,1]
    else:
        return False

a = int(input())
b = int(input())
c = int(input())
arr = find_min_arr(a,b,c)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
