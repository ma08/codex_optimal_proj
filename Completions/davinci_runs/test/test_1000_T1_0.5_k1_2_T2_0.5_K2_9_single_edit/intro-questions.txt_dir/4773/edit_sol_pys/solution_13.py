
def compress(route):
    if len(route) < 2:
        return route
    for i in range(1, len(route)):
        if route[i] == route[i-1]:
            return compress(route[:i-1] + 'M' + route[i+1:])
    return route

def encode(route):
    if len(route) < 2:
        return route
    else:
        return route[0] + encode(route[1:])

def decode(route):
    if len(route) < 2:
        return route
    else:
        if route[0] == 'M':
            return route[1] + decode(route[1:])
        else:
            return route[0] + decode(route[1:])

def expand(route):
    if len(route) < 2:
        return route
    else:
        if route[0] == 'M':
            return route[1] + expand(route[1:])
        else:
            return route[0] + expand(route[1:])
