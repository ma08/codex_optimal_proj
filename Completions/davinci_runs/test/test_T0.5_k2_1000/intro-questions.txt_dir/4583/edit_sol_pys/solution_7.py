

from itertools import product

def main():
    #get input
    ABCD = input() #ABCD is a string
    ABCD = list(ABCD)

    #all possible combinations of + and -
    #this is a list of tuples
    signs = list(product(["+","-"], repeat=3))

    #for each combination of signs
    for sign in signs:
        #create the formula and evaluate it
        result = ABCD[0] + sign[0] + ABCD[1] + sign[1] + ABCD[2] + sign[2] + ABCD[3] #result is a string
        #if the result is 7, print and exit
        if eval(result) == 7: #eval() returns an integer
            print(result + "=7")
            exit()

if __name__ == "__main__":
    main()
