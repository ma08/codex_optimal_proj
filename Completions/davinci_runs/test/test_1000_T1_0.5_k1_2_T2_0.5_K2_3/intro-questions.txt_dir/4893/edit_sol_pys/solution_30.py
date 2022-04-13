

#==============================================================
#=============================CODE=============================
#==============================================================


import sys

def main():
    input_ = sys.stdin.readline().split()
    n = int(input_[0])
    p = int(input_[1])
    input_ = sys.stdin.readline().split()
    cars = [int(i) for i in input_]
    print(cars)

main()
