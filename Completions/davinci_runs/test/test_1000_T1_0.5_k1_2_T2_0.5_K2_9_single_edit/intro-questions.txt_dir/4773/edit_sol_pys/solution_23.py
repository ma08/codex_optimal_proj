"""
This program takes a route in string form and converts it into a series of
macro directions
"""

def main():
    macro = []
    route = []
    route_string = input("Enter your route: ")
    route_len = len(route_string)
    for i in range(route_len):
        route.append(route_string[i].upper())
    print(route)
    while len(route) > 0:
        if route[0] == route[1]:
            macro.append('M')
            del route[0]
            del route[0]
        elif route[0] == 'N':
            if route[1] == 'E':
                macro.append('R')
                del route[0]
                del route[0]
            elif route[1] == 'W':
                macro.append('L')
                del route[0]
                del route[0]
        elif route[0] == 'S':
            if route[1] == 'E':
                macro.append('L')
                del route[0]
                del route[0]
            elif route[1] == 'W':
                macro.append('R')
                del route[0]
                del route[0]
        elif route[0] == 'E':
            if route[1] == 'N':
                macro.append('L')
                del route[0]
                del route[0]
            elif route[1] == 'S':
                macro.append('R')
                del route[0]
                del route[0]
        elif route[0] == 'W':
            if route[1] == 'N':
                macro.append('R')
                del route[0]
                del route[0]
            elif route[1] == 'S':
                macro.append('L')
                del route[0]
                del route[0]
        elif len(route) == 1:
            macro.append('R')
            del route[0]
    print(len(macro))

main()
