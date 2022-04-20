

def image():
    """
    >>> image()
    0
    """
    lines = [int(input()) for i in range(4)]
    print(int(not(lines[0] == lines[2] and lines[1] == lines[3])))

if __name__ == "__main__":
    import doctest
    doctest.testmod()