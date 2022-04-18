

route = input('Enter string: ')

def compress(route):
    if len(route) < 2:
        return route, len(route)
    for i in range(1, len(route)):
        if route[i] == route[i-1]:
            return compress(route[:i-1] + 'M' + route[i+1:]), len(route)
    return route, len(route)

def encode(route):
    if len(route) < 2:
        return route, len(route)
    else:
        return route[0] + encode(route[1:])[0], len(route)

def decode(route):
    if len(route) < 2:
        return route, len(route)
    else:
        if route[0] == 'M':
            return route[1] + decode(route[1:])[0], len(route)
        else:
            return route[0] + decode(route[1:])[0], len(route)

def expand(route):
    if len(route) < 2:
        return route, len(route)
    else:
        if route[0] == 'M':
            return route[1] + expand(route[1:])[0], len(route)
        else:
            return route[0] + expand(route[1:])[0], len(route)

print(len(encode(compress(route)[0])))
