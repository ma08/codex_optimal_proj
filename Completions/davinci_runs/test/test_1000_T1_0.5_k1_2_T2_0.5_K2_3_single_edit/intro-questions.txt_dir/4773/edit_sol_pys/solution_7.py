

def main():
    macro = []
    route = []
    route_string = input()
    route_len = len(route_string)
    for i in range(route_len):
        route.append(route_string[i])
    while route:
        if len(route) == 1 and route[0] == 'R':
            macro.append(route[0])
            route.pop(0)
        elif len(route) == 1 and route[0] == 'L':
            macro.append(route[0])
            route.pop(0)
        else:
            if route[0] == route[1]:
                macro.append('M')
                route.pop(0)
            else:
                macro.append(route[0])
                route.pop(0)
    print(len(macro))

main()
