
def compress(route):
    if len(route) < 2:
        return route
    for i in range(1, len(route)):
        if route[i] == route[i-1]:
            return compress(route[:i-1] + 'M' + route[i+1:])
    return route

def encode(route):
    return route[0] + encode(route[1:]) if len(route) > 1 else route

def decode(route):
    return route[1] + decode(route[1:]) if len(route) > 1 and route[0] == 'M' else route[0] + decode(route[1:])

def expand(route):
    return route[1] + expand(route[1:]) if len(route) > 1 and route[0] == 'M' else route[0] + expand(route[1:])

if __name__ == '__main__':
    route = input()
    print(len(encode(compress(route))))
