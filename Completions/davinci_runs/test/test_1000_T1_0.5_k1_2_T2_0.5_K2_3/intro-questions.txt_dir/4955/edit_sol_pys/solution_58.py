

import sys
import itertools

def scale_check(notes):
    return len(notes) == 8 and notes[0] == notes[7] and notes[1] == notes[0] + 2 and notes[2] == notes[1] + 2 and notes[3] == notes[2] + 1 and notes[4] == notes[3] + 2 and notes[5] == notes[4] + 2 and notes[6] == notes[5] + 2

def main():
    notes = []
    valid_scales = []
    n = int(sys.stdin.readline().strip())
    notes = list(map(int, sys.stdin.readline().strip().split()))
    for i in xrange(n):
        for j in xrange(i+1, n):
            for k in xrange(j+1, n):
                for l in xrange(k+1, n):
                    for m in xrange(l+1, n):
                        for o in xrange(m+1, n):
                            for p in xrange(o+1, n):
                                for q in xrange(p+1, n):
                                    if scale_check(notes[i:q+1]): valid_scales.append(notes[i:q+1])    
    valid_scales = sorted(list(set(tuple(sorted(l)) for l in valid_scales)))
    valid_scales = [chr(l[0]+64) + ("#" if l[0] < 11 else "") for l in valid_scales]    
    print("none" if len(valid_scales) == 0 else " ".join(valid_scales))

if __name__ == '__main__':
    main()
