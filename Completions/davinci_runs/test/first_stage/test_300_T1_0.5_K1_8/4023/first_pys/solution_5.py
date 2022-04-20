

def vova_wall(n, a):
    """
    :param n: number of parts in the wall
    :param a: initial heights of the parts of the wall
    :return: YES if Vova can complete the wall using any amount of bricks (possibly zero).
    """
    # check if the wall is already complete
    if len(set(a)) == 1:
        return "YES"

    # check if the wall is already complete
    if len(set(a)) == 2:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 3:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 4:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 5:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 6:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 7:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 8:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 9:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

    # check if the wall is already complete
    if len(set(a)) == 10:
        # check if the wall has no empty spaces inside it
        if a[0] == a[-1]:
            return "YES"
        else:
            return "NO"

if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split()]
    print(vova_wall(n, a))