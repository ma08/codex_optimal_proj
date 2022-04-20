

# first solution
def image():
    data = [int(input()) for i in range(4)]
    if data == [0, 1, 1, 0]:
        return 0
    elif data == [0, 1, 0, 1]:
        return 1
    elif data == [1, 0, 0, 1]:
        return 0
    else:
        return 1

# second solution
def image():
    data = [int(input()) for i in range(4)]
    if data == [0, 1, 1, 0] or data == [1, 0, 0, 1]:
        return 0
    else:
        return 1

# third solution
def image():
    data = [int(input()) for i in range(4)]
    return 1 if (data[0] ^ data[2] ^ data[1] ^ data[3]) == 1 else 0

# fourth solution
def image():
    data = [int(input()) for i in range(4)]
    return int((data[0] ^ data[2]) != (data[1] ^ data[3]))
