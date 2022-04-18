

import sys

def main():
    a, b = map(int, sys.stdin.readline().split()) # a = rent, b = cost
    m, sigma = map(int, sys.stdin.readline().split()) # m = max number of apartments, sigma = total rent
    n = int(sys.stdin.readline()) # n = number of apartments
    apartments = []
    for i in range(n):
        apartments.append(list(map(int, sys.stdin.readline().split()))) # apartments[i][0] = rent, apartments[i][1] = cost

    # we want to maximize the sum of the rents
    # subject to the constraint that the sum of the costs is less than or equal to b
    # and the number of apartments is less than or equal to m
    # and the total rent is less than or equal to sigma
    # and each apartment is rented

    # let x_i = 1 if we rent the ith apartment and 0 otherwise
    # we want to maximize sum_i r_i x_i
    # subject to sum_i c_i x_i <= b
    # and sum_i x_i <= m
    # and sum_i r_i x_i <= sigma
    # and x_i >= 1

    # let z = sum_i r_i x_i
    # x_i >= 1 => x_i <= z
    # sum_i x_i <= m => sum_i x_i <= mz
    # sum_i r_i x_i <= sigma => sum_i r_i x_i <= sigma z
    # sum_i c_i x_i <= b => sum_i c_i x_i <= bz
    # so we have a system of inequalities
    # x_i <= z
    # sum_i x_i <= mz
    # sum_i r_i x_i <= sigma z
    # sum_i c_i x_i <= bz
    # x_i >= 1
    # we want to maximize z

    # let A = [c_1, ..., c_n], b = [b, m, sigma]
    # then we want to maximize z
    # subject to A x <= b
    # and x >= 1

    # we can use the simplex algorithm to solve this

    # add slack variables
    # add slack variables to the first three inequalities
    # add surplus variables to the last three inequalities

    # A = [[c_1, ..., c_n, 1, 0, 0, 0, 0, 0],
    #      [1, ..., 1, 0, 1, 0, 0, 0, 0],
    #      [r_1, ..., r_n, 0, 0, 1, 0, 0, 0],
    #      [0, ..., 0, -1, 0, 0, 1, 0, 0],
    #      [0, ..., 0, 0, -1, 0, 0, 1, 0],
    #      [0, ..., 0, 0, 0, -1, 0, 0, 1]]
    # b = [b, m, sigma, 0, 0, 0]
    # c = [0, ..., 0, 0, 0, 0, 1, 1, 1]

    # we want to maximize c^T x
    # subject to A x <= b
    # and x >= 1

    # we can use the simplex algorithm to solve this

    # let x = [x_1, ..., x_n, z_1, z_2, z_3, s_1, s_2, s_3]
    # then we want to maximize [0, ..., 0, 0, 0, 0, 1, 1, 1]^T x
    # subject to [[c_1, ..., c_n, 1, 0, 0, 0, 0, 0],
    #            [1, ..., 1, 0, 1, 0, 0, 0, 0],
    #            [r_1, ..., r_n, 0, 0, 1, 0, 0, 0],
    #            [0, ..., 0, -1, 0, 0, 1, 0, 0],
    #            [0, ..., 0, 0, -1, 0, 0, 1, 0],
    #            [0, ..., 0, 0, 0, -1, 0, 0, 1]] x <= [b, m, sigma, 0, 0, 0]
    # and x >= [1, ..., 1, 0, 0, 0, 0, 0, 0]

    # we can use the simplex algorithm to solve this

    # let x = [x_1, ..., x_n, z_1, z_2, z_3, s_1, s_2, s_3]
    # then we want to maximize [0, ..., 0, 0, 0, 0, 1, 1, 1]^T x
    # subject to [[c_1, ..., c_n, 1, 0, 0, 0, 0, 0],
    #            [1, ..., 1, 0, 1, 0, 0, 0, 0],
    #            [r_1, ..., r_n, 0, 0, 1, 0, 0, 0],
    #            [0, ..., 0, -1, 0, 0, 1, 0, 0],
    #            [0, ..., 0, 0, -1, 0, 0, 1, 0],
    #            [0, ..., 0, 0, 0, -1, 0, 0, 1]] x <= [b, m, sigma, 0, 0, 0]
    # and x >= [1, ..., 1, 0, 0, 0, 0, 0, 0]

    # we can use the simplex algorithm to solve this

    # let x = [x_1, ..., x_n, z_1, z_2, z_3, s_1, s_2, s_3]
    # then we want to maximize [0, ..., 0, 0, 0, 0, 1, 1, 1]^T x
    # subject to [[c_1, ..., c_n, 1, 0, 0, 0, 0, 0],
    #            [1, ..., 1, 0, 1, 0, 0, 0, 0],
    #            [r_1, ..., r_n, 0, 0, 1, 0, 0, 0],
    #            [0, ..., 0, -1, 0, 0, 1, 0, 0],
    #            [0, ..., 0, 0, -1, 0, 0, 1, 0],
    #            [0, ..., 0, 0, 0, -1, 0, 0, 1]] x <= [b, m, sigma, 0, 0, 0]
    # and x >= [1, ..., 1, 0, 0, 0, 0, 0, 0]

    # we can use the simplex algorithm to solve this

    # let x = [x_1, ..., x_n, z_1, z_2, z_3, s_1, s_2, s_3]
    # then

if __name__ == "__main__":
    main()
