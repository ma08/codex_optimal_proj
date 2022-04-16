
import sys

def main():
    b, d, c, l = [int(x) for x in sys.stdin.readline().split()]
    solutions = []
    for num_birds in range(l//b + 1):  # l//b rounds down to the nearest integer, so we have to add 1
        for num_dogs in range(l//d + 1):  # to ensure that we count up to l.
            for num_cats in range(l//c + 1):  # Otherwise, we would miss the case where l is
                if num_birds*b + num_dogs*d + num_cats*c == l:  # exactly divisible by b, d, or c.
                    solutions.append([num_birds, num_dogs, num_cats])
    if solutions:
        solutions.sort()
        for sol in solutions:
            print(" ".join([str(x) for x in sol]))
    else:
        print("impossible")

main()
