import sys

def main():
    b, d, c, l = [int(x) for x in input().split()] #read in the input
    solutions = []
    for num_birds in range(l//b + 1): #iterate through all possible combinations of animals
        for num_dogs in range(l//d + 1):
            for num_cats in range(l//c + 1):
                if num_birds*b + num_dogs*d + num_cats*c == l: #check if the combination is a solution
                    solutions.append([num_birds, num_dogs, num_cats])
    if solutions:
        solutions.sort()
        for sol in solutions:
            print(" ".join([str(x) for x in sol]))
    else:
        print("impossible")

main()
