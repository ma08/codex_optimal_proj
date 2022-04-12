
import sys

def main():
    b, d, c, l = map(int, sys.stdin.readline().split()) # b = number of 1-meter boards, d = number of 2-meter boards, c = number of 3-meter boards, l = length of the fence
    if l % 2 == 1 or l < b or l < d or l < c or l > b + d + c * 2: # if the length of the fence is odd or the number of boards is not enough to build the fence, print impossible
        print("impossible")
        return
    for i in range(0, l // b + 1): # iterate through all possible combinations of 1-meter boards
        for j in range(0, l // d + 1): # iterate through all possible combinations of 2-meter boards
            for k in range(0, l // c + 1): # iterate through all possible combinations of 3-meter boards
                if i * b + j * d + k * c == l: # if the combination of boards equals the length of the fence, print the combination
                    print(i, j, k) 

if __name__ == ("__main__"):
    main()
