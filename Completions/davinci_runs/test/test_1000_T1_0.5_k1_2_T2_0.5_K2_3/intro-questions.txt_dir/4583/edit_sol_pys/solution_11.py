

from itertools import product

def main():
    #get input from user
    ABCD = input()
    ABCD = list(ABCD)

    #all possible combinations of + and -
    #this is a list of tuples
    signs = list(product(["+","-"], repeat=3))

    #for each combination of signs
    for sign in signs:
        #create the formula
        result = str(ABCD[0]) + sign[0] + str(ABCD[1]) + sign[1] + str(ABCD[2]) + sign[2] + str(ABCD[3])
        #if the result is 7, print and exit
        if eval(result) == 7:
            print(result + "=7")
            exit()

if __name__ == "__main__":
    main()
