

# ---=== FUNCTIONS ===--- #
def get_input():
    """
    Gets and returns input from stdin.
    """
    n = int(input())
    a = [int(x) for x in input().split()]
    return n, a

def get_gis(a):
    """
    Returns the GIS of the given sequence.
    """
    n = len(a)
    gis = [a[0]]
    for i in range(1, n):
        if a[i] > gis[-1]:
            gis.append(a[i])
    return gis

def print_gis(gis):
    """
    Prints the given GIS.
    """
    print(len(gis))
    print(" ".join([str(x) for x in gis]))

# ---=== MAIN ===--- #
n, a = get_input()
gis = get_gis(a)
print_gis(gis)
