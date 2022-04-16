

def main():
    macro = []
    route = []
    route_string = input()
    route_len = len(route_string)
    for i in range(route_len):
        route.append(route_string[i])
    while len(route) > 0:
        if len(route) == 1: #if there is only one node left in the route, append it to the macro
            macro.append(route[0])
            del route[0]
        else:
            if route[0] == route[1]: #if the first and second nodes are the same, append M to the macro
                macro.append('M')
                del route[0]
                del route[0]
            else:
                macro.append(route[0]) #if the first and second nodes are different, append the first node to the macro
                del route[0]
    print(len(macro))

main()
