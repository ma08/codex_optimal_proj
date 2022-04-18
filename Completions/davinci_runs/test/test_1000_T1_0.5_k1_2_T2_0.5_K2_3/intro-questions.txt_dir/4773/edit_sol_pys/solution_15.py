

def main():
    n = int(input())
    for i in range(n):
        macro_string = []
        route_string = list(input())
        while len(route_string) > 0:
            if len(route_string) == 1:
                macro_string.append(route_string[0])
                del route_string[0]
            else:
                if route_string[0] == route_string[1]:
                    macro_string.append('M')
                    del route_string[0]
                    del route_string[0]
                else:
                    macro_string.append(route_string[0])
                    del route_string[0]
        print(len(macro_string))

main()
