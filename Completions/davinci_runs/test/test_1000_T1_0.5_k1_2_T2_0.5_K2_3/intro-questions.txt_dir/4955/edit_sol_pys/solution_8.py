import sys
import itertools

def scale_check(notes):
    if len(notes) != 7:
        return False
    elif notes[0] != notes[6]:
        return False
    elif notes[1] != notes[0] + 1:
        return False
    elif notes[2] != notes[1] + 1:
        return False
    elif notes[3] != notes[2] + 2:
        return False
    elif notes[4] != notes[3] + 2:
        return False
    elif notes[5] != notes[4] + 1:
        return False
    # elif notes[6] != notes[5] + 2:
    #     return False
    else:
        return True

def main():
    n = int(sys.stdin.readline().strip())
    notes = map(int, sys.stdin.readline().strip().split())
    valid_scales = [notes[i:i+7] for i in xrange(n-6) if scale_check(notes[i:i+7])]
    valid_scales = list(set(tuple(sorted(l)) for l in valid_scales if l[0] < l[6]))
    valid_scales = [list(l) for l in valid_scales]
    valid_scales = sorted(valid_scales, key=lambda x: x[0])
    valid_scales = [chr(l[0]+64) + ("#" if l[0] < 10 else "") for l in valid_scales]
    if len(valid_scales) == 0:
        print "none"
    else:
        print " ".join(valid_scales)

if __name__ == '__main__':
    main()
