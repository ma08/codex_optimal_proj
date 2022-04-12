

C = int(input())
P = int(input())
#C = 6
#P = 5
H = [int(x) for x in input().split()]
#H = [2,1,1,1,0,1]

#print (C, P, H)

def get_piece_shape(P):
    if P == 1: # I
        return [[1,1,1,1]]
    elif P == 2: # L
        return [[1,1,1],
                [0,0,1]]
    elif P == 3: # J
        return [[1,1,1],
                [1,0,0]]
    elif P == 4: # O
        return [[1,1],
                [1,1]]
    elif P == 5: # T
        return [[1,1,1,1],
                [0,0,0,1]]
    elif P == 6: # S
        return [[1,1,1,1],
                [1,0,0,0]]
    elif P == 7: # Z
        return [[1,1,1],
                [0,0,1],
                [0,0,1]]

def get_rotated(shape): # returns all rotations of a shape
    if len(shape) == 4:
        return [shape]
    if len(shape) == 2:
        return [shape, [[shape[1][0],shape[0][0]],[shape[1][1],shape[0][1]]]]
    if len(shape) == 3:
        return [[shape[0],shape[1],shape[2]],
                [[shape[2][0],shape[1][0],shape[0][0]],[shape[2][1],shape[1][1],shape[0][1]],[shape[2][2],shape[1][2],shape[0][2]]],
                [[shape[2][0],shape[2][1],shape[2][2]],[shape[1][0],shape[1][1],shape[1][2]],[shape[0][0],shape[0][1],shape[0][2]]],
                [[shape[0][0],shape[1][0],shape[2][0]],[shape[0][1],shape[1][1],shape[2][1]],[shape[0][2],shape[1][2],shape[2][2]]]]

def get_shifted(shape, C): # returns all shifts of a shape
    if len(shape) == 4:
        return [[shape[0][i:]+[0]*(C-len(shape[0])+i) for i in range(C+1)]] # list of lists
    if len(shape) == 2:
        return [[shape[0][i:]+[0]*(C-len(shape[0])+i),shape[1][i:]+[0]*(C-len(shape[1])+i)] for i in range(C+1)] # list of lists of lists
    if len(shape) == 3:
        return [[shape[0][i:]+[0]*(C-len(shape[0])+i),shape[1][i:]+[0]*(C-len(shape[1])+i),shape[2][i:]+[0]*(C-len(shape[2])+i)] for i in range(C+1)] # list of lists of lists of lists

def get_all_shapes(P, C): # returns all possible shapes of a piece
    shape = get_piece_shape(P)
    rotated = get_rotated(shape)
    all_shapes = []
    for rot in rotated:
        all_shapes += get_shifted(rot, C)
    return all_shapes

def get_score(H, shape): # returns the score of a shape
    score = 0
    for i in range(len(shape)):
        score += H[i] - sum(shape[i])
    return score

def get_best_score(H, shapes): # returns the best score of a set of shapes
    best_score = 0
    for shape in shapes:
        if get_score(H, shape) > best_score:
            best_score = get_score(H, shape)
    return best_score

def get_num_shapes(H, shapes): # returns the number of shapes with the best score
    num_shapes = 0
    for shape in shapes:
        if get_score(H, shape) == get_best_score(H, shapes):
            num_shapes += 1
    return num_shapes

def get_num_possibilities(H, shapes): # returns the number of possibilities
    return get_best_score(H, shapes) * get_num_shapes(H, shapes)

shapes = get_all_shapes(P, C)
print(get_num_possibilities(H, shapes))
