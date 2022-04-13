

def check(reserve, damaged):
    for i in damaged:
        if i-1 in reserve:
            reserve.remove(i-1)
            damaged.remove(i)
        elif i+1 in reserve:
            reserve.remove(i+1)
            damaged.remove(i)
    return len(damaged)

N, S, R = map(int, raw_input().split())
damaged = map(int, raw_input().split())
reserve = map(int, raw_input().split())

print check(set(reserve), set(damaged))
