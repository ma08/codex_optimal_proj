
import sys
import itertools

def scale_check(notes_list):
    return (len(notes_list) == 8 and notes_list[0] == notes_list[7] and 
            notes_list[1] == notes_list[0] + 2 and notes_list[2] == notes_list[1] + 2 and
            notes_list[3] == notes_list[2] + 1 and notes_list[4] == notes_list[3] + 2 and
            notes_list[5] == notes_list[4] + 2 and notes_list[6] == notes_list[5] + 2)

def main():
    valid_scales = []
    n = int(sys.stdin.readline().strip())
    notes_list = map(int, sys.stdin.readline().strip().split())
    for i in xrange(n):
        for j in xrange(i+1, n):
            for k in xrange(j+1, n):
                for l in xrange(k+1, n):
                    for m in xrange(l+1, n):
                        for o in xrange(m+1, n):
                            for p in xrange(o+1, n):
                                for q in xrange(p+1, n):
                                    if scale_check(notes_list[i:q+1]):
                                        valid_scales.append(notes_list[i:q+1])    
    valid_scales = sorted(list(set(tuple(sorted(l)) for l in valid_scales)))
    valid_scales = [chr(l[0]+64) + ("#" if l[0] < 11 else "") for l in valid_scales]
    if len(valid_scales) == 0:
        print("none")
    else:
        print(" ".join(valid_scales))

if __name__ == '__main__':
    main()
