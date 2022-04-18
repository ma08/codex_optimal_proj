

import sys

def main():
    b, d, c, l = [int(x) for x in sys.stdin.readline().split()]  # b = birds, d = dogs, c = cats
    solutions = []
    for num_birds in range(l//b + 1):  # how many birds
        for num_dogs in range(l//d + 1):  # how many dogs
            for num_cats in range(l//c + 1):  # how many cats
                if num_birds*b + num_dogs*d + num_cats*c == l:  # if the total number of legs is correct
                    solutions.append([num_birds, num_dogs, num_cats])  # add it to the list of solutions
    if solutions:
        solutions.sort()  # sort the list of solutions
        for sol in solutions:
            print(" ".join([str(x) for x in sol]))  # print each solution
    else:
        print("impossible")  # if no solutions were found

main()
