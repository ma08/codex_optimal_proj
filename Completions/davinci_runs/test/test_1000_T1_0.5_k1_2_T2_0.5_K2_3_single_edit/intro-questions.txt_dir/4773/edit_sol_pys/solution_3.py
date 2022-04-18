

route = input('Enter route: ')

def compress(route, prev = None):
    if len(route) < 2:
        return route
    for i in range(1, len(route)):
        if route[i] == route[i-1]:
            return compress(route[:i-1] + 'M' + route[i+1:], 'M')
    return route

def encode(route, prev = None):
    if len(route) < 2:
        return route
    else:
        return route[0] + encode(route[1:], route[0])

def decode(route, prev = None):
    if len(route) < 2:
        return route
    else:
        if route[0] == 'M':
            return route[1] + decode(route[1:], route[1])
        else:
            return route[0] + decode(route[1:], route[0])

def expand(route, prev = None):
    if len(route) < 2:
        return route
    else:
        if route[0] == 'M':
            return route[1] + expand(route[1:], route[1])
        else:
            return route[0] + expand(route[1:], route[0])

print(encode(compress(route)))
