

route = input().strip()

def compress(route, prev = None):
    if len(route) < 2:
        return route, prev
    for i in range(1, len(route)):
        if route[i] == route[i-1]:
            return compress(route[:i-1] + 'M' + route[i+1:], route[i-1])
    return route, prev

def encode(route, prev = None):
    return route[0] + encode(route[1:], route[0])

    if route[0] == 'M':
        return route[1] + decode(route[1:], route[1])
    else:
        return route[0] + decode(route[1:], route[0])

def expand(route, prev = None):
    if route[0] == 'M':
        return route[1] + decode(route[1:])
    else:
        return route[0] + decode(route[1:])

print(len(encode(compress(route)[0])))
