

def main():
    macro = []
    route = []
    route_string = raw_input()
    route_len = len(route_string)
    for i in range(route_len):
        route.append(route_string[i])
    while len(route) > 0:
        if len(route) == 1:
            macro.append(route[0])
            del route[0]
        else:
            if route[0] == route[1]:
                macro.append('M')
                del route[0]
                del route[0]
            else:
                macro.append(route[0])
                del route[0]
    print len(macro)

main()
