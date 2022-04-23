
import sys

def main():
    n, b, a = [int(i) for i in input().strip().split(' ')]
    s = [int(i) for i in input().strip().split(' ')]
    b_left = b # battery for 0
    a_left = a # battery for 1

    max_segments = 0 # max number of segments
    i = 0
    while i < n:
        if b_left == 0: # no more battery for 0
            if a_left > 0: # check if there is battery for 1
                a_left -= 1
                max_segments += 1
            else:
                break
        elif a_left == 0: # no more battery for 1
            if b_left > 0: # check if there is battery for 0
                b_left -= 1
                max_segments += 1
            else:
                break
        elif s[i] == 1: # segment is 1
            if a_left < a: # check if there is room for more battery for 1
                a_left += 1
                b_left -= 1
                max_segments += 1
            elif b_left > 0: # check if there is battery for 0
                b_left -= 1
                max_segments += 1
            else:
                break
        elif s[i] == 0: # segment is 0
            if a_left > 0: # check if there is battery for 1
                a_left -= 1
                max_segments += 1
            elif b_left > 0: # check if there is battery for 0
                b_left -= 1
                max_segments += 1
            else:
                break
        i += 1
    print(max_segments) # print max number of segments

main()
