
import sys
import itertools

def scale_check(notes):
    if len(notes) != 8:
        return False
    elif notes[0] != notes[7]:
        return False
    elif notes[1] != notes[0] + 2:
        return False
    elif notes[2] != notes[1] + 2:
        return False
    elif notes[3] != notes[2] + 1:
        return False
    elif notes[4] != notes[3] + 2:
        return False
    elif notes[5] != notes[4] + 2:
        return False
    elif notes[6] != notes[5] + 2:
        return False
    else:
        return True

def main():
    notes = []
    valid_scales = []
    n = int(sys.stdin.readline().strip())
    notes = map(int, sys.stdin.readline().strip().split())
    for i in xrange(n):
        for j in xrange(i+1, n):
            for k in xrange(j+1, n):
                for l in xrange(k+1, n):
                    for m in xrange(l+1, n):
                        for o in xrange(m+1, n):
                            for p in xrange(o+1, n):
                                for q in xrange(p+1, n):
                                    if scale_check(notes[i:q+1]):
                                        valid_scales.append(notes[i:q+1])
    valid_scales = list(set(tuple(sorted(l)) for l in valid_scales))
    valid_scales = [list(l) for l in valid_scales]
    valid_scales = sorted(valid_scales, key=lambda x: x[0])
    valid_scales = [chr(l[0]+64) + ("#" if l[0] < 11 else "") for l in valid_scales] 
    if len(valid_scales) == 0:
        print "none"
    else:
        print " ".join(valid_scales)

if __name__ == '__main__':
    main()
