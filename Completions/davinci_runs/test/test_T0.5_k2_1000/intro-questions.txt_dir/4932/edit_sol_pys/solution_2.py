
import sys

def main():
    agg, calm, agg2, calm2 = [int(n) for n in sys.stdin.readline().split()] # get input
    p, m, g = [int(n) for n in sys.stdin.readline().split()] # get input
    if (p - 1) % (agg + calm) < agg and (p - 1) % (agg2 + calm2) < agg2: # if p is aggressive in both
        print("both") # print both
    elif (p - 1) % (agg + calm) < agg or (p - 1) % (agg2 + calm2) < agg2: # if p is aggressive in one
        print("one") # print one
    else: # if p is aggressive in none
        print("none") # print none
    if (m - 1) % (agg + calm) < agg and (m - 1) % (agg2 + calm2) < agg2: # if m is aggressive in both
        print("both") # print both
    elif (m - 1) % (agg + calm) < agg or (m - 1) % (agg2 + calm2) < agg2: # if m is aggressive in one
        print("one") # print one
    else: # if m is aggressive in none
        print("none") # print none
    if (g - 1) % (agg + calm) < agg and (g - 1) % (agg2 + calm2) < agg2: # if g is aggressive in both
        print("both") # print both
    elif (g - 1) % (agg + calm) < agg or (g - 1) % (agg2 + calm2) < agg2: # if g is aggressive in one
        print("one") # print one
    else: # if g is aggressive in none
        print("none") # print none

main() # call main
