

def check_if_unique(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


def check_if_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        if set(string1) == set(string2):
            return True
        return False


def remove_duplicates(string):
    new_string = ""
    for i in range(len(string)):
        if i == 0:
            new_string += string[0]
        elif string[i] != string[i - 1]:
            new_string += string[i]
    return new_string


def replace_spaces(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == " ":
            new_string += "%20"
        else:
            new_string += string[i]
    return new_string


def string_compression(string):
    new_string = ""
    count = 0
    for i in range(len(string)):
        if i == 0:
            count += 1
            new_string += string[0]
        elif string[i] != string[i - 1]:
            new_string += str(count)
            count = 1
            new_string += string[i]
        else:
            count += 1
    new_string += str(count)
    return new_string


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix


def zero_matrix(matrix):
    row = []
    column = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                column.append(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in row or j in column:
                matrix[i][j] = 0
    return matrix


def string_rotation(string1, string2):
    if len(string1) == len(string2):
        for i in range(len(string1)):
            if string1[i:] + string1[:i] == string2:
                return True
    return False


