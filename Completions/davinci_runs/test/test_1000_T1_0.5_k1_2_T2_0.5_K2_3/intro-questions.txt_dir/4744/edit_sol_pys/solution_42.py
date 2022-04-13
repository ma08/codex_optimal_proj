
import math

def main():
    v = int(input()) # volume
    print(find_cost(v)) # output

def find_cost(volume):
    cost = math.inf # set cost to infinity
    for i in range(1, int(math.sqrt(volume)) + 1): # iterate through possible dimensions
        if volume % i == 0:
            if 2 * i + 2 * (volume // i) < cost: # if new cost is less than current cost
                cost = 2 * i + 2 * (volume // i)
    return cost # return cost

if __name__ == "__main__":
    main()
