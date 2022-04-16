

def main():
    macro = []
    route_string = input()
    route_len = len(route_string)
    route = list(route_string)
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
    print(len(macro))

main()
